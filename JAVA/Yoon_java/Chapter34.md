#### 쓰레드 그리고 동기화
---
##### 쓰레드의 이해와 쓰레드의 생성
---
###### 쓰레드의 이해와 쓰레드의 생성 방법
---
쓰레드는 실행 중인 프로그램 내에서 '또 다른 실행의 흐름을 형성하는 주체'를 의미한다.
```java
// 현재 메소드를 실행하는 쓰레드를 지칭하는 인스턴스의 참조를 얻는다
Thread ct = Thread.currentThread();
// 쓰레드의 이름
String name = ct.getName();
```

###### 쓰레드를 생성하는 방법
---
```java
Runnable task1 = () -> {...};
Runnable task2 = () -> {...};

Thread t1 = new Thread(task1);
Thread t2 = new Thread(task2);

t1.start();
t2.start();
```     

각각의 쓰레드는 독립적으로 실행된다.

쓰레드에 별도의 이름을 붙여주고 싶다면 다음 생성자를 사용한다

`public Thread(Runnable target, String name)`

`Runnable`은 `void Run()` 추상메소드 하나만 존재하는 함수형 인터페이스이다.

###### 쓰레드를 생성하는 두 번째 방법
---
```java
class Task extends Thread {
  public void run() {...} // 이 메소드를 오버라이딩 해야한다.
}
```
Thread를 상속하는 클래스 정의한 후
```java
Task t1 = new Task();
t1.start();
```

##### 쓰레드의 동기화
---
###### 쓰레드의 메모리 접근 방식과 그에 따른 문제점
---
> 둘 이상의 쓰레드가 동일한 변수에 접근하는 것은 문제를 일으킬 수 있다. 문제가 발생하지 않으려면 '동기화'를 해야 한다.

###### 동일한 메모리 공간에 접근하는 것이 왜 문제가 되는가?
---
> 쓰레드는 변수 num에 저장된 값 99를 가져다 코어의 도움을 받아서 100으로 만드는 과정을 거친 후 이 값을 변수 num에 가져다 놓는다. 두 개의 쓰레드가 동시에 진행할 경우 시차를 두고 가져갈 수도 있지만 여러 개가 동시에 가져가는 것도 가능한 상황이므로 문제가 발생할 수 있다. 한 순간에 한 쓰레드만 변수에 접근하도록 제한하면 문제는 해결된다.

###### 동기화(Synchronization) 메소드
---
메소드에 `synchronization`선언을 추가하면 동기화가 이뤄진다. 아래 선언을 하면 한 순간에 한 쓰레드의 접근만을 허용하게 된다.
```java
synchronized public void increment() {...}
```

###### 동기화(Synchronization) 블록
---
'동기화 메소드'기반의 동기화는 메소드 전체에 동기화를 걸어야 한다는 단점이 있다. 동기화가 불필요한 부분을 실행하는 동안에도 다른 쓰레드의 접근을 막는 일이 발생하게 된다. 이러한 경우 '동기화 블록'을 통해 문장 단위로 동기화 선언을 하는 것이 효율적이다.
```java
public void increment() {
  synchronized(this) {  // 동기화 블록
    count++;
  }
  System.out.println("카운터의 값이 1 증가하였습니다.");
}
```

##### 쓰레드를 생성하는 더 좋은 방법
---
> java.util.concurrent


###### 지금 소개하는 이 방법으로 쓰레드를 생성하고 활용하자.
---
쓰레드의 생성과 소멸은 시스템에 부담을 주고 따라서 처리해야 할 일이 있을 때마다 쓰레드를 생성하는 것은 성능의 저하로 이어질 수 있다. 그래서 쓰레드 풀을 이용해 제한된 수의 쓰레드를 생성해두고 이를 재활용 하는 기술을 사용한다.
```java
import java.util.concurrent.Executors;
import java.util.concurrent.ExecutorService;
```
```java
Runnable task = () -> { ... };

ExecutorService exr = Executors.newSingleTreadExecutor();
exr.submit(task);  // 쓰레드 풀에 작업을 전달

exr.shutdown(); // 쓰레드 풀과 그 안에 있는 쓰레드의 소멸
```
submit메소드 호출을 통해 작업을 전달하면, 풀에서 대기하고 있던 쓰레드가 이 일을 실행하게 된다. 그리고 작업이 끝나면 해당 쓰레드는 다시 쓰레드풀로 돌아가서 다음 작업이 전달되기를 기다리게 된다.

다음 메소드들을 통해서 다양한 유형의 쓰레드 풀을 생성할 수 있다.
- `newSingleThreadExecutor` : 풀 안에 하나의 쓰레드만 생성하고 유지한다.
- `newFixedThreadPool` : 풀 안에 인자로 전달된 수의 쓰레드를 생성하고 유지한다.
- `newCachedThreadPool` : 풀 안의 쓰레드의 수를 작업의 수에 맞게 유동적으로 관리한다.

###### Callable & Future
---
Runnable 의 run 메소드는 반환형이 void 였다. 다음 인터페이스를 기반으로 작업하면 작업의 끝에서 값을 반환하는 것이 가능하다.
```java
@FunctionalInterface
public interface Callable<V> {
  V call() throws Exception;
}
```
```java
Callable<Integer> task = () -> {...};
ExecutorService exr = Executors.newSingleThreadExecutor();

Future<Integer> fur = exr.submit(task); // Callable과 타입 인자 일치

Integer r = fur.get();  // 쓰레드의 반환 값 획득
System.out.println("result: " + r);
exr.shutdown();
```

###### synchronized를 대신하는 ReentrantLock
---
```java
class MyClass {
  ReentrantLock criticObj = new ReentrantLock();
  void myMethod(int arg) {
    criticObj.lock(); // 문을 잠근다
    try{
      // 한 쓰레드에 의해서만 실행되는 영역
    } finally {
      criticObj.unlock(); // 문을 연다.
    }
  }
}
```
unlock메소드를 호출하지 않는 코드상의 실수가 발생할 수 있기 때문에 위와 같이 작성하는 것이 안정적이다.

`.awaitTermination(100, TimeUnit)`
- 쓰레드 풀에 전달된 작업이 끝나기를 100초간 기다린다.

###### 컬렉션 인스턴스 동기화
---
Collections의 다음 메소드들을 통해 동기화 할 수 있다.
- `public static <T> Set<T> synchronizedSet(Set<T> s)`
- `public static <T> List<T> synchronizedList(List<T> list)`
- `public static <K, V> Map <K, V> synchronizedMap(Map<K, V> m)`
- `public static <T> Collection<T> sychronizedCollection(Collection<T> c)`