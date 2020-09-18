#### Chapter 7. SQL 고급
---
##### 7.1 MySQL의 데이터 형식
---
###### 7.1.1 MySQL에서 지원하는 데이터 형식의 종류
---

**숫자 데이터 형식**

|데이터 형식|바이트 수|설명|
|---|---|---|
|BIT(N)|N/8|1~62bit를 표현. b'0000'형식으로 표현|
|TINYINT|1|정수|
|\*SMALLINT|2|정수|
|MEDIUMINT|3|정수|
|\*INT<br>INTEGER|4|정수|
|\*BIGINT|8|정수|
|\*FLOAT|4|소수점 아래 7자리까지 표현|
|DOUBLE<br>REAL|8|소수점 아래 15자리까지 표현|
|\*DECIMAL(m, [d])<br>NUMERIC(m, [d])|5~17|전체 자릿수(m)와 소수점 이하 자릿수(d)를 가진 숫자형|

- `DECIMAL` 은 정확한 수치를 저장하게 되고 `FLOAT`, `DOUBLE`은 근사치의 숫자를 저장한다. 대신 `FLOAT`, `DOUBLE`은 상당히 큰 숫자를 저장할 수 있다는 장점이 있다.
  - 소수점이 들어간 실수를 저장하려면 되도록 `DECIMAL`
- `UNSIGNED` 예약어를 뒤에 붙여줌으로써 부호없는 수를 저장할 수 있다.


**문자 데이터 형식**

|데이터 형식|바이트수|설명|
|---|---|---|
|\*CHAR(n)|1~255|고정길이 문자형. n을 1부터 255까지 지정. CHAR만 쓰면 CHAR(1).|
|\*VARCHAR(n)|1~65535|가변길이 문자형. n을 사용하면 1~65535까지 지정.|
|BINARY(n)|1~255|고정길이의 이진 데이터 값|
|VARBINARY(n)|1~255|가변길이의 이진 데이터 값|
|TINYTEXT|1~255|255 크기의 TEXT 데이터 값|
|TEXT|1~65535|N 크기의 TEXT 데이터 값|
|MEDIUMTEXT|1~16777215|16777215 크기의 TEXT 데이터 값|
|\*LONGTEXT|1~4294967295|최대 4GB 크기의 TEXT 데이터 값|
|TINYBLOB|1~255|255 크기의 BLOB 데이터 값|
|BLOB|1~65535|N 크기의 BLOB 데이터 값|
|MEDIUMBLOB|1~16777215|16777215 크기의 BLOB 데이터 값|
|\*LONGBLOB|1~4294967295|최대 4GB 크기의 BLOB 데이터 값|
|ENUM(값들...)|1 또는 2|최대 65535개의 열거형 데이터 값|
|SET(값들...)|1,2,3,4,8|최대 64개의 서로 다른 데이터 값|

> MySQL 은 기본적으로 CHAR, VARCHAR 모두 UTF-8 형태를 지니므로 영문, 한글 등에 따라 크기가 달라진다. 하지만 사용자 입장에서는 CHAR(100)은 영문, 한글 구분 없이 100글자를 입력하는 것으로 알고 있으면 된다.


**날짜와 시간 데이터 형식**

|데이터 형식|바이트수|설명|
|---|---|---|
|\*DATE|3|'YYYY-MM-DD'형식으로 사용됨. 1001-01-01 ~ 9999-12-31|
|TIME|3|'HH:MM:SS'형식으로 사용됨. -839:59:59.000000 ~ 839:59:59.000000|
|\*DATETIME|8|'YYYY-MM-DD HH:MM:SS'형식으로 사용됨. 1001-01-01 00:00:00 ~ 9999-12-31 23:59:59|
|TIMESTAMP|4|'YYYY-MM-DD HH:MM:SS'형식으로 사용됨. 1001-01-01 00:00:00 ~ 9999-12-31 23:59:59. time_zone 시스템 변수와 관련이 있으며 UTC 시간대 변환하여 저장|
|YEAR|1|'YYYY'형식. 1901 ~ 2155|

**기타 데이터 형식**

|데이터 형식|바이트 수|설명|
|---|---|---|
|\*GEOMETRY|N/A|공간 데이터 형식으로 선, 점 및 다각형 같은 공간 데이터 개체를 저장하고 조작|
|\*JSON|8|JSON(JavaScript Object Notation)문서를 저장|

###### 7.1.2 변수의 사용
SQL도 변수를 선언하고 사용할 수 있다
```SQL
SET @변수이름 = 변수의 값;  -- 변수의 선언 및 값 대입
SELECT @변수이름 ;         -- 변수의 값 출력
```

