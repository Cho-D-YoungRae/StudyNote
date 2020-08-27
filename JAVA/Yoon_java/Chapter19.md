#### 자바의 메모리 모델과 Object 클래스
---
##### Object 클래스
---
###### 인스턴스 소멸 시 해야 할 일이 있다면: finalize 메소드
---
> `protected void finalize() throws Throwable`

###### 인스턴스의 비교: equals 메소드
---
> ==연산자는 참조변수의 참조값을 비교하므로 인스턴스 내용을 비교하기위해 별도의 방법을 사용해야 한다.

```java
class INum {
  private int num;
  @Override
  public boolean equals(Object obj) { // Object의 메소드
  if(this.num == ((INum)obj).num)
    return true;
  else
    return false;
  }
}
```
equals 를 오버라이딩 하자

###### 인스턴스 복사(복제): clone 메소드
---
Object 클래스에는 인스턴스의 복사를 위한 다음 메소드가 정의되어 있다.
> `protected Object clone() throws CloneNotSupportedException`

> interface Cloneable(마커 인터페이스) 를 구현한 클래스의 인스턴스를 대상으로 호출할 수 있으며 구현하지 않은 클래스의 인스턴스가 호출하면 위의 예외가 발생한다.

> 오버라이딩을 통해 protected를 public으로 바꿔주자 -> 오버라이딩을 통해 접근 범위를 넓히는 것이 가능하다. 거꾸로 접근 범위를 제한 하는 것은 불가능 하다.

**깊은 복사**
```java
class Rectangle implements Cloneable {
  private Point upperLeft;
  private Point lowerRight;
  @Override
  public Object clone() throws CloneNotSupportedException {
    Rectangle copy = (Rectangle)super.clone();

    copy.upperLeft = (Point)upperLeft.clone();
    copy.lowerRight = (Point)lowerRight.clone();

    return copy
  }
}
```

###### 인스턴스 변수가 String인 경우의 깊은 복사
---
String은 Cloneable 인터페이스를 구현하지 않았다.
> String은 문자열의 수정이 불가능하므로, 깊은 복사의 대상에서 제외 해도 된다.

###### clone 메소드의 반환형 수정: Covariant Return Type
- 자바 5 이후부터는 오버라이딩 과정에서 반환형의 수정을 허용한다
- 상위클래스로 반환형이 되어 있는 메소드를 오버라이딩하는 하위클래스의 반환형으로만 수정할 수 있다.

```java
class AAA {
  public AAA method() { } // 반환형이 자신이 속한 AAA 클래스
}
class ZZZ {
  @Override
  public ZZZ method() { } // 반환형이 자신이 속한 ZZZ 클래스
}
