#### Chapter 8. 테이블과 뷰
---
##### 8.1 테이블
---
###### 8.1.1 테이블 만들기
---
*SQL로 테이블 생성*
**실습2**
```sql
USE tabledb;
DROP TABLE IF EXISTS buytbl, usertbl;
CREATE TABLE usertbl
(	userID 	CHAR(8) NOT NULL PRIMARY KEY,
	name	VARCHAR(10) NOT NULL,
    birthYear	INT NOT NULL,
    addr	CHAR(2) NOT NULL,
    mobile1	CHAR(3),
    mobile2	CHAR(8),
    height	SMALLINT,
    mDate	DATE
);
CREATE TABLE buytbl
(	num		INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	userid	CHAR(8) NOT NULL,
    prodName	CHAR(6) NOT NULL,
    groupName	CHAR(4),
    price	INT NOT NULL,
    amount	SMALLINT NOT NULL,
    FOREIGN KEY (userid) REFERENCES usertbl(userID)
);
```
- `AUTO_INCREMENT`로 지정한 열은 `PRIMARY KEY` 혹은 `UNIQUE` 로 지정해줘야 한다.
- `NOT NULL` 을 명시하지 않으면 `NULL`이 디폴트다.
- 기본 키로 설정된 열은 당연히 `NULL`이 허용되지 않는다. 그러므로 `NOT NULL`을 빼도 관계없다.
```sql
INSERT INTO usertbl VALUES
	('LSG', '이승기', 1987, '서울', '011', '11111111', 182, '2008-8-8'),
    ('KBS', '김범수', 1979, '경남', '011', '22222222', 173, '2012-4-4'),
    ('KKH', '김경호', 1971, '전남', '019', '33333333', 177, '2007-7-7');
```
```sql
INSERT INTO buytbl VALUES
	(NULL, 'KBS', '운동화', NULL, 30, 2),
    (NULL, 'KBS', '노트북', '전자', 1000, 1);
 -- (NULL, 'JYP', '모니터', '전자', 200, 1) usertbl에 'JYP' 없으므로 오류난다
```

###### 8.1.2 제약 조건
---