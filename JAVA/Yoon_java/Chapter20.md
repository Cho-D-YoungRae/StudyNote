#### 자바의 기본 클래스
---
##### 래퍼 클래스 (Wrapper 클래스)
---
###### 래퍼 클래스의 두 가지 기능
---
```java
Integer iObj = new Integer(10); // 박싱
int num1 = iObj.intValue(); // 언박싱
```
래퍼 인스턴스들은 담고 있는 값 수정 불가능

###### 오토 박싱 & 오토 언박싱
---
```java
Integer iObj = 10;  // 오토 박싱
iObj++; // 오토 박싱, 오토 언박싱 동시 진행
iObj += 3;  // 오토 박싱, 오토 언박싱 동시 진행
int num1 = iObj;  //오토 언박싱
```

###### Number 클래스와 래퍼 클래스의 static 메소드
---
앞의 모든 래퍼 클래스는 다음 클래스를 상속한다.
> java.lang.Number

이 클래스에는 다음의 추상 메소드들이 존재한다(즉 Number도 추상클래스). 래퍼 클래스들은 아래 메소드를 구현하고있다.
- `public abstract int intValue()`
- `public abstract long longValue()`
- `public abstract double doubleValue()`


래퍼 클래스의 static 메소드
- `Integer.max(n1, n2);`
- `Integer.min(n1, n2);`
- `Integer.sum(n1, n2);`
- `Integer.valueOf(num);` 숫자 기반 인스턴스 생성
- `Integer.valueOf("str");` 문자열 기반 인스턴스 생성
- `Integer.toBinaryString(num);`

##### BigInteger 클래스와 BigDecimal 클래스
---
###### 매우 큰 정수의 표현을 위한 java.math.BigInteger 클래스
###### 오차 없는 실수의 표현을 위한 java.math.BigDecimal 클래스
---

##### Math 클래스와 난수의 생성, 그리고 문자열 토큰(Token)의 구분
---
###### 수학 관련 다양한 연산의 제공을 위한 Math 클래스
---
수학과 관련된 static 메소드들이 선언되어있다.

###### 난수(Random Number) 생성
---
난수 생성을 위한 java.util.Random 클래스
`Random rand = new Random();`

인스턴스 생성 후 아래 메소드 호출
- `public boolean nextBoolean()`
- `public int nextInt()`
- `public long nextLong()`
- `public int nextInt(int bound)`: 0이상 bound 미만
- `public float nextFloat()`: 0.0 ~ 1.0미만
- `public double nextDouble()`: 0.0 ~ 1.0미만

###### 씨드(Seed) 기반의 난수 생성
---
`Random rand = new Random(12);`: 12 는 seed 값
```java
public Random() {
  this(System.currentTimeMillis()); // Random(long seed)
}
```
seed 값 없이 그냥 실행하면 생성자를 통해 생성된다.

###### 문자열의 토큰(Token) 구분
- `public StringTokenizer(String str, String delim)`
- - `StringTokenizer st = new StringTokenizer("12 + 36 - 8 / 2 = 44", "+-/= ");`
- `public boolean hasMoreTokens()`
- `public String nextToken()` : 토큰이 없는 상태에서 호출되면 예외 발생
- 구분자도 토큰으로 반환하려면 생성자 마지막 매개변수에 true 추가

##### Arrays 클래스
---
> java.util.Arrays

###### 배열의 복사
---
모든 기본 자료형에 대해 오버로딩 (제네릭)
- `public static int[] copyOf(int[] original, int newLength)`
- `public static int[] copyOfRange(int[] original, int from, int to)`
- `public static void arraycopy(Object src, int srcPos, Object dest, int destPos, int length)`
- - 배열 src의 srcPos에서 배열 dest의 destPos로 length 길이만큼 복사

###### 배열의 비교
---
`public static boolean equals(int[] a, int[] a2)`
`public static boolean equals(Object[] a, Object[] a2)` : Object의 equals를 통해

###### 배열의 정렬
---
`public static void sort(int[] a)`

`public static void sort(Object[] a)` 의 정렬기준
- interface Comparable의 `int compareTo(Object o)`메소드 구현을 통해
- o가 작으면, 양의 정수 반환
- o가 크다면, 음의 정수 반환
- o와 같으면, 0 반환

###### 배열의 탐색
---
`public static int binarySearch(int[] a, int key)`
- 정렬 후 가능

`public static int binarySearch(Object[] a, Object key)`
- compareTp 메소드를 통해 찾는다. -> 0일 때




