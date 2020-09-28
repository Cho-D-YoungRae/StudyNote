#### 5. 시세 DB 구축 및 시세 조회 API 개발
---
##### 5.1 야후 파이낸스와 네이버 금융 비교하기
---
###### 5.1.1 야후 파이낸스 데이터의 문제점
---
- 한국 주식 종목들의 데이터는 종가 및 수정 종가가 정확하지 않다.
- 한국 주식 종목들은 2017년 10월 3주가량 데이터가 비어있다.

부정확한 야후 파이낸스 데이터 대신 네이버 금융의 주식 데이터를 스크레이핑해서 데이터베이스를 구축한 뒤, 이를 언제든지 조회할 수 있도록 시세 API를 만들어보자.

##### 5.2 마리아디비 설치 후 접속 확인 -> MySQL 이용함
---
###### 5.2.4 pymysql로 버전 정보 확인하기
---
데이터베이스에서 변경된 내역을 영구적으로 확정하는 것을 커밋(commit)이라고 한다. pymysql의 `connection` 객체의 `autocommit` 속성은 기본적으로 False 이기 때문에 INSERT, UPDATE, DELETE 등 데이터를 변경하더라도 `connection.commit()` 함수를 호출해야 실제로 데이터베이스에 반영된다. 이때 `commit()` 함수는 커서 객체가 아닌 커넥션 객체에서 호출해야한다.
```python
import pymysql

if __name__ == '__main__':

    connection = pymysql.connect(host='localhost', port=3306,\
                                 db='INVESTAR', user='root', \
                                 passwd='비밀번호', autocommit=True)   # 1

    cursor = connection.cursor()    # 2
    cursor.execute("SELECT VERSION();") # 3
    result = cursor.fetchone()  # 4

    print("MySQL version : {}".format(result))

    connection.close()
```
1. `connect()` 함수를 이용해 `connection` 객체를 생성한다.
2. `cursor()` 함수를 사용해 `cursor` 객체를 생성한다.
3. `cursor` 객체의 `execute()` 함수를 사용해 sql문을 실행한다.
4. `cursor` 객체의 `fetchon()` 함수를 사용해 3의 실행 결과를 튜플로 받는다.

##### 5.3 주식 시세를 매일 DB로 업데이트하기
---
import된 모듈들
```python
import pandas as pd
from bs4 import BeautifulSoup
import urllib, pymysql, calendar, time, json
from urllib.request import urlopen
from datetime import datetime
from threading import Timer
```
###### 5.3.4 pymysql로 테이블 생성하기
---
```python
class DBUpdater:  
    def __init__(self):
        """생성자: MariaDB 연결 및 종목코드 딕셔너리 생성"""
        self.conn = pymysql.connect(host='localhost', user='root',
            password='비밀번호', db='INVESTAR', charset='utf8')
        
        with self.conn.cursor() as curs:
            sql = """
            CREATE TABLE IF NOT EXISTS company_info (
                code VARCHAR(20),
                company VARCHAR(40),
                last_update DATE,
                PRIMARY KEY (code))
            """
            curs.execute(sql)
            sql = """
            CREATE TABLE IF NOT EXISTS daily_price (
                code VARCHAR(20),
                date DATE,
                open BIGINT(20),
                high BIGINT(20),
                low BIGINT(20),
                close BIGINT(20),
                diff BIGINT(20),
                volume BIGINT(20),
                PRIMARY KEY (code, date))
            """
            curs.execute(sql)
        self.conn.commit()

        self.codes = dict()
        self.update_comp_info() # 1

    def __del__(self):
        """소멸자: MariaDB 연결 해제"""
        self.conn.close() 
```
1. KRX 주식 코드를 읽어와서 DB의 company_info 테이블에 업데이트하는 것이다.

