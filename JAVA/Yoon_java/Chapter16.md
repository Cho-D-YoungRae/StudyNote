#### 클래스의 상속 3: 상속의 목적
##### 상속이 도움이 되는 상황의 소개
###### 인맥 관리 프로그램의 문제를 상속으로 해결하자.
```java
Friend[] frns = new Friend[10];

// UnivFriend와 CompFriend 는 Friend 를 상속한다.
//적절히 오버라이딩도 되어있다.
frns[0] = new UnivFriend("Lee", "Computer");
frns[1] = new CompFriend("Yoon", "R&D");
```

##### Object 클래스와 final 선언 그리고 @Override
###### 모든 클래스는 Object 클래스를 상속합니다.
> java.lang 패키지 안에 있다.

`public void println(Object X)`
- 매개변수 형이 Object이므로 모든 인스턴스는 인자가 될 수 있다.
- 인자로 전달된 인스턴스의 다음 메소드를 호출한다

`public String toString()`
- Object클래스에 정의되어 있다.
- 클래스를 정의할 때, 가급적 오버라이딩 하자.

###### 클래스와 메소드의 final 선언
```java
public final class simple { // 다른 클래스가 상속할 수 없다.
  public final void func(int n) {}  // 오버라이딩을 할 수 없다.
}
```

###### @Override
> 어노테이션(Annotations)

```java
class ChildAdder extends ParendAdder {
  @Override
  public double add(double a, double b) {}
}
```
- 이 메소드는 상위 클래스의 메소드를 오버라이딩 할 목적으로 정의하였습니다.
- 프로그래머의 의도대로 오버라이딩이 되지 않으면 에러를 띄워준다
- - 매개변수 형, 반환형 등 다르면 오버라이딩이 되지 않는다.

