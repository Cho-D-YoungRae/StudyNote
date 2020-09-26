#### 4. 웹 스크레이핑을 사용한 데이터 분석
---
##### 4.1 팬더스로 상장법인 목록 읽기
---
종목코드 구하기
- <kind.krx.co.kr>
- 상장법인상세정보
- 상장법인목록
- EXCEL 버튼으로 다운


###### 4.1.1 엑셀 파일 내용 확인하기
---
- 확장자가 .xls이긴 하지만, 실제 내용은 HTML이다.
- 팬더스의 `read_excel()`함수로 읽을 수 없다.
- `read_html()`함수를 이용하여 파일을 읽어야 한다.
- `read_excel()`로 읽으려면 .xlsx 형태로 저장해야한다.

###### 4.1.2 read_html() 함수로 파일 읽기
---

```python
import pandas as pd

# 데이터프레임 객체를 원소로 가지는 리스트를 반환한다.
krx_list = pd.read_html("상장법인목록.xls")

# 앞에 0을 붙여서 출력되도록
krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format)
krx_list[0]

            회사명    종목코드  ...                          홈페이지     지역
0          원방테크  053080  ...        http://wonbangtech.com   충청북도
1           비나텍  126340  ...         http://www.vina.co.kr   전라북도
2     엔에이치스팩17호  359090  ...                           NaN  서울특별시
3         박셀바이오  323990  ...    http://www.vaxcell-bio.com   전라남도
4        티와이홀딩스  363280  ...  http://www.ty-holdings.co.kr  서울특별시
         ...     ...  ...                           ...    ...
2374     CJ대한통운  000120  ...    http://www.cjlogistics.com  서울특별시
2375      메리츠화재  000060  ...     http://www.meritzfire.com  서울특별시
2376         경방  000050  ...    http://www.kyungbang.co.kr  서울특별시
2377      유수홀딩스  000700  ...  http://www.eusu-holdings.com  서울특별시
2378   한진중공업홀딩스  003480  ...  http://www.hhic-holdings.com    경기도
[2379 rows x 9 columns]
```

```python
# url을 이용해 인터넷 상 파일도 읽을 수 있다.
# 뒤에 [0]을 붙여주어 데이터프레임을 받도록
df = pd.read_html("http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13")[0]

# 위 예제코드와 동일한 기능을 한다. 취향에 맞게 사용하면 된다.
df['종목코드'] = df['종목코드'].map('{:06d}'.format)

# ascending=False 를 추가해주면 내림차순으로 정렬된다.
df = df.sort_values(by='종목코드')
df
```

##### 4.3 웹에서 일별 시세 구하기
---
네이버 금융에서 한국거래소에 상장된 종목의 일별 시세를 확인할 수 있다.

https://finance.naver.com/item/main.nhn?code=035720
- 뒤에 code 는 종목 코드이다.
- 다른 종목 종가를 확인하려면 이 종목코드를 바꾸면 된다.


###### 4.3.1 네이버 금융 일별 시세 분석하기
----
<view-source:https://finance.naver.com/item/sise_day.nhn?code=035720&page=514>
- 일별 시세 페이지 페이지 소스 보기
- code = 종목코드
- page = 페이지 숫자

###### 4.3.2 소스 코드에서 링크 주소 검색하기
---
<https://finance.naver.com/item/sise_day.nhn?code=035720&page=1>
- 첫 페이지
- Ctrl + U 를 눌러서 소스코드 확인
- 맨 뒤를 검색 -> 맨 뒤가 몇 페이지인지 확인할 수 있다.

##### 4.4 뷰티풀 수프로 일별 시세 읽어오기
---
HTML, XML 페이지로부터 데이터를 추출하는 파이썬 라이브러리. 웹 크롤러나 웹 스크레이퍼로 불리기도 한다.

###### 4.4.1 파서별 장단점
---
뷰티풀 수프는 HTML 페이지를 분석할 때 네 가지 인기 파서 라이브러리를 골라서 쓸 수 있다.
|파서|문자열|장점|단점|
|---|---|---|---|
|Python's html parser|'html.parser'|기본 옵션으로 설치되어 있다. 속도가 적절하고, 유연한 파싱이 가능하다.|lxml보다 느리고, html5lib 파서만큼 유연하지 못하다.|
|lxml's HTML parser|'lxml'|속도가 매우 빠르고, 유연한 파싱이 가능하다.||
|lxml's XML parser|'lxml-xml', 'xml'|속도가 매우 빠르고, 유연한 파싱이 가능하다.|XML 파일에만 사용할 수 있다.|
|html5lib|'html5lib'|웹 브라우저와 동일한 방식으로 파싱한다. 극도록 유연하여 복잡한 구조의 HTML 문서를 파싱하는데 사용한다.|매우 느리다.|

###### 4.4.2 find_all() 함수와 find() 함수 비교
---
뷰티풀 수프의 원하는 태그를 찾아주는 함수
- `find_all(['검색할 태그'][, 'class_=클래스 속성값'][, id='아이디 속성값'][, limit=찾을 개수])`
  - 아무것도 찾지 못하면 빈 리스트 반환
- `find(['검색할 태그'][, 'class_=클래스 속성값'][, id='아이디 속성값'])`
  - 아무것도 찾지 못하면 None 반환

