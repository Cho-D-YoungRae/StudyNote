#### Chapter 6. SQL 기본
---
##### 6.1 SELECT문
---
###### 6.1.1 원하는 데이터를 가져와 주는 기본적인 <SELECT...FROM>
---
**SELECT의 구문 형식**

실제적으로 많이 사용되는 형태로 요약한 구조이다. [] 안의 내용은 생략할 수 있다.
```SQL
SELECT select_expr
    [FROM table_reference]
    [WHERE where_condition]
    [GROUP BY {col_name | expr | position}]
    [HAVING where_condition]
    [ORDER BY {col_name | expr | position}]
```

그 중에서도 가장 자주 쓰이는 것은 아래와 같다
```SQL
SELECT 열 이름
FROM 테이블 이름
WHERE 조건
```

**USE 구문**

```SQL
USE 데이터베이스_이름;
```
사용할 데이터베이스를 지정한다. 지정해 놓은 후에는 특별히 다른 DB를 사용하겠다고 명시하지 않는 이상 모든 SQL문은 지정된 DB에서 수행된다. Workbench에서 사용하려는 DB를 더블클릭하는 것과 같다.

**SELECT와 FROM**

```SQL
SELECT 열 이름(*은 모든열. 여러 개의 열 올 수 있다.)
FROM DB이름.테이블이름 (DB이름 생략해도 사용하던 DB이름이 자동으로 붙는다.)
```

**실습1**

- `SHOW DATABASES;` : 현재 서버에 어떤 데이터베이스가 있는지 조회한다.
- `SHOW TABLE STATUS;` : 현재 데이터베이스에 있는 테이블의 정보를 조회한다.
- `DESCRIBE 테이블;` or `DESC 테이블` : 테이블의 열이 무엇이 있는지 확인한다.

```SQL
SELECT first_name AS 이름, gender 성별, hire_date '회사 입사일'
FROM employees;
```
> `AS` 를 사용해서 열 이름을 별도의 별칭으로 지정할 수 있다. `AS`는 생략 가능하다. 공백이 있는 별칭은 ''로 감싸준다. 별칭을 붙일경우 ''안에 별칭을 사용하기를 권장한다.

**실습2**


```SQL
DROP DATABASE IF EXISTS sqldb;
CREATE DATABASE sqldb;

USE sqldb;
CREATE TABLE usertbl
(	userID		CHAR(8) NOT NULL PRIMARY KEY,
	name		VARCHAR(10) NOT NULL,
    birthYear	INT NOT NULL,
    addr		CHAR(2) NOT NULL,
    mobile1		CHAR(3),
    mobile2		CHAR(8),
    height		SMALLINT,
    mDate		DATE
);
CREATE TABLE buytbl
(	num			INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	userID		CHAR(8) NOT NULL,
    prodName	CHAR(6) NOT NULL,
    groupName	CHAR(4),
    price		INT NOT NULL,
    amount		SMALLINT NOT NULL,
    FOREIGN KEY (userID) REFERENCES usertbl(userID)
);

insert into usertbl values('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
insert into usertbl values('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
insert into usertbl values('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');
insert into usertbl values('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');
insert into usertbl values('SSK', '성시경', 1979, '서울', NULL, NULL, 186, '2013-12-12');
insert into usertbl values('LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9');
insert into usertbl values('YJS', '윤종신', 1969, '경남', NULL, NULL, 170, '2005-5-5');
insert into usertbl values('EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3');
insert into usertbl values('JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010-10-10');
insert into usertbl values('BBK', '바비킴', 1973, '서울', '019', '0000000', 176, '2013-5-5');

insert into buytbl values(NULL, 'KBS', '운동화', NULL, 30, 2);
insert into buytbl values(NULL, 'KBS', '노트북', '전자', 1000, 1);
insert into buytbl values(NULL, 'JYP', '모니터', '전자', 200, 1);
insert into buytbl values(NULL, 'BBK', '모니터', '전자', 200, 5);
insert into buytbl values(NULL, 'KBS', '청바지', '의류', 50, 3);
insert into buytbl values(NULL, 'BBK', '메모리', '전자', 80, 10);
insert into buytbl values(NULL, 'SSK', '책', '서적', 15, 5);
insert into buytbl values(NULL, 'EJW', '책', '서적', 15, 2);
insert into buytbl values(NULL, 'EJW', '청바지', '의류', 50, 1);
insert into buytbl values(NULL, 'BBK', '운동화', NULL, 30, 2);
insert into buytbl values(NULL, 'EJW', '책', '서적', 15, 1);
insert into buytbl values(NULL, 'BBK', '운동화', NULL, 30, 2);
```

