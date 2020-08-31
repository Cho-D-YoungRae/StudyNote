#### 열거형, 가변 인자 그리고 어노테이션
---
##### 열거형
---
> '의미가 부여된 이름'을 갖는 '상수'의 선언에 그 목적이 있다.

###### 자료형의 부여를 돕는 열거형
---
열거형 정의
```java
enum Scale {
  DO, RE, MI, FA, SO, RA, TI
}
```
example
```java
Scale sc = Scale.DO;  //  열거형 내에 선언된 '열거형 값'만 대입 가능
System.out.println(sc); // DO 출력

switch(sc) {  //  switch문 구성 가능
case DO:
  ...
}
```

###### 클래스 내에 정의가 가능한 열거형의 정의
---
###### 열거형 값의 정체
---
열거형은 클래스다. 위 Scale 열거형은 클래스이고, 열거형 값은 Scale 인스턴스를 참조하는 참조변수이다. 열거형의 정의에도 생성자가 없으면 디폴트 생성자가 삽입된다. 다만 이 생성자는 private으로 선언이 되어 직접 생성하는 것이 불가능 할 뿐이다.
```java
enum Person {
  MAN(29), WOMAN(25);

  int age;
  private Person(int age) {
    this.age = age;
  }
}
```
- Person.MAN -> age = 29인 enum 생성
- Person.WOMAN -> age = 25인 enum 생성

열거형도 java.lang.Enum\<E\> -> Object를 상속하는 일종의 클래스이다. 따라서 생성자, 인스턴스 변수, 메소드 다 가질 수 있다. 하지만 모든 생성자를 private으로 선언해야하므로 '열거형 값'이 유일한 인스턴스 생성 방법이다.

##### 매개변수의 가변 인자 선언
---
> `public static int hash(Object...values)` 에서 ...이 삽입된 이 메소드의 매개변수 선언을 '가변 인자 선언'이라 한다.

###### 매개변수의 가변인자 선언과 호출
---
```java
class Varargs {
    public static void showAll(String... vargs) {
        System.out.println("LEN: " + vargs.length);

        for(String s : vargs) 
            System.out.print(s + '\t');
        System.out.println();
    }

    public static void main(String[] args) {
        showAll("Box");
        showAll("Box", "Toy");
        showAll("Box", "Toy", "Apple");
    }
}
```
> LEN: 1<br>
> Box
> LEN: 2<br>
> Box Toy
> LEN: 3<br>
> Box Toy Apple

###### 가변 인자 선언에 대한 컴파일러의 처리
---
가변 인자 선언이 추가되기 이전에는 다음과 같이 코드를 작성해야만 했다.
```java
class VarargsBefore {
    public static void showAll(String[] vargs) {
        System.out.println("LEN: " + vargs.length);

        for(String s : vargs) 
            System.out.print(s + '\t');
        System.out.println();
    }

    public static void main(String[] args) {
        showAll(new String[]{"Box"});
        showAll(new String[]{"Box", "Toy"});
        showAll(new String[]{"Box", "Toy", "Apple"});
    }
}
```
그리고 이것이 자바 컴파일러가 가변 인자 선언 및 메소드 호출문을 처리하는 방식이다.


##### 어노테이션 (Annotations)
---
> 자바 컴파일러에게 메세지를 전달하는 목적의 메모

###### @Override
---
> 상위 클래스의 메소드 오버라이딩 또는 인터페이스에 선언된 추상 메소드의 구현

###### @Deprecated
---
- 문제의 발생 소지가 있거나 개선된 기능의 다른 것으로 대체되어서 더 이상 필요 없게 되었음을 뜻한다.
- 아직은 호환성 유지를 위해 존재하지만 이후에 사라질 수 있는 클래스 또는 메소드를 가르킨다.
- 컴파일은 되지만 경고메세지를 보낸다.

###### @SuppressWarnings
---
특정 경고에 대하여 경고 대상에서 제외시킬 수 있다.
- `@SuppressWarnings("경고")`
- `@SuppressWarnings({"경고1", "경고2"})` : 둘 이상의 경고 유형에 대해 동시에 처리할 때





