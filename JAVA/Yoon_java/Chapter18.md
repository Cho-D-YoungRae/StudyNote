#### 예외처리 (Exception Handling)
---
##### 자바 예외처리의 기본
---
###### 예외의 처리를 위한 try ~ catch
---
java.lang.ArithmeticException
- 수학 연산에서의 오류 상황을 의미하는 예외 클래스

java.util.InputMismatchException
- 클래스 Scanner를 통한 값의 입력에서의 오류 상황을 의미하는 예외 클래스

> 예외 상황별로 그 상황을 알리기 위한 '예외클래스'

> 오류가 발생하면 예외 클래스의 인스턴스 생성

```java
try {
  // 관찰 영역
}
catch(Exception name) {
  // 처리 영역
}
```
- try 영역에서 예외 상황이 만들어 지면 예외 클래스의 인스터스 생성
- catch 의 매개변수로 전달
- catch 안에서 무엇을 하든 상관없이 예외가 처리된 것으로 간주하고 실행을 이어 나간다.

###### 둘 이상의 예외를 처리하기 위한 구성
---
- 예외 수 만큼 catch 구문을 구성한다
- catch(ArithmeticException | InputMismatchException e)

###### Throwable 클래스와 예외처리의 책임 전가
---
**java.lang.Throwalb**
- 자바의 최상위 클래스인 java.lang.Object 를 제외하고 예외 클래스의 최상위 클래스
- 예외의 정보를 알 수 있는 대표적인 메소드
- - public String getMessage(): 예외의 원인을 담고 있는 문자열 반환
- - public void printStackTrace(): 예외가 발생한 위치와 호출된 메소드의 정보를 출력

> 메소드에서 예외가 발생하였는데 처리하지 않으면 그 메소드를 호출한 곳으로 예외처리의 책임을 넘긴다. 그 끝은 main 이다.

###### Exception을 상속하는 예외 클래스의 예외처리
---
- Error를 상속하거나 RuntimeException을 상속하는 예외의 발생은 코드 작성과정에서 특별히 무언가를 하지 않아도 된다.
- Exception을 상속하는 예외의 발생에 대해서는 try ~ catch문을 통해 예외를 처리하거나 throws 선언을 통해서 예외의 처리를 넘긴다는 표시를 꼭 해야한다.
- `public void simpleWrite() throws IOException, IndexOutofBoundsException {}`

###### 프로그래머가 정의하는 예외
---
```java
class ReadAgeException extends Exception { // Exception을 상속하는 것이 핵심
  public ReadAgedException() {
    super("Throwable클래스의 getMessage() 호출 시 반환될 문자열");
  }
}
```
- `throw new ReadAgeException();` 으로 예외 발생

###### 잘못된 catch 구문의 구성
```java
class FirstException extends Exception {...}
class SecendException extends FirstException {...}
class ThirdException extends SecondException {...}
```
위와 같이 정의되어 있을 때
```java
try{
  ...
}
catch(FirstException) {...}
catch(SecondException) {...}
catch(ThirdException) {...}
```
> 두 번째, 세 번째 catch 구문은 실행될 일이 절대 없다.

**아래와 같이 해야한다.**
```java
try{
  ...
}
catch(ThirdException) {...}
catch(SecondException) {...}
catch(FirstException) {...}
```

###### finally 구문
---
> try안으로 진입하면 반드시 실행이 되야하는 구문

```java
try {...}
catch(Exception name) {...}
finally {...}
```

try 안에서 `writer = Files.newBufferedWriter(file);` 실행되었을 때  `writer.close();` 등 반드시 실행되어하는 것을 위해

###### try-with-resources 구문
---
```java
try(BufferedWriter writer = Files.newBufferedWriter(file)) {...}
catch(IOException e) {...}
```
> java.lang.AutoCloseable 안에는 추상메소드 `void close() throws Exception`가 존재한다. 이를 구현하는 클래스가 사용될 수 있다.

