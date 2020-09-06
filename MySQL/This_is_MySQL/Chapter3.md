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
###### 3.3.1 인덱스
---
많은 데이터가 있을 때 탐색을 빠르게 해준다.

Execution Plan -> Full Table Scan : 인덱스를 사용하지 않고 테이블 전체를 검색했다는 뜻

`create index idx_indextbl_firstname ON indextbl(first_name);`
- 인덱스 이름 `idx_indextbl_firstname`은 `indextbl` 테이블의 `first_name`열에 생성된 색인이 된다.
- 인덱스 이름을 위 처럼 어느 테이블의 어느열에 설전된 것인지 알 수 있도록 지정해 주는 것이 좋다.

Excution Plan -> Non-Unique Key Lookup : 인덱스를 사용했다는 의미

###### 3.3.2 뷰
---
> 가상의 테이블. 진짜 테이블에 링크된 개념이라고 생각하면 된다.

```sql
create view uv_membertbl
as
	select membername, memberaddress from membertbl;
```
- membertbl 테이블에서 membername, memberaddress 만 가져온 uv_membertbl 뷰 테이블

###### 3.3.3 스토어드 프로시저
> MySQL 에서 제공해주는 프로그래밍 기능. 즉, SQL문을 하나로 묶어서 편리하게 사용하는 기능.

```sql
delimiter //
create procedure myproc()
begin
	select * from membertbl where membername = '당탕이' ;
    select * from producttbl where productname = '냉장고' ;
end//
delimiter ;
```
- myproc() 이라는 스토어드 프로시저를 만든다
- delimiter는 '구분 문자'를 뜻한다. 뒤에 //가 나오면 기존의 세미콜론을 //로 대신한다는 의미이다.
  - create procedure ~ end 까지를 하나의 단락으로 묶어주는 효과
  - 다시 마지막에 세미콜론으로 돌려놓는다.

`call myproc();` 으로 실행할 수 있다.

**create**
> 데이터베이스 개체를 만들기 위해서 `create 개체종류 개체이름 ~~`의 형식을 사용한다.

**drop**
> 데이터베이스 개체를 삭제하기 위해서는 `drop 개체종류 개체이름` 으로 사용하면 된다.

###### 3.3.4 트리거
---
> 테이블에 부착되어서 테이블에 `insert`, `update`, `delete` 작업이 발생되면 실행되는 코드를 말한다.

```sql
insert into membertbl values ('Figure', '연아', '경기도 군포시 당정동');
```

```sql
update membertbl set memberaddress = '서울 강남구 역삼동' where membername = '연아';
```

```sql
delete from membertbl where membername = '연아';
```

'연아'가 삭제된 후, 연아가 이전에 회원이었다는 정보는 기록이 없다.

```sql
create table deletedmembertbl (
	memberid char(8),
    membername char(5),
    memberaddress char(20),
    deleteddate date -- 삭제한 날짜
);
```
지워진 데이터를 보관할 테이블

```sql
DELIMITER //
CREATE TRIGGER 	trg_deletedMemberTBL -- 트리거 이름
	AFTER DELETE -- 삭제 후에 작동하게 지정
    ON memberTBL -- 트리거를 부착할 테이블
    FOR EACH ROW -- 각 행마다 적용시킴
BEGIN
	-- OLD 테이블의 내용을 백업 테이블에 삽입
    INSERT INTO deletedMemberTBL
		VALUES (OLD.memberID, OLD.memberName, OLD.memberAddress, CURDATE() );
END //
DELIMITER ;
```

##### 3.4 데이터베이스 백업 및 관리
---
###### 3.4.1 백업과 복원
---
**백업**
1. Navigator의 Administration 탭을 클릭한 후, Data Export 클릭
2. 데이터베이스를 선택하면 오른쪽에 테이블, 뷰 등이 보인다. 모두 체크하자.
3. Object to Export 도 모두 체크해서 스토어드 프로시저, 스토어드함수, 트리거 등도 모두 백업한다.
4. 백업 경로는 Export to Self-Contained File 에서 자기 컴퓨터 내 경로 설정
5. Create Dump in a Single~~ 및 Include Create Schema 도 체크
6. 모든 내용을 백업하도록 설정한 것이다. -> Start Export

**복원**
1. 사용중인 데이터베이스를 복원하면 문제가 생길 수 있으므로 복원하려는 DB와 다른 DB로 일단 이동
    - `USE DB;`
2. Navigator의 Administration 탭을 클릭한 후, Data Import/Restore 클릭
3. Import from Self-Contained File 선택 -> 파일이 있는 경로 선택
4. Default Target Schema 에서 해당되는 것 선택
5. Start Import

##### 3.5 MySQL과 응용 프로그램의 연결
---