###### 5.3.5 종목코드 구하기
---
한국거래소 사이트에서 제공하는 '상장법인목록.xls' 파일을 다운로드해 문자열로 변경하는 코드다. 법인목록 파일을 일겅서 데이터프레임으로 반환한 뒤 종목코드와 회사명을 제외한 나머지 칼럼을 제거해보자.
```python
class DBUpdater:
    def read_krx_code(self):
        """KRX로부터 상장기업 목록 파일을 읽어와서 데이터프레임으로 반환"""
        url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method='\
            'download&searchType=13'
        krx = pd.read_html(url, header=0)[0]    # 1
        krx = krx[['종목코드', '회사명']]   # 2
        krx = krx.rename(columns={'종목코드': 'code', '회사명': 'company'}) # 3
        krx.code = krx.code.map('{:06d}'.format)    # 4
        return krx
```
1. '상장법인목록.xls' 파일을 `read_html()` 함수로 읽는다.
2. 종목코드 칼럼과 회사명만 남긴다. 데이터프레임에 [[]]을 사용하면 특정 칼럼만 뽑아서 원하는 순서대로 재구성할 수 있다.
3. 한글 칼럼명을 영문 칼럼명으로 변경한다.
4. 종목코드 형식을 {:06d} 형식의 문자열로 변경한다.

###### 5.3.6 종목코드를 DB에 업데이트하기
---
KRX 사이트로부터 종목코드 리스트를 읽어오는데 다소 시간이 걸리므로, 하루에 한 번만 읽어서 업데이트하자. company_info 테이블에 last_update 칼럼을 조회하여 오늘 날짜로 업데이트한 기록이 있으면 더는 업데이트하지 않도록 했다.

**`REPLACE INTO 구문**
일반적으로 테이블에 데이터 행을 삽입하는데 `INSERT INTO` 구문을 사용하지만, 이는 데이터 행이 테이블에 이미 존재하면 오류가 발생해 프로그램이 종료된다.


표준 SQL문은 아니지만 MySQL(+mariaDB) 에서 제공하는 `REPLACE INTO` 구문을 사용하면, 동일한 데이터 행이 존재하더라도 오류를 발생하지 않고 `UPDATE` 를 수행한다. 이처럼 `INSERT`와 `UPDATE`를 합쳐놓은 기능을 `UPSERT`라고 부르기도 한다.

```python
class DBUpdater:
    def update_comp_info(self):
        """종목코드를 company_info 테이블에 업데이트 한 후 딕셔너리에 저장"""
        sql = "SELECT * FROM company_info"
        df = pd.read_sql(sql, self.conn)    # 1
        for idx in range(len(df)):
            self.codes[df['code'].values[idx]] = df['company'].values[idx]  # 2
                    
        with self.conn.cursor() as curs:
            sql = "SELECT max(last_update) FROM company_info"
            curs.execute(sql)
            rs = curs.fetchone()    # 3
            today = datetime.today().strftime('%Y-%m-%d')

            if rs[0] == None or rs[0].strftime('%Y-%m-%d') < today: # 4
                krx = self.read_krx_code()  # 5
                for idx in range(len(krx)):
                    code = krx.code.values[idx]
                    company = krx.company.values[idx]                
                    sql = f"REPLACE INTO company_info (code, company, last"\
                        f"_update) VALUES ('{code}', '{company}', '{today}')"
                    curs.execute(sql)   # 6
                    self.codes[code] = company  # 7
                    tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                    print(f"[{tmnow}] #{idx+1:04d} REPLACE INTO company_info "\
                        f"VALUES ({code}, {company}, {today})")
                self.conn.commit()
                print('')              
