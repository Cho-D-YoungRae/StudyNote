#### 클래스의 상속 2: 오버라이딩
##### 메소드 오버라이딩
###### 상위 클래스의 참조변수가 참조할 수 있는 대상의 범위
**상위클래스의 참조변수는 하위 클래스의 인스턴스를 참조할 수 있다.**
> `class SmartPhone extends MobilePhone {...}`
> > `SmartPhone phone1 = new SmartPhone(...);`
> > `MobilePhone phone2 = new SmartPhone(...);`
phone2를 통해서 접근이 가능한 멤버는 MobilePhone 클래스에 정의되었거나 이 클래스가 상속하는 클래스의 멤버로 제한된다. (phone2가 참조하는 인스턴스가 무엇인지는 상관없다.)

###### 참조변수 간 대입과 형 변환
```java
class Cake {
  public void sweet() {};
}
class CheeseCake extends Cake {
  public void milky() {};
}
```
**가능**
```java
CheeseCake ca1 = new CheeseCake();
Cake ca2 = ca1; // 가능
```
**불가능**
```java
Cake ca3 = new CheeseCake();
CheeseCake ca4 = ca3; // 불가능
```
> ca3이 참조하는 인스턴스가 CheeseCake 인스턴스임은 확신할 수 없다.
> 참조변수의 형(Type) 정보를 기준으로 대입의 가능성을 판단한다.

**가능**
`CheeseCake ca4 = (CheeseCake)ca3;`
> 명시적으로 형 변환을 하면 대입이 가능하다.

###### 메소드 오버라이딩 (Method Overriding)
> - 상위 클래스에 정의된 메소드를 하위 클래스에서 다시 정의
> - 메소드의 이름, 메소드의 반환형, 메소드의 매개변수 선언 이 같아야 성립한다.
> - 참조변수의 형에 상관없이 오버라이딩 한 메소드(하위 클래스의 메소드)가 오버라이딩 된 메소드(상위 클래스의 메소드)를 대신하게 된다.

###### 메소드 오버라이딩의 일반화
```java
class Cake {
  public void yummy() {}
}
class CheeseCake extends Cake {
  public void yummy() {}
}
class StrawberryCheeseCake extends CheeseCake {
  public void yummy() {}
}
```
위와 같이 정의 되어 있을 때
```java
Cake c1 = new StrawberryCheeseCake();
CheeseCake c2 = new StrawberryCheeseCake();
StrawberryCheeseCake c3 = new StrawberryCheeseCake();


c1.yummy(); // 오버라이딩 한 StrawberryCheeseCake의 메소드
c2.yummy(); // 오버라이딩 한 StrawberryCheeseCake의 메소드
c3.yummy();
```

###### 오버라이딩 된 메소드를 호출하는 방법
> 하위 클래스의 인스턴스를 생성해서 상위 클래스의 오버라이딩 된 메소드를 호출할 수 없다.

```java
Cake c1 = new CheeseCake(); // 불가능
CheeseCake c2 = new CheeseCake(); // 불가능
```

> 클래스 외부가 아닌 내부에서 가능

```java
class CheeseCake extends Cake {
  public void yummy() {
    super.yummy();
  }
}
```

###### 인스턴스 변수와 클래스 변수도 오버라이딩의 대상이 되는가?
- 오버라이딩되지 않으나 이렇게 동일한 이름의 변수를 하위 클래스에서 선언하는 일은 가급적 피해야 한다.
- 참조변수의 형에 따라서 접근하는 변수가 결정된다.
- 클래스 변수와 클래스 메소드의 경우도 마찬가지이다.

```java
CheeseCake c1 = new CheeseCake();
c1.size = ... // CheeseCake 의 size

Cake c2 = new CheeseCake();
c1.size = ... // Cake 의 size
```

##### instanceof 연산자
###### instanceof 연산자의 활용
> 명시적 형 변환의 가능성을 판단해주는 연산자이다.




