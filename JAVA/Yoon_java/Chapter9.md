#### 정보 은닉 그리고 캡슐화
##### 접근 수준 지시자
###### 네 가지 종류의 접근 수준 지시자 'Access-level Modifiers'
> public, protected, private, default
> * 클래스 정의 대상: public, default
> * 인스턴스 변수와 메소드 대상: public, protected, private, default

###### 클래스 정의 대상의 public과 default 선언이 갖는 의미
```java
public class AAA {
  ...
}
```
> 위치에 상관없이 어디서든 해당 클래스 인스턴스를 생성 가능

```java
class ZZZ {
  ...
}
```
> 동일 패키지로 묶인 클래스 내에서만 인스턴스 생성이 가능

**클래스의 public 선언 관련 사항**
* 하나의 소스파일에 하나의 클래스만 public으로 선언한다.
* 소스파일의 이름과 public으로 선언된 클래스의 이름을 일치시킨다.

###### 인스턴스 멤버 대상의 public, protected, private, default 선언
```java
class AAA {
  public int num1;
  protected int num2;
  private int num3;
  int num4;

  public void md1() {}
  protected void md2() {}
  private void md3() {}
  void md4() {}
}
```

**public**: 어디서든 접근이 가능하다.

**default**: 동일 패키지로 묶인 클래스 내에서만 접근이 가능하다.

**private**: 클래스 내부에서만 접근 가능

**protected**: 
default선언이 허용하는 접근 가능 + 상속 관계에 있는 다른 클래스에서 접근 가능