> 일부 DBMS에서는 CHAR, VARCHAR 은 영문자를 기준으로 1Byte를 할당하고, NCHAR, NVARCHAR 은 유니코드를 기준으로 2Byte를 할당한다. MySQL 8.0은 CHAR, VARCHAR 모두 UTF-8 코드를 사용한다.

###### 6.1.2 특정한 조건의 데이터만 조회하는 <SELET...FROM...WHERE>
**기본적인 WHERE절**

```sql
SELECT 필드이름 FROM 테이블이름 WHERE 조건식;
```

**관계 연산자의 사용**

```sql
SELECT userID, name FROM usertbl WHERE birthYear >= 1970 AND height >= 182;
SELECT userID, name FROM usertbl WHERE birthYear >= 1970 OR height >= 182;
```

**BETWEEN...AND와 IN() 그리고 LIKE**
```sql
-- BETWEEN...AND
SELECT name, height FROM usertbl WHERE height >= 180 AND height <= 183;
SELECT name, height FROM usertbl WHERE height BETWEEN 180 AND 183;

-- IN()
SELECT name, height FROM usertbl WHERE addr='경남' OR addr='전남' OR addr='경북';
SELECT name, height FROM usertbl WHERE addr IN ('경남', '전남', '경북');

-- LIKE
-- %: 무엇이든 허용
SELECT name, height FROM usertbl WHERE name LIKE '김%';
-- _: 무엇이든 한 글자와 매치
SELECT name, height FROM usertbl WHERE name LIKE '_종신';
```

> %나 _가 문자열의 제일 앞에 들어가는 것은 성능에 나쁜 영향을 끼칠 수 있다. 인덱스가 있더라도 인덱스를 사용하지 않고 전체 데이터를 검색하게 되기 때문이다.


**ANY/ALL/SOME 그리고 서브쿼리(SubQuery, 하위쿼리)**

서브쿼리란 쿼리문 안의 쿼리문이다.
```sql
SELECT name, height FROM usertbl
    where height > (SELECT height FROM usertbl WHERE name = '김경호');
```
김경호의 키는 177이므로 height > 177과 같다

```sql
SELECT name, height FROM usertbl
    where height >= (SELECT height FROM usertbl WHERE addr = '경남');
```
addr = '경남' 사람들의 키는 173, 170 둘이어서 오류가 뜬다. 둘 이상의 값을 반환할 때는 ANY/ALL/SOME 을 붙여줘야 한다.

```SQL
SELECT name, height FROM usertbl
    where height >= ANY(SELECT height FROM usertbl WHERE addr = '경남');
```
173이상인 사람과 170이상인 사람. 즉, 173이상인 사람이 모두 출력된다.

```SQL
SELECT name, height FROM usertbl
    where height >= ALL(SELECT height FROM usertbl WHERE addr = '경남');
```

173이상이고 170이상인 사람. 즉, 170이상인 사람 모두 출력된다.

*즉, ANY는 서브 쿼리의 여러 개의 결과 중 한 가지만 만족해도 되며, ALL은 서브쿼리의 여러 개의 결과를 모두 만족시켜야 한다.*

SOME은 ANY와 동일하다.

```sql
-- '=ANY(서브쿼리)' 와 'IN(서브쿼리)'는 동일하다.
SELECT name, height FROM usertbl
    where height = ALL(SELECT height FROM usertbl WHERE addr = '경남');

SELECT name, height FROM usertbl
    where height IN (SELECT height FROM usertbl WHERE addr = '경남');
```

