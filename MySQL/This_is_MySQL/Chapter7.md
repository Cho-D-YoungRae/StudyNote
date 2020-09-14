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