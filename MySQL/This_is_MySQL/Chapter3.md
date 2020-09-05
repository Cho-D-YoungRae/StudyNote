#### Chapter 3. MySQL 전체 운영 실습
---
##### 3.2 요구사항 분석과 시스템 설계 그리고 모델링
---
###### 3.2.1 데이터베이스 생성
---
SCHEMAS의 빈 공간에 우클릭 -> Create Schema

`CREATE SCHEMA 'name';` : 데이터베이스 생성

###### 3.2.2 테이블 생성
---
MySQL은 기본적으로 테이블, 열 이름 등 모두 소문자로 처리한다. 그러므로 대문자로 입력하더라도 소문자로 변경되어서 저장된다.

db확장 -> Tables우클릭 -> Create Table
###### 3.2.3 데이터 입력
---
해당 테이블 우클릭 -> Select Rows - Limits 100

`INSERT INTO...`: 데이터 입력

`DELETE...`: 데이터 삭제

###### 3.2.4 데이터 활용
---
데이터를 활용한다는 것은 주로 `SELECT`문을 사용한다는 의미이다.


1. 상단 제일 왼쪽(Create a new SQL tab for executing queries) 혹은 FIlE -> New Query Tab
2. SCHEMAS의 사용하려는 데이터베이스 더블클릭 -> 쿼리 창에 입력할 SQL문이 선택된 데이터베이스에서 적용된다는 의미
3. 툴바의 실행버튼(Execute the selected portion~~) 혹은 Ctrl+Shift+Enter 혹은 메뉴의 Query -> Execute(All or Selection)
    - 드래그한 부분만 실행 가능

`select 열 이름 from 테이블 이름 where 조건`
- \* 는 '모든'
- 대소문자 구분 없음

```
create table `띄어쓰기 있는 테이블 명` (id INT);
```
- 테이블 생성
- 띄어쓰기 있는 테이블 명 가능
- 해당 테이블이 보이지 않으면 Navigator에서 우클릭->Refresh All

```
drop table `띄어쓰기 있는 테이블 명`;
```

##### 3.3 테이블 외의 데이터베이스 개체의 활용
---