**원하는 순서대로 정렬하여 출력: ORDER BY**
> 결과물에 대해 영향은 미치지 않지만, 결과가 출력되는 순서를 조절


```sql
SELECT * FROM usertbl ORDER BY mDate;
```
기본적으로 오름차순

```sql
SELECT * FROM usertbl ORDER BY height DESC, name ASC;
```
여러 개로 정렬할 수 있다. `DESC`는 내림차순을 위한 키워드다.  `ASC`는 오름차순을 위한 키워드이고 디폴트 값이므로 생략해도된다.


**중복된 것은 하나만 남기는 DISTINCT**

```SQL
SELECT DISTINCT addr FROM usertbl;
```

**출력하는 개수를 제한하는 LIMIT**

```SQL
USE employees;
SELECT emp_no, hire_date FROM employees
    ORDER BY hire_date ASC
    LIMIT 5;
```
5개만 출력한다.


```SQL
USE employees;
SELECT emp_no, hire_date FROM employees
    ORDER BY hire_date ASC
    LIMIT 0, 5; -- LIMIT 5 OFFSET 0 과 동일 (LIMIT 시작, 개수)
```

**테이블을 복사하는 CREATE TABLE...SELECT**

```SQL
CREATE TABLE 새로운테이블 (SELECT 복사할열 FROM 기존테이블)
```
Primary Key 및 Foreign Key는 복사되지 않는다.

###### GROUP BY 및 BAVING 그리고 집계함수
---
**GROUP BY절**
> 데이터를 그룹화


```sql
SELECT userID AS '사용자 아이디', SUM(amount) AS '총 구매 개수'
	FROM buytbl GROUP BY userID;
```
- userID -> 사용자 아이디, SUM(amount) -> 총 구매 개수 로 표기된다.
- 아이디로 그룹을 지어 해당 아이디가 구매한 총량을 보여준다.
- SUM() 은 집계함수

**집계 함수**

|함수명|설명|
|---|---|
|`AVG()`|평균을 구한다.|
|`MIN()`|최소값을 구한다.|
|`MAX()`|최대값을 구한다.|
|`COUNT()`|행의 개수를 센다.|
|`COUNT(DISTINCT)`|행의 개수를 센다.(중복X)|
|`STDEV()`|표준편차를 구한다.|
|`VAR_SAMP()`|분산을 구한다.|

**Having 절**

총 구매액이 1000이상인 사용자를 찾아보자
```sql
SELECT userID AS '사용자', SUM(price*amount) AS '총구매액'
    FROM buytbl
    WHERE SUM(price*amount) > 1000
    GROUP BY userID;
```
WHERE절에 집계함수가 올 수 없으므로 오류가 나타난다. 이럴 때 사용되는 것이 Having절이다. Having절은 집계함수에 대해서 조건을 제한하는 것이라고 생각하면되며, GROUP BY절 다음에 나와야 한다.
```sql
select userID as '사용자', sum(amount*price) as '총구매액'
	from buytbl
    group by userID
    having sum(amount*price) > 1000;
```

**ROLLUP**
> 총합 또는 중간합계가 필요하다면 GROUP BY절과 함께 WITH ROLLUP문을 사용하면 된다.

```sql
SELECT num, groupName, SUM(price*amount) AS '비용'
	FROM buytbl
    GROUP BY groupName, num
    WITH ROLLUP;
```
그룹 별로 중간 합계를 표시해준다. num은 Primary Key 이며 모든 항복이 보이게 하기 위해서 넣어준 것이다. 그룹 별 합계만 보려면 아래와 같이 sql문을 구성하면 된다.

```sql
SELECT groupName, SUM(price*amount) AS '비용'
	FROM buytbl
    GROUP BY groupName
    WITH ROLLUP;
```

##### 6.2 데이터의 변경을 위한 SQL문
---
###### 6.2.1 데이터의 삽입 : INSERT
---
**INSERT문 기본**