> 스토어드 프로시저나 함수 안에서의 변수 사용은 DECLARE문으로 선언하여 @ 없이 변수명만으로 사용한다. @변수명은 '전역 변수'처럼 사용하고 DECLARE 변수명은 '지역 변수' 처럼 사용된다.

**실습1**

```sql
USE sqldb;

SET @myVar1 = 5;
SET @myVar2 = 3;
SET @myVar3 = 4.25;
SET @myVar4 = '가수 이름==>';

SELECT @myVar1;
SELECT @myVar2 + @myVar3;

SELECT @myVar4, name FROM usertbl WHERE height > 180;
```

LIMIT에는 원칙적으로 변수를 사용할 수 없으나 다음과 같이 활용할 수 있다.
```SQL
SET @myVar1 = 3;
PREPARE myQuery
	FROM 'SELECT name, height FROM usertbl ORDER BY height LIMIT ?';
EXECUTE myQuery USING @myVar1;
```
`PREPARE 쿼리이름 FROM '쿼리문'`은 쿼리이름에 '쿼리문'을 준비만 해놓고 실행하지는 않는다. 그리고 `EXECUTE` 를 만나는 순간 실행되며, `USING @변수`를 이용해서 '쿼리문'에서 ?으로 처리해 놓은 부분에 대입된다.


###### 7.1.3 데이터 형식과 형 변환
---
**데이터 형식 변환 함수**

```SQL
CAST ( expression AS 데이터형식[(길이)])
CONVERT ( expression, 데이터형식[(길이)])
```

**암시적인 형 변환**

```SQL
SELECT '100' + '200' ; -- 문자와 문자를 더함 -> 정수로 변환되어 연산됨
SELECT CONCAT('100', '200') ; -- 문자와 문자를 연결 -> 문자로 처리
SELECT CONCAT(100, '200') ; -- 정수와 문자를 연결 -> 문자로 처리
SELECT 1 > '2MEGA'; -- 정수인 2로 변환되어서 비교
SELECT 0 = 'MEGA2'; -- 문자는 0으로 변환
```
DBMS 에 따라 다를 수 있다.


###### 7.1.4 MySQL 내장함수
---

**제어 흐름 함수**

- `IF(수식, 참, 거짓)`
- `IFNULL(수식1, 수식2)`
  - 수식1이 NULL이 아니면 수식1이 반환, NULL이면 수식2가 반환
- `NULLIF(수식1, 수식2)`
  - 수식1과 수식2가 같으면 NULL, 다르면 수식1 반환
- `CASE ~ WHEN ~ ELSE ~ END`
  - ```SQL
    SELECT CASE 10
                WHEN 1  THEN  '일'
                WHEN 5  THEN  '오'
                WHEN 10 THEN  '십'  -- CASE 뒤 10 이므로 '십' 반환
                ELSE '모름'
          END AS 'CASE 연습'  -- 출력될 열의 별칭
    ```


**문자열 함수**

- `ASCII(아스키코드)`, `CHAR(숫자)`
- `BIT_LENGTH(문자열)`, `CHAR_LENGTH(문자열)`, `LENGTH(문자열)`
- `CONCAT(문자열1, 문자열2, ...)`, `CONCAT_WS(구분자, 문자열1, 문자열2, ...)`
- `ELT(위치, 문자열1, 문자열2, ...)`, `FIELD(찾을 문자열, 문자열1, 문자열2)`, `FIND_IN_SET(찾을 문자열, 문자열 리스트)`, `INSTR(기준 문자열, 부분 문자열)`, `LOCATE(부분 문자열, 기준 문자열)`
  - `FIND_IN_SET`에 주어지는 문자열 리스트는 콤마(,)로 구분되어 있어야 하며 공백이 없어야 한다. 
  - `LOCATE`, `INSTR`은 동일하지만 파라미터의 순서가 반대로 되어 있다.
  - `LOCATE`, `POSITION`은 동일한 함수
- `FORMAT(숫자, 소수점 자릿수)`
- `BIN(숫자)`, `HEX(숫자)`, `OCT(숫자)`
- `INSERT(기준 문자열, 위치, 길이, 삽입할 문자열)`
  - 기준 문자열의 위치부터 길이만큼을 지우고 삽입할 문자열을 끼워 넣는다.
- `LEFT(문자열, 길이)`, `RIGHT(문자열, 길이)`
  - 왼쪽 또는 오른쪽에서 문자열의 길이만큼 반환
- `UPPER(문자열)`, `LOWER(문자열)`
  - `LOWER`, `LCASE` 는 동일. `UPPER`, `UCASE`는 동일
