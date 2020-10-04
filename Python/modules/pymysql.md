#### pymysql
> 파이썬 mysql 연동

```python
import pymysql
```

*데이터 입력*
1. MySQL 연결
   - 연결자 = pymysql.connect(연결 옵션)
   - conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='hanbitDB', charset='utf8')    
2. 커서 생성
   - 커서 이름 = 연결자.cursor()
3. (테이블 만들기)
   - 커서 이름.execute("CREATE TABLE 문장")
4. 데이터 입력
   - 커서 이름.execute("INSERT 문장")
   - 반복
5. 입력한 데이터 저장
   - 연결자.commit()
6. MySQL 연결 종료
   - 연결자.close()

*데이터 조회*
1. MySQL 연결
   - 연결자 = pymysql.connect(연결 옵션)    
2. 커서 생성
   - 커서 이름 = 연결자.cursor()
3. 데이터 조회
   - 커서 이름.execute("SELECT 문장")
4. 조회한 데이터 출력
   - 커서 이름.fetchon()
   - 반복
5. MySQL 연결 종료
   - 연결자.close()