기본 형식
```sql
INSERT [INTO] 테이블[(열1, 열2, ...)] VALUES (값1, 값2, ...)
```
테이블 이름에 다음에 나오는 열은 생략 가능하다. 하지만, 생략할 경우 VALUES 다음에 나오는 값들의 순서 및 개수가 테이블에 정의된 열 순서 및 개수와 동일해야 한다.
```sql
USE sqldb;
CREATE TABLE testtbl1 (id INT, username CHAR(3), age INT);
INSERT INTO testtbl1 VALUES (1, '홍길동', 25);
```
만약, 위 예에서 ID와 이름만 입력하고 나이를 입력하고 싶지 않다면 다으모가 같이 테이블 이름뒤에 입력할 열의 목록을 나열해줘야 한다. 이 경우 생략된 값에는 NULL 값이 들어간다.
```SQL
INSERT INTO testtbl1(id, userName) VALUES (2, '설현');
```

열의 순서를 바꿔서 입력하고 싶을 때는 꼭 열 이름을 입력할 순서에 맞춰 나열해 줘야 한다.
```sql
INSERT INTO testtbl1(userName, age, id) VALUES ('하니', 26, 3);
```

**자동으로 증가하는 AUTO_INCREMENT**

테이블의 속성이 AUTO_INCREMENT로 되어있다면, INSERT에서는 해당열이 없다고 생각하고 입력하면 된다. AUTO_INCREMENT는 자동으로 1부터 증가하는 값을 입력해주며 이를 지정할 때는 꼭 PRIMARY KEY 또는 UNIQUE로 지정해주고 데이터 형은 숫자 형식만 사용할 수 있다.
```SQL
USE sqldb;
CREATE TABLE testtbl2
	(id INT AUTO_INCREMENT PRIMARY KEY,
    userName CHAR(3),
    age INT);
INSERT INTO testtbl2 VALUES (NULL, '지민', 25);
INSERT INTO testtbl2 VALUES (NULL, '유나', 22);
INSERT INTO testtbl2 VALUES (NULL, '유경', 21);

SELECT * FROM testtbl2;
```

현재 어느 숫자까지 증가되었는지 확인하려면 `SELECT LAST_INSERT_ID();` 쿼리를 사용해 마지막에 입력된 값을 알 수 있다. `AUTO_INCREMENT` 입력값을 100부터 입력되도록 변경하고 싶다면 다음과 같이 수행하면 된다.
```sql
ALTER TABLE testtbl2 AUTO_INCREMENT=100;
INSERT INTO testtbl2 VALUES (NULL, '찬미', 23);
SELECT * FROM testtbl2;
```

증가 값을 지정하려면 서버 변수인 `@@auto_increment_increment` 변수를 변경 시켜 주어야 한다.
```sql
USE sqldb;
CREATE TABLE testtbl3
	(id INT AUTO_INCREMENT PRIMARY KEY,
    userName CHAR(3),
    age INT );
ALTER TABLE testtbl3 AUTO_INCREMENT=1000;
SET @@auto_increment_increment = 3;
INSERT INTO testtbl3 VALUES (NULL, '나연', 20);
INSERT INTO testtbl3 VALUES (NULL, '정연', 18);
INSERT INTO testtbl3 VALUES (NULL, '모모', 19);
SELECT * FROM testtbl3;
```

> 여러 개의 행을 한번에 입력할 수도 있다.
> ```sql
> INSERT INTO 테이블이름 VALUES (값1), (값2), ...;
> ```

**대량의 샘플 데이터 생성**

다른 테이블의 데이터를 가져와서 대량으로 입력할 수 있다.
`SELECT`문의 결과 열의 개수는 `INSERT` 할 열의 개수와 일치해야 한다.
```SQL
INSERT INTO 테이블이름 (열 이름1, 열 이름2,...)
    SELECT ... ;
```
```sql
USE sqldb;
CREATE TABLE testtbl4
	(id INT, Fname VARCHAR(50), Lname VARCHAR(50));
INSERT INTO testtbl4
	SELECT emp_no, first_name, last_name
		FROM employees.employees;
SELECT * FROM testtbl4;
```
```sql
CREATE TABLE testtbl5
    (SELECT emp_no, first_name, last_name FROM employees.employees);
```

