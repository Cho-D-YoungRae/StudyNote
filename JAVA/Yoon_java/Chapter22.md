#### 제네릭(Generics) 2
---
##### 제네릭의 심화 문법
---
###### 제네릭 클래스와 상속
---
```java
class SteelBox<T> extends Box<T> {
  public SteelBox(T o) {  // 제네릭 클래스의 생성자
    ...
  }
}
```
상속 관계
- `Box<T>` -> `SteelBox<T>`
- `Box<Integer>` -> `SteelBox<Integer>`
- `Box<String>` -> `SteelBox<String>`

**아래와 같은 문장은 성립하지 않는다.**
`Box<Number> box = new Box<Integer>();`

###### 타겟 타입 (Target Types)
---
`Box<Integer> iBox = EmptyBoxFactory.<Integer>makeBox();`
> 인자를 전달받지 않기 때문에 메소드 호출시 \<Integer\> 생략할 수 없었다.

`Box<Integer> iBox = EmptyBoxFactory.makeBox();`
> 자바 7부터 가능해졌다.

> Box\<Integer\> 인스턴스의 참조값을 반환해야 함을 알 수 있다. -> T 는 Integer. Box\<Integer\>는 '타겟 타입'

###### 와일드 카드
---
```java
public static <T> void peekBox(Box<T> box) {
  // 제네릭 메소드
}
public static void peekBox(Box<?> box) {
  // 와일드카드 기반 메소드 정의
}
```
기능적으로 두 메소드는 동일하며 상호 대체 가능하다. 그러나 와일드카드 기반이 더 간결하므로 더 선호 된다.

###### 와일드카드의 상한과 하한의 제한: Bounded Wildcards
---
`Box<? extends Number> box`
- box는 Box\<T\> 인스턴스를 참조하는 참조변수이다.
- 단 이때 Box\<T\> 인스턴스의 T는 Number 또는 이를 상속하는 하위 클래스이어야한다.

`Box<? super Integer> box`
- box는 Box\<T\> 인스턴스를 참조하는 참조변수이다.
- 단 이때 Box\<T\> 인스턴스의 T는 Integer 또는 Integer가 상속하는 클래스이어야한다.

###### 언제 와일드카드에 제한을 걸어야 하는가?: 상한 제한의 목적
---
```java
public static void outBox(Box<? extends Toy> box) {
  /* 이 안에서 box가 참조하는 인스턴스에 Toy인스턴스를
    저장하는(전달하는) 메소드 호출은 불가능하다 */
}
```
```java
public static void outBox(Box<? extends Toy> box) {
  box.get(); // 꺼내는 것 OK
  bot.set(); // 넣는 것 ERROR
}
```
Toy 인스턴스를 저장할 수 있는 상자만 전달된다는 사실을 보장할 수 없기 때문이다.

예를 들어, Toy 클래스는 다른 클래스들에 의해 얼마든지 상속될 수 있다.
> ```java
> class Car extends Toy {...}
> class Robot extends Toy {...}
> ```

이렇게 상속 관계를 맺으면 위의 메소드에 Box<Car> 또는 Box<Robot> 이 올 수 있고 이 들은 Toy 인스턴스를 담을 수 없다.

###### 언제 와일드카드에 제한을 걸어야 하는가?: 하한 제한의 목적
---
```java
public static void inBox(Box<? super Toy> box) {
  /* 이 안에서는 box가 참조하는 인스턴스에서
    Toy 인스턴스를 꺼내는(반환하는) 메소드 호출은 불가능 하다. */
}
```
```java
public static void inBox(Box<? super Toy> box, Toy n) {
  box.set(n); // 넣는 것 OK
  Toy myToy = box.get();  // 꺼내는 것 ERROR
}
```
반환형을 Toy로 결정할 수 없기 때문이다. 즉 get 메소드 호출 자체는 문제 되지 않으나, 반환되는 값을 저장하기 위해 선언한 참조변수의 형을 Toy로 결정했다는 사실에서 문제가 발생한다.

예를 들어, Toy 클래스의 상속 관계가 다음과 같다고 가정하자.
```java
class Plastic {...}
class Toy extends Plastic {...}
```

`Toy myToy = box.get();`에서 

Box\<Toy\>인스턴스가 전달되면 get이 반환하는 것이 Toy 인스턴스이므로 문제가 없지만,

Box\<Plastic\>인스턴스가 전달되면 get이 반환하는 것이 Plastic이므로 문제가 된다.

###### 제한된 와일드카드 선언을 갖는 제네릭 메소드
---
```java
class BoxHandler {
  // 다음 두 메소드는 오버로딩 인정 안됨.
  public static void outBox(Box<? extends Toy> box) {...}
  public static void outBox(Box<? extends Robot> box) {...}

  // 다음 두 메소드는 두 번째 매개변수로 인해 오버로딩 인정 됨.
  public static void inBox(Box<? super Toy> box, Toy n) {...}
  public static void inBox(Box<? super Robot> box, Robot n) {...}

  // 'Type Erasure'로 인해 오버로딩되지 않는 위 메소드 해결
  // 제네릭 메소드
  public static <T> void outBox(Box<? extends T> box) {...}
}
```

###### 제네릭 인터페이스의 정의와 구현
> 인터페이스 역시 클래스와 마찬가지로 제네릭으로 정의할 수 있다.

```java
interface Getable<T> {
  public T get();
}

// T를 결정한 상태로 구현할 수 있다.
class Box<T> implements Getable<String> {...}
```

위와 같이 T가 결정된 채로 인터페이스 구현되면
```java
Box<Toy> box = new Box();
...
Getable<String> gt = box;
...
```
Getable\<String\>형 참조변수는 Box\<T\>인스턴스를 T에 상관없이 참조할 수 있다.