```                
1. `company_info` 테이블을 `read_sql()` 함수로 읽는다.
2. 1에서 읽은 데이터프레임을 이요해서 종목코드와 회사명으로 codes 딕셔너리를 만든다.
3. DB에서 가장 최근 업데이트 날짜를 가져온다.
4. 3에서 구한 날짜가 존재하지 않거나 오늘보다 오래된 경우에만 업데이트한다.
5. KRX 상장기업 목록 파일을 읽어서 krx 데이터프레임에 저장한다.
6. `REPLACE INTO` 구문을 사용해서 '종목코드, 회사명, 오늘날짜' 행을 DB에 저장한다.
7. codes 딕셔너리에 '키-값'으로 종목코드와 회사명을 추가한다.


###### 5.3.7 주식 시세 데이터 읽어오기
---
`pgrr` 클래스의 `<td>` 태그가 존재하지 않으면 `AttributeError` 가 발생하면서 프로그램이 종료되므로, `find()` 함수 결과가 `None`인 경우에는 다음 종목을 처리하도록 변경했다. `read_html()` 함수로 주식 시세 페이지를 읽어올 때도 HTTP Error가 발생하면서 프로그램이 종료될 수 있으므로, 예외 처리르 했다.

```python
class DBUpdater:
    def read_naver(self, code, company, pages_to_fetch):
        """네이버에서 주식 시세를 읽어서 데이터프레임으로 반환"""
        try:
            url = f"http://finance.naver.com/item/sise_day.nhn?code={code}"
            with urlopen(url) as doc:
                if doc is None:
                    return None
                html = BeautifulSoup(doc, "lxml")
                pgrr = html.find("td", class_="pgRR")
                if pgrr is None:
                    return None
                s = str(pgrr.a["href"]).split('=')
                lastpage = s[-1]    # 1
            df = pd.DataFrame()
            pages = min(int(lastpage), pages_to_fetch)  # 2
            for page in range(1, pages + 1):
                pg_url = '{}&page={}'.format(url, page)
                df = df.append(pd.read_html(pg_url, header=0)[0])   # 3
                tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
                print('[{}] {} ({}) : {:04d}/{:04d} pages are downloading...'.
                    format(tmnow, company, code, page, pages), end="\r")
            df = df.rename(columns={'날짜':'date','종가':'close','전일비':'diff'
                ,'시가':'open','고가':'high','저가':'low','거래량':'volume'})   # 4
            df['date'] = df['date'].replace('.', '-')   # 5
            df = df.dropna()
            df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close',
                'diff', 'open', 'high', 'low', 'volume']].astype(int)   # 6
            df = df[['date', 'open', 'high', 'low', 'close', 'diff', 'volume']] # 7
        except Exception as e:
            print('Exception occured :', str(e))
            return None
        return df
```
1. 네이버 금융에서 일별 시세의 마지막 페이지를 구한다.
2. 설정 파일에 설정된 페이지 수(pages_to_fetch)와 1의 페이지 수에서 작은 것을 택한다.
3. 일별 시세 페이지를 `read_html()` 로 읽어서 데이터프레임에 추가한다.
4. 네이버 금융의 한글 칼럼명을 영문 칼럼명으로 변경한다.
5. 연. 월. 일 형식의 일자 데이터를 연-월-일 형식으로 변경한다.
6. DB에서 `BIGINT`형으로 지정한 칼럼들의 데이터형을 int형으로 변경한다.
7. 원하는 순서로 칼럼을 재조합하여 데이터프레임을 만든다.

###### 5.3.8 일별 시세 데이터를 DB에 저장하기
---
`read_naver()` 메서드로 읽어온 네이버 일별 시세를 DB에 저장하는 `replace_into_db()`메소드다. pandas의 `to_sql()` 함수를 사용해서 DB에 저장할 수도 있지만, 그러려면 종목별로 테이블을 구성해야 하고 이 함수는 데이터를 저장할 때 기존 테이블을 전체적으로 교체하기 때문에 효율적이지 않다.

다음처럼 한 테이블에 전체 종목의 시세 데이터를 기록하면 테이블 크기가 커져서 성능 면에서 다소 바람직하지 않지만, 소스 코드를 간단히 작성할 수 있다. 여기서는 `daily_price` 테이블 하나에 전체 종목의 시세 데이터를 저장했다.

```python
class DBUpdater:
    def replace_into_db(self, df, num, code, company):
        """네이버에서 읽어온 주식 시세를 DB에 REPLACE"""
        with self.conn.cursor() as curs:
            for r in df.itertuples():   # 1
                sql = f"REPLACE INTO daily_price VALUES ('{code}', "\
                    f"'{r.date}', {r.open}, {r.high}, {r.low}, {r.close}, "\
                    f"{r.diff}, {r.volume})"
                curs.execute(sql)   # 2
            self.conn.commit()  # 3
            print('[{}] #{:04d} {} ({}) : {} rows > REPLACE INTO daily_'\
                'price [OK]'.format(datetime.now().strftime('%Y-%m-%d'\
                ' %H:%M'), num+1, company, code, len(df)))