###### 6.2.2 데이터의 수정: UPDATE
---
```SQL
UPDATE 테이블이름
    SET 열1=값1, 열2=값2 ...
    WHERE 조건;
```
`WHERE`절은 생략가능하지만, 생략하면 테이블의 전체 행이 변경된다.
```SQL
UPDATE testtbl4
    SET Lname = '없음';
    WHERE Fname = 'Kyoichi';
```
예를 들어 구매 테이블에서 단가가 모두 현재에서 1.5배 인상되었다면 다음과 같이 사용할 수 있다.
```sql
UPDATE buytbl SET price = price * 1.5;
```

###### 6.2.3 데이터의 삭제: DELETE FROM
---
```sql
DELETE FROM 테이블이름 WHERE 조건;
```
상위 5건만
```SQL
DELETE FROM testtbl4 WHERE Fname = 'Aamer' LIMIT = 5;
```
> ```SQL
> DELETE FROM bigttbl1;
> DROP TABLE bigttbl2;
> TRUNCATE TABLE bigttbl3;
> ```
> - `DELETE`: DML문. 트랜잭션 로그를 기록하므로 삭제가 오래걸린다.
> - `DROP`: DDL문. 테이블 자체를 삭제한다. 즉, 테이블의 구조 자체를 삭제한다. 또 DDL은 트랜잭션을 발생시키지 않느다
> - `TRUNCATE`: DDL문. DELETE와 동일하지만 DDL이므로 트랜잭션을 발생시키지 않아 속도가 빠르다.


###### 6.2.4 조건부 데이터 입력, 변경
---
멤버테이블 정의
```sql
CREATE TABLE membertbl (SELECT userID, name, addr FROM usertbl LIMIT 3);
ALTER TABLE membertbl
	ADD CONSTRAINT pk_membertbl PRIMARY KEY (userID); -- PK지정
SELECT * FROM membertbl;
```
여러 건 입력 시 PK중복되면 건너 뛰고 나머지 입력.
```sql
insert ignore into membertbl values ('BBK', '비비코', '미국');
insert ignore into membertbl values ('SJH', '서장훈', '서울');
```
PK중복되면 데이터가 수정된다.
```sql
insert into membertbl values ('BBK', '비비코', '미국')
	on DUPLICATE KEY UPDATE name='비비코', addr='미국';
```


##### 6.3 WITH절과 CTE
---
###### 6.3.1 WITH절과 CTE개요
---
WITH절은 CTE(Common Table Expression)을 표현하기 위한 구문으로 MySQL8.0 이후부터 사용가능하다. CTE는 기존의 뷰, 파생테이블, 임시 테이블 등으로 사용되던 것을 대신할 수 있고 더 간결하게 보여진다. CTE는 ANSI-SQL99 표준에서 나오며 최근 DBMS는 대개 호환되므로 다른 DBMS에서도 비슷하게 응용된다.

###### 6.3.2 비재귀적 CTE
---
```sql
WITH CTE_테이블이름(열 이름)
AS
(
    쿼리문
)
SELECT 열 이름 FROM CTE_테이블이름 ;
```
ex)
```SQL
WITH abc(userid, total)
AS
(SELECT userid, SUM(price*amount)
    FROM buytbl, GROUP BY userid )
SELECT * FROM abc ORDER BY total DESC ;
```
다음과 같이 중복 CTE 허용
```SQL
WITH
AAA (컬럼들)
AS ( AAA의 쿼리문 ),
    BBB (컬럼들)
        AS (BBB의 쿼리문),
    CCC (컬럼들)
        AS (CCC의 쿼리문)
SELECT * FROM [AAA or BBB or CCC];
```
CCC 쿼리문에서는 AAA나 BBB를 참조할 수 있지만 AAA나 BBB의 쿼리문에서는 아직 정의되지 않은 CCC를 참조할 수 없다. 즉, 아직 정의되지 않은 CTE를 미리 참조할 수 없다.