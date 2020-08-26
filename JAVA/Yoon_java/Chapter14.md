#### 클래스의 상속 1: 상속의 기본
##### 상속의 기본 문법 이해
###### 상속의 가장 기본적인 특성
```java
class BusinessMan extends Man {
  ...
}
```
Man 을 상속하는 BuisnessMan

###### 상속과 생성자
```java
class SuperCls {
  ...
}

class SubCls extends SuperCls {
  public SubCls() {
    super();  // 상위 클래스의 생성자를 지정 및 호출
  }
}
```
> 상위 클래스의 생성자는 하위 클래스 생성자의 몸체 부분에 앞서 실행 되어야 한다.
> > ```java
> > public SubCls() {
> >   System.out.println(...);
> >   super(); //이 위치에 있으면 컴파일 오류
> > }
> > ```
> 상위 클래스 생성자 호출을 생략하면 하위 클래스 생성자 제일 처음에 자동으로 디폴트 생성자 실행된다. 

###### 단일 상속만을 지원하는 자바
> 하나의 클래스는 하나의 클래스만 상속 가능

##### 클래스 변수, 클래스 메소드와 상속
###### static 선언이 붙는 '클래스 변수'와 '클래스 메소드'의 상속
```java
class superCls {
  protected static int count = 0;
}

class subCls {
  public void exampleFunc() {
    count++;
  }
}
```
> 하위 클래스에서도 클래스 변수 이름만으로 직접 접근 가능하다.

> private선언 되어있으면 접근 불가이다.