```
1. 인수로 넘겨받은 데이터프레임을 튜플로 순회처리한다.
2. `REPLACE INTO` 구문으로 `daily_price` 테이블을 업데이트한다.
3. `commit()` 함수를 호출에 DB에 반영한다.

`update_daily_price()` 메소드는 전체 상장법인의 주식 시세를 네이버에서 읽어 DB에 업데이트한다.

```python
class DBUpdater: 
    def update_daily_price(self, pages_to_fetch):
        """KRX 상장법인의 주식 시세를 네이버로부터 읽어서 DB에 업데이트"""  
        for idx, code in enumerate(self.codes): # 1
            df = self.read_naver(code, self.codes[code], pages_to_fetch)    # 2
            if df is None:
                continue
            self.replace_into_db(df, idx, code, self.codes[code])   # 3
```
1. `self.codes` 딕셔너리에 저장된 모든 종목코드에 대해 순회처리한다.
2. `read_naver()` 메소드를 이용하여 종목코드에 대한 일별 시세 데이터 프레임을 구한다.
3. 일별 시세 데이터프레임이 구해지면 `replace_into_db()` 메소드로 DB에 저장한다.

###### 5.3.9 json을 이용한 업데이트 페이지 수 설정
---
`config.json` 파일을 이용해 `DBUpdater`가 처음 실행되었는지 여부를 체크한다. `config.json` 파일이 없으면 `DBUpdater`가 처음 실행되는 경우이므로 종목별로 100페이지씩 가져온다. 최초 업데이트한 이후부터는 1페이지씩 가져오도록 `config.json` 파일이 자동으로 변경된다. 만일 업데이트할 페이지 수를 변경하려면 `config.json` 파일의 `pages_to_fetch`값을 수정하면 된다.

다음 `execute_daily()` 메소드는 `DBUpdater.py` 모듈의 시작 포인트다.
```python
class DBUpdater: 
    def execute_daily(self):
        """실행 즉시 및 매일 오후 다섯시에 daily_price 테이블 업데이트"""
        self.update_comp_info() # 1
        
        try:
            with open('config.json', 'r') as in_file:   # 2
                config = json.load(in_file)
                pages_to_fetch = config['pages_to_fetch']   # 3
        except FileNotFoundError:   # 4
            with open('config.json', 'w') as out_file:
                pages_to_fetch = 100    # 5
                config = {'pages_to_fetch': 1}
                json.dump(config, out_file)
        self.update_daily_price(pages_to_fetch) # 6

        tmnow = datetime.now()
        lastday = calendar.monthrange(tmnow.year, tmnow.month)[1]   # 7
        if tmnow.month == 12 and tmnow.day == lastday:
            tmnext = tmnow.replace(year=tmnow.year+1, month=1, day=1,
                hour=17, minute=0, second=0)
        elif tmnow.day == lastday:
            tmnext = tmnow.replace(month=tmnow.month+1, day=1, hour=17,
                minute=0, second=0)
        else:
            tmnext = tmnow.replace(day=tmnow.day+1, hour=17, minute=0,
                second=0)   
        tmdiff = tmnext - tmnow
        secs = tmdiff.seconds
        t = Timer(secs, self.execute_daily) # 8
        print("Waiting for next update ({}) ... ".format(tmnext.strftime
            ('%Y-%m-%d %H:%M')))
        t.start()
