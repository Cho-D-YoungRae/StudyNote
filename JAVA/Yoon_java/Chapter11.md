#### 메소드 오버로딩과 String 클래스
##### 메소드 오버로딩
###### 메소드 오버로딩의 조건
*호출할 메소드를 찾을 때 참조하는 정보*
- 메소드 이름
- 메소드 매개변수 정보

**메소드 오버로딩이 성립하려면**: 매개변수 선언이 달라야한다.

반환형이 다른 것은 안된다.

###### 애매한 상황
오버로딩된 메소드 들 중 두 개 이상의 메소드가 실행 가능할 경우,

가까운 위치에 있는 메소드 실행된다.

###### 키워드 this를 이용한 인스턴스 변수의 접근
메소드의 매개변수 이름이 인스턴스 변수의 이름과 동일하게 선언된 경우,

this키워드를 이용해 인스턴스 변수에 접근 가능.

this는 이 문장이 속한 인스턴스를 의미한다.
``` java
class SimpleBox {
  private int data;
  SimpleBox(int data) {
    this.data = data;
  }
}
```

##### String 클래스
###### String 클래스의 인스턴스 생성
``` java
String str1 = new String("Simple String1");
String str2 = "Simple String2"; // 더 보편적인 방법

System.out.println(str1);
```

###### 문자열 생성을 위한 두 가지 방법의 차이점은?
```java
// str1과 str2는 동일 인스턴스 참조
String str1 = "Simple String";
String str2 = "Simple String";

// str3과 str4 는 다른 인스턴스 참조
String str3 = new String("Simple String");
String str4 = new String("Simple String");
```

###### String 인스턴스를 이용한 switch문의 구성
자바 7부터 가능해졌다.

##### String 클래스의 메소드
- `public String concat(String str)` : str1과 str2를 연결한 결과를 반환
- `public String substring(int beginIndex)` : beginIndex 이후의 문자열 반환
- `public String substring(int beginIndex, int endIndex)` : beginIndex ~ endIndex 사이 반환

###### 문자열 내용 비교
- `public boolean equals(Object anObject)`
- `public int compareTo(String anotherString)` : 사전 편찬 순서
- `public int compareToIgnoreCase(String str)` : 대소문자 구분 안 함

###### 기본 자료형의 값을 문자열로 바꾸기
```java
static String valueOf(boolean b)
static String valueOf(char c)
static String valueOf(double d)
static String valueOf(float f)
static String valueOf(int i)
static String valueOf(long l)
```

###### 문자열을 대상으로 하는 + 연산과 += 연산
- "funny" + "camp" -> "funny".concat("camp")
- "age: " + 17 -> "age: ".concat(String.valueOf(17))

###### 문자열 결합의 최적화: Optimization of String Concatenation
`String birth = "<양> + 7 + '.' + 16;`
> `String birth = "<양>".concat(String.valueOf(7)).concat(String.valueOf('.')).concat(String.valueOf(16));`

기본 자료형의 값을 문자열로 변환하는 과정을 여러번 거쳐야한다.
> String 인스턴스의 생성 -> 성능에 영향

**StringBuilder** 를 이용하자

###### StringBuilder 클래스
> 내부적으로 문자열을 저장하기 위한 메모리공간을 지닌다. 문자를 추가하거나 삭제하는 것이 가능하다.
> >수정하면서 유지해야 할 문자열이 있다면 이 클래스를 이용하는 것이 효율적이다.

- `public StringBuilder append(int i)`
- `public StringBuilder delete(int start, int end)`
- `public StringBuilder insert(int offset, String str)`
- `public StringBuilder replace(int start, int end, String str)`
- `public StringBuilder reverse()`
- `public String substring(int start, int end)`
- `public String toString()`

> 몇 메소드는 다양한 인자를 받을 수 있도록 오버로딩 되어있다.

**생성자**
- `public StringBuilder()` : 16개 문자를 저장할 수 있는 메모리 공간 확보
- `public StringBuilder(int capacity)` : capacity개 문자를 저장할 수 있는 메모리 공간 확보
- `public StringBuilder(String str)` : 전달되는 문자열과 16개 문자를 저장할 수 있는 메모리공간 확보

> StringBuilder 는 메모리 공간을 스스로 관리한다. 즉 부족하면 그 공간을 늘린다. 그러나 이는 소모가 많은 작업이다. 따라서 사용 계획에 따라 적절한 크기를 초기에 만들면 그만큼의 성능 향상을 기대할 수 있다.