#### Chapter 4. 데이터베이스 모델링
---
##### 4.2 데이터베이스 모델링
---
###### 4.2.2 데이터베이스 모델링 실습
---
**새로운 모델 생성**
1. File -> New Model
2. 기본적으로 데이터베이스 이름은 mydb로 되는데 우클릭 후 Edit Schema를 통해 변경 가능
3. Model Overview -> Add Diagram -> EER Diagram 탭이 추가된다.
4. 왼쪽의 Place a New Table 클릭 후 빈 화면에 마우스 클릭하면 테이블 생성
5. 테이블 더블 클릭 후 테이블 정보 입력
6. 왼쪽의 Place a Relationship Using Existing column 클릭 후 외래 키 -> 기본 키 순서로 클릭 하여 연결
7. Workbench 메뉴의 File -> Save Model 클릭 하여 저장

**모델링한 파일을 실제 데이터베이스에 적용**
1. Workbench 메뉴의 File -> Open Model
2. Workbench 메뉴의 Database -> Forward Engineer


**기존의 데이터베이스를 이용해서 다이어그램 작성**
1. Workbench 메뉴의 Database -> Reverse Engineer