- `LPAD(문자열, 길이, 채울 문자열)`, `RPAD(문자열, 길이, 채울 문자열)`
  - 문자열을 길이만큼 늘린 후, 빈 곳을 채울 문자열로 채운다.
- `LTRIM(문자열)`, `RTRIM(문자열)`
  - 문자열의 왼쪽/오른쪽 공백을 제거
- `TRIM(문자열)`, `TRIM(방향 자를_문자열 FROM 문자열)`
  - `TRIM`은 앞뒤 공백을 모두 없앤다
  - 방향 : `LEADING`(앞), `BOTH`(양쪽), `TRAILING`(뒤)
- `REPEAT(문자열, 횟수)`
- `REPLACE(문자열, 원래 문자열, 바꿀 문자열)`
- `REVERSE(문자열)`
- `SPACE(길이)`
  - 길이만큼의 공백 반환
- `SUBSTRING(문자열, 시작위치, 길이)`, `SUBSTRING(문자열 FROM 시작위치 FOR 길이)`
  - `SUBSTRING`, `SUBSTR`, `MID` 동일
- `SUBSTRING_INDEX(문자열, 구분자, 횟수)`
  - 구분자를 기준으로 횟수 번째 나오면 나머지 버림
  - 횟수가 음수이면 오른쪽부터 세고 왼쪽 버림


**수학 함수**

- `ABS(숫자)`
- `ACOS(숫자)`, `ASIN(숫자)`, `ATIN(숫자)`, `ATIN2(숫자1, 숫자2)`, `SIN(숫자)`, `COS(숫자)`, `TAN(숫자)`
- `CEILING(숫자)`, `FLOOR(숫자)`, `ROUND(숫자)`
  - 올림, 내림, 반올림
- `CONV(숫자, 원래 진수, 변환할 진수)`
- `DEGREES(숫자)`, `RADIANS(숫자)`, `PI()`
- `EXP(X)`, `LN(숫자)`, `LOG(숫자)`, `LOG(밑수, 숫자)`, `LOG2(숫자)`, `LOG10(숫자)`
- `MOD(숫자1, 숫자2)`, `숫자1 % 숫자2`, `숫자1 MOD 숫자2`
- `POW(숫자1, 숫자2)`, `SQRT(숫자)`
- `RAND()`
  - 0 이상 1미만의 실수
  - `FLOOR (m + (RAND() * (n-m)))`: m이상 n 미만의 정수
- `SIGN(숫자)`
  - 양수: 1, 0: 0, 음수: -1
- `TRUNCATE(숫자, 정수)`
  - 숫자를 소수점을 기준으로 정수 위치까지 구하고 나머지는 버린다.


**날짜 및 시간 함수**

- `ADDDATE(날짜, 차이)`, `SUBDATE(날짜, 차이)`
  - ```SQL
    SELECT ADDDATE('2020-01-01', INTERVAL 31 DAY);
    SELECT SUBDATE('2020-01-01', INTERVAL 31 MONTH);
    ```
- `ADDTIME(날짜/시간, 시간)`, `SUBTIME(날짜/시간, 시간)`
  - ```SQL
    SELECT ADDTIME('2020-0101 23:59:59', '1:1:1');
    SELECT SUBTIME('2020-0101 23:59:59', '1:1:1');
    ```
- `CURDATE()`, `CURTIME()`, `NOW()`, `SYSDATE()`
  - 연-월-일, 시:분:초, 연-월-일 시:분:초
  - `CURDATE()`, `CURRENT_DATE()`, `CURRENT_DATE` 동일, `CURTIME()`, `CURRENT_TIME()`, `CURRENT_TIME` 동일, `NOW()`, `LOCALTIME`, `LOCALTIME()`, `LOCALTIMESTAMP`, `LOCALTIMESTAMP()` 동일
- `YEAR(날짜)`, `MONTH(날짜)`, `DAY(날짜)`, `HOUR(시간)`, `MINUTE(시간)`, `SECOND(시간)`, `MICROSECOND(시간)`
  - `DATOFMONTH()`, `DAY()` 동일
- `DATE()`, `TIME()`
- `DATEDIFF(날짜1, 날짜2)`, `TIMEDIFF(날짜1 또는 시간1, 날짜2 또는 시간2)`
- `DAYOFWEEK(날짜)`, `MONTHNAME()`, `DAYOFYEAR(날짜)`
  - 1~7 : 일~토
- `LAST_DAY(날짜)`
  - 주어진 날짜의 마지막 날짜. 그 달이 몇 일까지 있는지
