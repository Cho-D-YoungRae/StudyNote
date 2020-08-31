#### 네스티드 클래스와 람다(Lambda)의 소개
---
##### 네스티드(Nested) 클래스와 이너(Inner) 클래스
---
```java
class Outer {
  class Nested {...}
}
```
###### 네스티드 클래스의 구분
---
기본적으로 클래스 내에 정의되는 모든 클래스를 가리켜 '네스티드 클래스'라 하는데, 네스티드 클래스는 static의 선언 여부를 기준으로 다음과 같이 나뉜다.
- Static 네스티드 클래스
- Non-static 네스티드 클래스
이 중에서 Non-static 네스티드 클래스를 가리켜 '이너 클래스'라 한다. 이너 클래스는 정의되는 위치나 특성에 따라 다시 세 종류로 나뉜다.
- 멤버 이너 클래스
- 로컬 이너 클래스
- 익명 이너 클래스
'이너'를 생략하고 부르는 것이 일반적이다.

###### Stati 네스티드 클래스 (Static Nested Class)
---
- static 선언이 갖는 특성이 반영된 클래스
- 외부 클래스의 인스턴스와 상관없이(생성하지 않고도) Static 네스티드 클래스의 인스턴스 생성이 가능
- 외부의 static 멤버에 접근 가능 (private으로 선언되어 있어도 가능)
- Static 네스티드 클래스 내에서 외부 클래스의 인스턴스 멤버에 접근 불가능

###### 이너(Inner) 클래스의 구분
---
- 멤버 클래스: 인스턴스 멤버와 동일한 위치에 정의
- 로컬 클래스: 중괄호 내에, 특히 메소드 내에 정의
- 익명 클래스: 이름이 존재하지 않는 클래스

```java
class Outer {
  class MemberInner {...} // 멤버 클래스

  void method() {
    class LocalInner {...}  // 로컬 클래스
  }
}
```

###### 멤버 클래스
---
- 멤버 클래스의 인스턴스는 외부 클래스의 인스턴스에 종속적이다.
- 외부 클래스 인스턴스 없이 생성 불가능
- 한 외부 클래스의 인스턴스로부터 생성된 멤버 클래스는 그 외부 클래스의 인스턴스 공유

###### '멤버 클래스'를 언제 사용하는가?
---
> 클래스의 정의를 감추어야 할 때 유용하게 사용된다.

```java
interface Printable {
    void print();   
}

class Papers {
    private String con;

    public Papers(String s) {
        con = s;
    }

    public Printable getPrinter() { //Printable을 구현하는 인스턴스를 반환
        return new Printer(); // 멤버 클래스 인스턴스 생성 및 반환
    }

    // private선언이 되어있으므로 외부 클래스 내에서만 인스턴스 생성 가능
    private class Printer implements Printable {  // 멤버 클래스의 정의
        public void print() {
            System.out.println(con);
        }
    }
}

class UseMemberInner {
    public static void main(String[] args) {
        Papers p = new Papers("서류내용...");
        Printable prn = p.getPrinter(); // Printer 인스턴스를 참조하기 위해
        prn.print();
    }
}
```
getPrinter() 가 어떠한 인스턴스의 참조 값을 반환하는지 알지 못한다. 이러한 상황을 '클래스 정의가 감추어진 상황'이라 한다.

이렇게 클래스의 정의를 감추면, getPrinter()가 반환하는 인스턴스가 다른 클래스의 인스턴스로 변경되어도 Papers 클래스 외부 코드는 조금도 수정할 필요가 없게 된다.

이러한 방식으로 정의된 클래스의 예: 반복자

###### 로컬 클래스
---
> 멤버 클래스와 상당 부분 유사하다. 단 클래스의 정의 위치가 if문, while문 메소드 몸체와 가이 블록 안에 정의 된다.

```java
class Papers {
    private String con;
    public Papers(String s) { con = s; }

    public Printable getPrinter() {
        class Printer implements Printable {
            public void print() { System.out.println(con); }
        }
        
        return new Printer();
    }
}
```
이렇게 메소드 내에 클래스를 정의하면 해당 메소드 내에서만 인스턴스 생성이 가능하다. 어처피 메소드 내에서만 인스턴스 생성이 가능하므로 private 선언은 의미가 없다. 멤버 클래스보다도 클래스를 더 깊이, 특정 블록 안으로 감추는 효과가 있다.

###### 익명 클래스
---
```java
public Printable getPrinter() {
  // 인터페이스를 대상으로 인스턴스를 생성하고 있으므로 원래 문제가 있는 문장
  return new Printable() {  // 인터페이스를 구현하는 클래스의 정의를 덧붙이면 가능
    public void print() {
      System.out.println(con);
    }
  };
}
```

##### 람다(lambda)의 소개
---
###### 람다의 이해
---
```java
interface Printable { // 추상 메소드가 하나인 인터페이스
    void print(String s);
}

class Lambda3 {
    public static void main(String[] args) {
        Printable prn = (s) -> { System.out.println(s); };
        prn.print("What is Lambda?");
    }
}
```

###### 람다식의 인자 전달
---
`int n = 10;` 과 같이 변수를 선언하고 초기화 할 수 있다.

`void method(int n) {...}`일 때 위와 동일한 원리로 `method(10);`와 같이 인자를 전달하여 매개변수를 초기화할 수 있다.

마찬가지로 

`Printable prn = (s) -> { System.out.println(S); };` 와 같이 참조변수를 초기화할 수 있으니

`void method(Printable prn) {...}`일 때, `methoe((s)-> System.out.println(s));`과 같이 람다식을 메소드의 인자로 전달할 수도 있다.
```java
interface Printable {
    void print(String s);
}

class Lambda4 {
    public static void ShowString(Printable p, String s) {
        p.print(s);
    }

    public static void main(String[] args) {
        ShowString((s) -> { System.out.println(s); }, "What is Lambda?");
    }
}
```