###### 4.4.3 맨 뒤 페이지 숫자 구하기
---
```python
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://finance.naver.com/item/sise_day.nhn?code=035720&page=1'
with urlopen(url) as doc:
...     html = BeautifulSoup(doc, 'lxml')       # 1
...     pgrr = html.find('td', class_='pgRR')   # 2
...     print(pgrr.a['href'])                   # 3
...     
/item/sise_day.nhn?code=035720&page=513
```
1. 첫 번째 인수로 HTML/XML 페이지의 파일 결로나 URL. 두 번째 인수로 웹 페이지를 파싱할 방식.
2. 결과 값은 'bs4.element.Tag' 타입으로 반환된다. 'pgrr'은 Page Right Right 으로 맨 오른쪽 마지막 이라는 뜻
3. \<td\> 태그 하부에 있는 \<a\> xormdml href 속성값

```python
# 전체 텍스트를 확인하려면 getText 속성을 이용하면 된다.
# prettify() 함수를 호출하면 getText 속성값을 계층적으로 보기좋게 출력
print(pgrr.prettify())

# 태그를 제외한 택스트 부분만 구할 때
print(pgrr.text)

# 전체 페이지 수를 구하기
s = str(pgrr.a['href']).split('=')
last_page = s[-1]
```

###### 4.4.4 전체 페이지 읽어오기
---
```python
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

if __name__ == '__main__':
    url = 'https://finance.naver.com/item/sise_day.nhn?code=035720&page=1'
    with urlopen(url) as doc:
        html = BeautifulSoup(doc, 'lxml')
        pgrr = html.find('td', class_='pgRR')
        last_page = str(pgrr.a['href']).split('=')[-1]

    df = pd.DataFrame()
    sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=035720'

    for page in range(1, int(last_page)+1):
        page_url = '{}&page{}'.format(sise_url, page)
        df = df.append(pd.read_html(page_url, header=0)[0])

    df = df.dropna()    # 값이 빠진 행 제거

    print(df)
```

##### 4.5 OHLC와 캔들 차트
---
OHLC 는 Open-High-Low-Close 를 나타내며 시가-고가-저가-종가를 의미한다.

*캔들차트*
- 시가보다 종가가 높으면, 붉은 양봉으로 표시
- 시가보다 종가가 낮으면, 푸른 음봉으로 표시
- 고가와 저가를 실선으로 연결

###### 4.5.2 종가 차트
---
> 나는 카카오를 이용함

```python
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
    url = 'https://finance.naver.com/item/sise_day.nhn?code=035720&page=1'
    with urlopen(url) as doc:
        html = BeautifulSoup(doc, 'lxml')
        pgrr = html.find('td', class_='pgRR')
        last_page = str(pgrr.a['href']).split('=')[-1]

    df = pd.DataFrame()
    sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=035720'

    for page in range(1, int(last_page)+1):
        page_url = '{}&page={}'.format(sise_url, page)
        df = df.append(pd.read_html(page_url, header=0)[0])

    df = df.dropna()
    df = df.iloc[0:30]                      # 1
    df = df.sort_values(by='날짜')          # 2

    plt.title('Kakao (close)')
    plt.xticks(rotation=45)                 # 3
    plt.plot(df['날짜'], df['종가'], 'co-') # 4
    plt.grid(color='gray', linestyle='--')
    plt.show()
```
1. 최근 30행만 사용한다.
2. 네이버 금융의 데이터가 내림차순으로 되어 있어서 오름차순으로 변경한다.
3. x축 레이블의 날짜가 겹쳐서 보기 어려우므로 90도 회전하여 표시한다.
4. x축은 날짜 데이터로 y축은 종가 데이터로 출력한다. 'co-' 는 좌표를 청록색(Cyan) 원으로 표시하고 실선(-)으로 연결해서 표시하라는 의미이다.

###### 4.5.3 캔들차트
---
**신버전으로 캔들 차트 그리기**
```python
# 한글 칼럼명을 영문 칼럼명으로 변경한다.
df = df.rename(columns={'날짜':'Date', '시가':'Open', '고가':'High', '저가':'Low', '종가':'Close', '거래량':'Volume'})
df = df.sort_values(by='Date')
# Date 칼럼을 DatetimeIndex형으로 변경한 후 인덱스로 설명
df.index = pd.to_datetime(df.Date)
# Open, High, Low, Close, Volume 칼럼만 갖도록 데이터 프레임 구조 변경
df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

# 캔들 차트 그리기
# type 을 'ohlc'로 변경하면 OHLC 차트가 출력(default)
mpf.plot(df, title='Kakao candle chart', type='candle')
```
```python
 kwargs = dict(title='Kakao customized chart', type='candle',\
                mav=(2, 4, 6), volume=True, ylabel='ohlc candles')  # 1
mc = mpf.make_marketcolors(up='r', down='b', inherit=True)          # 2
s = mpf.make_mpf_style(marketcolors=mc)                             # 3

mpf.plot(df, **kwargs, style=s)                                     # 4
```
1. kwargs는 keyword arguments의 약자이며, mpf.plot() 함수를 호출할 때 쓰이는 여러 인수를 담는 딕셔너리다.
2. 마켓 색상은 스타일을 정하는 필수 객체.
   - 상승은 빨간색(red)
   - 하락은 파란색(blue)
   - 관련 색상은 이를 따르도록
3. 스타일 객체 생성
4. 차트 출력