- `MAKEDATE(연도, 정수)`
  - 연도에서 정수만큼 지난 날짜
- `MAKETIME(시, 분, 초)`
  - '시:분:초'
- `PERIOD_ADD(연월, 개월수)`, `PERIOD_DIFF(연월1, 연월2)`
  - ```SQL
    SELECT PERIOD_ADD(2020, 11), PERIOD_DIFF(202001, 202012);
    ```
  - 개월 수 차이만큼
- `QUARTER(날짜)`
  - 4분기 중 몇 분기인지
- `TIME_TO_SEC(시간)`
  - 시간을 초 단위로 구한다.


**시스템 정보 함수**

- `USER()`, `DATEBASE()`
- `FOUND_ROWS()`
  - 바로 앞의 `SELECT`문에서 조회된 행의 개수
- `ROW_COUNT()`
  - 바로 앞의 `INSERT`, `UPDATE`, `DELETE`문의 행 개수
  - `CREATE`, `DROP`문은 0
  - `SELECT`문은 -1
- `VERSION()`
- `SLEEP(초)`
  - 쿼리의 실행을 잠깐 멈춘다.

**실습2**

- `LOAD_FILE(경로)`
- `SHOW variables LIKE 'max_allowed_packet';` : 최대 패킷 크기(최대 파일 크기)
  - 'C:\ProgramData\MySQL\MySQL Server 8.0\my.ini' 에서 변경가능
- `SHOW variables LIKE 'secure_file_priv';` : 업로드/다운로드할 폴더 경로
  - 'C:\ProgramData\MySQL\MySQL Server 8.0\my.ini' 에서 변경가능
  - my.ini 파일 내에서는 'secure-file-priv'
  - 보안을 강화하기 위해서 지정한 폴더 외에는 파일의 읽기/쓰기를 금지하는 옵션
  - 여러 개가 써 있어도 상관은 없지만, 제일 마지막의 것만 적용
  - 명령프롬프트에서 `NET STOP MySQL` -> `NET START MySQL` 로 서버 재시작해야 적용된다.
    - 서버 재시작에 실패했다면 글자가 틀렸거나, 추가한 폴더가 없기 때문
- 추가한 파일 다운 가능
  - ```SQL
    SELECT movie_script FROM movietbl WHERE movie_id=1
      INTO OUTFILE '경로/파일이름'
      LINES TERMINATED BY '//n'; -- 줄 바꿈 문자도 그대로 저장하기 위한 옵션
    
    SELECT movie_film FROM movietbl WHERE movie_id=3
      INTO DUMPFILE '경로/파일이름';
    ```

**피벗의 구현**

피벗은 한 열에 포함된 여러 값을 출력하고, 이를 여러 열로 변환하여 테이블 반환식을 회전하고 필요하면 집계까지 수행하는 것

**실습3**

```sql
SELECT uName,
	SUM(IF(season='봄', amount, 0)) AS '봄',
    SUM(IF(season='여름', amount, 0)) AS '여름',
    SUM(IF(season='가을', amount, 0)) AS '가을',
    SUM(IF(season='겨울', amount, 0)) AS '겨울',
    SUM(amount) AS '합계' FROM pivottest GROUP BY uName;
```

**JSON 데이터**

속성(Key)과 값(Value) 쌍을 이루며 구성되어 있다.
```SQL
USE sqldb;
SELECT JSON_OBJECT('name', name, 'height', height) AS 'JSON값'
    FROM usertbl
    WHERE height >= 180;
```
- `JSON_OBJECT()`, `JSON_ARRAY()`로 JSON`으로 변환

```SQL
SET @json='{ "usertbl" : 
  [
      {"name":"임재범","height":182},
      {"name":"이승기","height":182},
      {"name":"성시경","height":186}
  ]
}' ;
-- 문자열이 JSON 형식을 만족하는지
SELECT JSON_VALID(@json);
-- 세번째 파라미터로 주어진 문자열의 위치 반환
-- 두번쨰 파라미터 'one': 처음하나, 'all' : 매치되는 모든 것
SELECT JSON_SEARCH(@json, 'one', '성시경');
-- 지정된 위치의 값 추출
SELECT JSON_EXTRACT(@json, '$.usertbl[2].name');
-- 새로운 값 추가
SELECT JSON_INSERT(@json, '$.usertbl[0].mDate', '2020-09-09');
-- 값 변경
SELECT JSON_REPLACE(@json, '$.usertbl[0].name', '홍길동');
-- 지정된 항목 삭제
SELECT JSON_REMOVE(@json, '$.usertbl[0]');


##### 7.2 조인