```
1. `update_comp_info()` 메소드를 호출하여 상장 법인 목록을 DB에 업데이트한다.
2. `DBUpdater.py`가 있는 디렉터리에서 `config.json` 파일을 읽기 모드로 연다.
3. 파일이 있다면 `pages_to_fetch` 값을 읽어서 프로그램에서 사용한다.
4. 1에서 열려고 시도했던 `config.json` 파일이 존재하지 않는 경우
5. 최초 실행시 프로그램에서 사용할 page_to_fetch값을 100으로 설정한다(`config.json`파일에 `page_to_fetch`값을 1로 저장해서 이후부터는 1페이지씩 읽음).
6. `pages_to_fetch`값으로 `update_daily_price()` 메소드를 호출한다.
7. 이번 달의 마지막 날(lastday)을 구해 다음 날 오후 5시를 계산하는 데 사용한다.
8. 다음 날 오후 5시에 execute_daily() 메소드를 실행하는 타이머(Timer) 객체를 생성한다.

###### 5.3.10 MySQL 자동 연결 해제 방지
---
MySQL 설정파일(`my.ini`)에서 `wait_timeout`값을 변경해야 한다. `C:\ProgramData\MySQL\MySQL Server 8.0` 에 있다. 기본으로 28800(8시간)으로 되어있었고, 이 이상 사용하지 않으면 ConnectionAbortedError(10053)가 발생해 자동으로 연결이 종료된다.

나는 위 파일에서 찾지 못했다. `show variables like '%timeout%';` 라고 쳐보니 있는 것을 확인할 수 있었고 따로 변경해줘야 되는 것 같다.

###### 5.3.12 Run 레지스트리 등록해 자동 실행하기
---
윈도우 업데이트 등으로 서버가 재시작하더라도 자동으로 실행되게 하려면 Run 레지스트리에 등록해야 한다. 
1. `DBUpdater.bat` 파일을 생성하여 `python 파일경로\DBUpdater.py` 를 입력한다. 
2. 윈도우키 + R 키를 함꼐 클릭하여 '실행'창을 띄운 뒤 'regedit'를 입력하여 레지스트리 편집기를 실행한다.
3. HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run 키를 마우스로 우클릭
4. 새로 만들기 메뉴 클릭
5. 문자열 값 메뉴를 클릭
6. DBUPDATER 라는 문자열 값으로 `파일경로\DBUpdater.bat` 경로를 지정

##### 5.4 일별 시세 조회 API
---
네이버 금융의 일별 시세를 DB로 복제하는 DBUpdater 클래스를 만들었다. 이제는 야후 파이낸스에서 제공하는 `get_data_yahoo()` 함수처럼, 우리가 구축한 DB에서 일별 시세를 직접 조회하는 API를 제작해보자. 이 API는 다음과 같은 장점이 있다
- 야후 파이낸스와 달리 검증된 국내 데이터를 조회할 수 있다.
- 종목코드를 몰라도 상장기업명으로 조회할 수 있다.
- 조회 일자 형식을 틀리게 입력하더라도 자동으로 조회 일자 양식에 맞추어 변경해준다.

###### 5.4.2 생성자와 소멸자로 DB 연결 관리
---
```python
class MarketDB:
    def __init__(self):
        """생성자: MariaDB 연결 및 종목코드 딕셔너리 생성"""
        self.conn = pymysql.connect(host='localhost', user='root', 
            password='snake.land.', db='INVESTAR', charset='utf8')
        self.codes = {}
        self.get_comp_info()    # 1
        
    def __del__(self):
        """소멸자: MariaDB 연결 해제"""
        self.conn.close()
