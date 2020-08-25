#### 배열 (Array)
##### 1차원 배열의 이해와 활용
###### 1차원 배열 생성 방법
```java
int[] ref = new int[5]; // 변수 선언과 인스턴스 생성 구분 가능
```
###### 배열을 대상으로 한 값의 저장과 참조
```java
String[] sr = new String[3];  // String 참조변수 배열 
sr[0] = new String("Cho");
sr[1] = new String("Young");
sr[2] = new String("Rae");
```

###### 배열을 생성과 동시에 초기화하기
```java
int[] arr = new int[] {1, 2, 3};  // 길이 정보를 생략해야한다.
int[] arr = {1, 2, 3};
```

###### 참조변수 선언의 두 가지 방법
```java
int[] ar = new int[3];
int ar[] = new int[3];  // 조금 더 선호하는 방법
```

###### 배열의 초기화와 배열의 복사
- `public static void fill(int[] a, int val)`
- - 두 번째 인자로 전달된 값으로 배열 초기화
- `public static void fill(int[] a, int fromIndex, int toIndex, int val)`
- - 인덱스 fromIndex ~ (toIndex-1) 의 범위까지 val의 값으로 배열 초기화
> 위의 두 메소드는 java.util.Arrays 클래스에 정의되어 있다.
- `public static void arraycopy(Object src, int srcPos, Object dest, int destPos, int length)`
- - 복사 원본의 위치: 배열 src의 인덱스 srcPos
- - 복사 대상의 위치: 배열 dest의 인덱스 destPos
- - 복사할 요소의 수: length

##### enhanced for 문
###### enhanced for 문
```java
for(요소 : 배열) {
  반복할 문장
}
for(int e : ar) {
  System.out.println(e);
}
```