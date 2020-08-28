#### 제네릭(Generics) 1
---
##### 제네릭의 이해
---
###### 제네릭 기반의 클래스 정의하기
---
```java
class Box<T> {
  private T ob;
  ...
}
```
- 타입 매개변수(Type Parameter): Box\<T\>에서 T
- 타입 인자(Type Argument): Box\<Apple\>에서 Apple
- 매개변수화 타입(Parameterized Type) or 제네릭 타입(Generic Type): Box\<Apple\>

##### 제네릭의 기본 문법
---
###### 다중 매개변수 기반 제네릭 클래스의 정의
---
```java
class DBox<L, R>{
  ...
}
```

이름 규칙
- 한 문자로 이름을 짓는다.
- 대문자로 이름을 짓는다

보편적으로 사용하는 타입 매개변수
- E: Element
- K: Key
- N: Number
- T: Type
- V: Value

###### 기본 자료형에 대한 제한 그리고 래퍼클래스
---
타입인자로 기본 자료형은 올 수 없다. -> 래퍼클래스 이용

###### 타입 인자의 생략: 다이아몬드 기호
---
`Box<Apple> aBox = new Box<>;`

###### 제네릭 클래스의 타입 인자 제한하기
---
```java
class Box<T> {
  private T ob;
  public int toIntValue() {
    return ob.intValue(); // ERROR;
  }
}
```

Number 또는 이를 상속하는 클래스로 제한
```java
class Box<T extends Number> {
  private T ob;
  public int toIntValue() {
    return ob.intValue(); // OK
  }
}
```
제네릭을 제한하므로써 intValue 메쏘드를 가지고 있음이 보장되므로 가능하다.

###### 제네릭 클래스의 타입 인자를 인터페이스로 제한하기
---
하나의 클래스와 하나 이상의 인터페이스에 대해 동시에 제한을 할 수 있다.

`class Box<T extends Number & Eatable> {...} `: Number를 상속하면서 동시에 Eatable 인터페이스를 구현하는 클래스만이 타입 인자로 올 수 있다.

###### 제네릭 메소드의 정의
---
> 클래스 전부가 아닌 일부 메소드에 대해서만 제네릭으로 정의할 수 있다. 이를 제네릭 메소드라 한다.

```java
class BoxFactory {
  public static <T> Box<T> makeBox(T o)  {
    ...
  }
}
```
Box\<T\>가 반환형. 그 앞의 \<T\>는 T가 타입 매개변수임을 알리는 표시
```java
Box<Double> dBox = BoxFactory.<Double>makeBox(7.59); //오토 박싱 진행된다.
Box<Double> dBox = BoxFactory.makeBox(7.59); // <Double> 생략가능
```
make박스에 전달되는 인자를 보고 T를 유추할 수 있기 때문에 생략 가능하다.

###### 제네릭 메소드의 제한된 타입 매개변수 선언
---
제네릭 메소드도 호출 시 전달되는 타입 인자를 제한할 수 있고 제네릭 클래스의 타입 인자 제한 시와 같은 특성을 갖는다.