```
1. `get_comp_info()` 함수를 호출하여 DB에서 `company_info` 테이블을 읽어와서 `codes`에 저장한다.

###### 5.4.3 일별 시세 조회 API
---
가장 중요한 부분이다.
```python
class MarketDB:
    def get_daily_price(self, code, start_date=None, end_date=None):    # 3
        """KRX 종목의 일별 시세를 데이터프레임 형태로 반환
            - code       : KRX 종목코드('005930') 또는 상장기업명('삼성전자')
            - start_date : 조회 시작일('2020-01-01'), 미입력 시 1년 전 오늘
            - end_date   : 조회 종료일('2020-12-31'), 미입력 시 오늘 날짜
        """
        if start_date is None:  # 4
            one_year_ago = datetime.today() - timedelta(days=365)
            start_date = one_year_ago.strftime('%Y-%m-%d')  # 5
            print("start_date is initialized to '{}'".format(start_date))
        else:
            start_lst = re.split('\D+', start_date)     # 6
            if start_lst[0] == '':
                start_lst = start_lst[1:]
            start_year = int(start_lst[0])
            start_month = int(start_lst[1])
            start_day = int(start_lst[2])
            if start_year < 1900 or start_year > 2200:
                print(f"ValueError: start_year({start_year:d}) is wrong.")
                return
            if start_month < 1 or start_month > 12:
                print(f"ValueError: start_month({start_month:d}) is wrong.")
                return
            if start_day < 1 or start_day > 31:
                print(f"ValueError: start_day({start_day:d}) is wrong.")
                return
            start_date=f"{start_year:04d}-{start_month:02d}-{start_day:02d}"    # 7

        if end_date is None:
            end_date = datetime.today().strftime('%Y-%m-%d')
            print("end_date is initialized to '{}'".format(end_date))
        else:
            end_lst = re.split('\D+', end_date)
            if end_lst[0] == '':
                end_lst = end_lst[1:] 
            end_year = int(end_lst[0])
            end_month = int(end_lst[1])
            end_day = int(end_lst[2])
            if end_year < 1800 or end_year > 2200:
                print(f"ValueError: end_year({end_year:d}) is wrong.")
                return
            if end_month < 1 or end_month > 12:
                print(f"ValueError: end_month({end_month:d}) is wrong.")
                return
            if end_day < 1 or end_day > 31:
                print(f"ValueError: end_day({end_day:d}) is wrong.")
                return
            end_date = f"{end_year:04d}-{end_month:02d}-{end_day:02d}"
         
        codes_keys = list(self.codes.keys())    # 8
        codes_values = list(self.codes.values())    # 9

        if code in codes_keys:  # 10
            pass
        elif code in codes_values:  # 11
            idx = codes_values.index(code)  # 12
            code = codes_keys[idx]  # 13
        else:
            print(f"ValueError: Code({code}) doesn't exist.")
        sql = f"SELECT * FROM daily_price WHERE code = '{code}'"\
            f" and date >= '{start_date}' and date <= '{end_date}'"
        df = pd.read_sql(sql, self.conn)    # 1
        df.index = df['date']   # 2
        return df 
```
1. 팬더스의 `read_sql()` 함수를 이용해 `SELECT` 결과를 데이터프레임으로 겨져오면 정수형 인덱스가 별도로 생성된다.
2. 데이터프레임의 인덱스를 새로 설정해준다.

###### 5.4.4 기본 인숫값 처리
---
조회 시작일과 조회 종료일을 인수로 넘겨주지 않았을 때 기본 인숫값으로 처리하는 함수

3. None 을 디폴트 값으로
4. 인수가 입력되지 않은 경우
5. 1년 전 오늘날짜로

###### 5.4.5 정규표현식으로 연-월-일 분리하기
---
사용자가 조회 시작일을 입력할 때 '2020-08-30' 처럼 정확히 입력할 수도 있지만, '2020-8-30', '2020.8.30' 등 다양한 형식으로 입력할 수 있다. 정규표현식을 사용하여 연, 월, 일에 해당하는 세 숫자를 분리하면 어떤 형식으로 입력하더라도 제대로 처리할 수 있다.

6. 정규표현식 `\+D`(숫자가 아닌 것 한번 이상)으로 분리하여 연, 월, 일에 해당하는 숫자만 남게된다.
7. DB에 저장된 날짜 형식과 같게 만든다.

###### 회사명으로 종목코드 조회하기
---
codes 딕셔너리의 키는 종목코드이고 값은 회사명이다. 종목코드로 회사명은 쉽게 조회 가능하지만, 반대로 값인 회사명으로 키를 찾기는 쉽지 않다.

딕셔너리에서 값으로 키를 조회해야 한다면, 애초부터 딕셔너리가 아닌 데이터프레임 같은 다른 자료형을 사용하는 것이 낫다. 굳이 딕셔너리에서 값으로 키를 조회하려면 다음과 같은 방법을 사용하면 된다.

8. 키(종목코드) 리스트
9. 값(회사명) 리스트
10. 사용자가 입력한 값(code)이 종목코드이면 별도 처리없이 사용
11. 값(회사명) 리스트에 존재하면
12. 값 리스트에서 해당 인덱스 구한 뒤
13. 키 리스트에서 동일한 인덱스에 위치한 값을 구한다.