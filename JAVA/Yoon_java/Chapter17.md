#### 인터페이스와 추상 클래스
---
##### 인터페이스의 기본과 그 의미
---
###### 추상 메소드만 담고 있는 인터페이스
---
```java
interface Printable {
  // 추상메소드
  // 몸체가 없고 세미콜론으로 마무리
  public void print(String doc);

  //디폴트 메소드
  default void printCMYK(String doc) {}
}
class Printer implements Printable {
  @Override
  public void print(String doc){
    ...
  }
}
```
- 키워드 inplements 를 이용해 구현
- 둘 이상의 인터페이스를 동시에 구현 가능
- 상속과 구현 동시에 가능
- 인터페이스의 형을 대상으로 참조변수의 선언 가능
- 오버라이딩 관계 성립 -> @Override 선언 가능

##### 인터페이스의 문법 구성과 추상 클래스
---
###### 인터페이스에 선언되는 메소드와 변수
---
**인터페이스에 정의된 추상메소드**
- public 선언이 된 것으로 간주한다.
- 인터페이스를 구현하는 클래스는 모든 추상메소드를 구현해야 한다.

**인터페이스 내 변수**
- 선언과 동시에 값으로 초기화를 해야한다.
- public, static, final 이 선언된 것으로 간주한다.

###### 인터페이스 간 상속
---
> extends 로 명시한다.

###### 인터페이스의 디폴트 메소드
---
- 메소드 앞에 default
- 인터페이스 내에 있지만 자체로 완전한 메소드
- - 클래스가 오버라이딩 하지 않아도 된다.
- 인터페이스에 추상 메소드를 추가해야 하는 상황에서 이전에 개발해 놓은 코드에 영향을 미치지 않기 위해

###### 인터페이스의 static 메소드(클래스 메소드)
---
- 인터페이스에도 static 메소드를 정의할 수 있다.
- 클래스의 static메소드 호출 방법과 같다

###### 인터페이스의 또 다른 사용 용도: Marker Interface
---
```java
interface Upper {}
interface Lower {}

interface Printable{
  ...
}

class Report implements Printable, Upper {
  ...
}
```
> instanceof 를 이용해 마커에 따라 다른 상황을 부여할 수 있다.

###### 추상 클래스: Abstract Class
---
```java
public abstract class House {
  public void methodOne() {
    ...
  }
  // 추상 메소드
  public abstract void methodTwo();
}
```
- abstract 선언 추가
- 인터페이스와 성격이 유사하다
- - 인스턴스 생성 불가
- - 다른 클래스에 의해서 추상 메소드가 구현 되어야 한다.