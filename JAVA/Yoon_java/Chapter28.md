#### 메소드 참조와 Optional
---
##### 메소드 참조 (Method References)
---
> '메소드 참조'라는 방법을 통해 메소드 정의는 람다식을 대신할 수 있다. 이를 통해 코드의 양을 줄일 수 있게 한다.
###### 메소드 참조의 4가지 유형과 메소드 참조의 장점
---
- static 메소드의 참조
- 참조변수를 통한 인스턴스 메소드 참조
- 클래스 이름을 통한 인스턴스 메소드 참조
- 생성자 참조

###### static 메소드의 참조
---
`ClassName::staticMethodName`

```java
Consumer<List<Integer>> c = l -> Collections.reverse(l);  //람다식
Consumer<List<Integer>> c = Collections::reverse; // 메소드 참조
```

###### 인스턴스 메소드의 참조 1: 인스턴스가 존재하는 상황에서 참조
---
`ReferenceName::instanceMethodName`
```java
class JustSort {
  public void sort(List<?> lst) {
    Collections.reverse(lst);
  }
}
```
일 때
```java
JustSort js = new JustSort();
Consumer<List<Integer>> c = e -> js.sort(e);  // 람다식 기반
Consumer<List<Integer>> c = e -> js::sort(e); // 메소드 참조 기반
```

람다식에서 같은 지역 내에 선언된 참조변수 js에 접근하고 있다. 코드만 보면 문제 없어 보이나 람다식이 인스턴스의 생성으로 이어진다는 사실을 고려하면 이는 다소 특이하다. 람다식에서 접근 가능한 참조변수는 final로 선언되었거나 effectively final이어야한다.


Collection<\E\> 인터페이스는 Iterable\<T\>를 상속하고 여기에는 다음 디폴트 메소드가 정의되어 있다.
```java
default void forEach(Consumer<? super T> action) {
  for(T t : this) // this는 이 메소드가 속한 컬렉션 인스턴스를 의미함
    action.accept(t);
}
```
###### 인스턴스 메소드의 참조 2: 인스턴스 없이 인스턴스 메소드 참조
---
`ClassName::instanceMethodName`
```java
ToIntBiFunction<IBox, IBox> bf = (b1, b2) -> b1.larger(b2);
ToIntBiFunction<IBox, IBox> bf = IBox::larger;
```
위의 람다식 기반을 보면 첫 번째 인자로 전달된 인스턴스의 메소드로 실행이 된 것을 알 수 있다. 이는 일종의 약속이다.

###### 생성자 참조
---
`ClassName::new`
```java
char src = {'R', 'o', 'b', 'o', 't'};

Function<char[], String> f = ar -> {
  return new String(ar);
};
Function<char[], String> f = ar -> new String(ar);
Function<char[], String> f = String::new;

String str = f.apply(src);
System.out.println(str);
```
Function\<char[], String\>이다. f는 String의 `public String(char[] value)`를 참조


##### Optional 클래스
---
> `NullPointerException` 예외처리를 단순히 처리할 수 있게 해준다.

###### Optional 클래스의 기본적인 사용 방법
> `java.util`
value에 인스턴스를 저장하는 일종의 래퍼 클래스이다.
```java
public final class Optional<T> extends Object {
  private final T value;
  ...
}
```java
import java.util.Optional;

class StringOptional1 {
    public static void main(String[] args) {
        // Null일 수 없다 -> 예외 발생
        Optional<String> os1 = Optional.of(new String("Toy1"));
        // Null일 수 있다. -> 비어있는 Optional 인스턴스 생성 가능
        Optional<String> os2 = Optional.ofNullable(new String("Toy2"));

        if(os1.isPresent())
            System.out.println(os1.get());

        if(os2.isPresent())
            System.out.println(os2.get());

        os1.ifPresent(s -> System.out.println(s));
        os2.ifPresent(System.out::println);          
    }
}
```

`public void ifPresent(Consumer<? super T> consumer)`

###### Optional 클래스를 사용하면 if ~ else문을 대신할 수 있다: map 메소드의 소개
---
```java
// Optional String -> optional_string
Optional<String> os3 = o1.map(s -> s.replace(' ','_'))
                          .map(s -> s.toLowerCase());
```                          
`public <U> Optional<U> map(Function<? super T, ? extends U> mapper)`
제네릭 클래스에 정의된 제네릭 메소드(T는 제네릭 클래스의 멤버임을 알려주고, U는 제네릭 메소드임을 알려준다.)

`Function<T, U>   U apply(T, t)`

Optional\<String\>의 인스턴스를 대상으로 호출하므로 T는 String map은 \<U\>에 대한 제네릭 메소드. map 메소드는 apply 메소드가 반환하는 대상을 Optional 인스턴스에 담아서 반환한다.

###### Optional 클래스를 사용하면 if ~ else문을 대신할 수 있다: orElse 메소드의 소개
---
```java
Optional<String> os1 = Optional.empty();
  Optional<String> os2 = Optional.of("So Basic");

  String s1 = os1.map(s -> s.toString())
                  .orElse("Empty");

  String s2 = os2.map(s -> s.toString())
                  .orElse("Empty");
```

###### Optional 클래스의 flatMap 메소드
---
> Optional 클래스를 코드 전반에 걸쳐 사용하기 위한 flatMap 메소드

```java
Optional<String> os2 = os1.map(s -> s.toUpperCase());
Optional<String> os3 = os1.flatmap(s -> Optional.of(s.toLowerCase()));
```
map은 람다식이 반환하는 내용물을 Optional 인스턴스로 감싸는 일을 알아서 해주지만, flatMap은 알아서 해 주지 않기 때문에 이 과정을 람다식이 포함하고 있어야 한다. flatMap은 Optional 인스턴스를 클래스의 멤버로 두는 경우에 유용하게 사용할 수 있다.
```java
//getphone은 Optional<String>을 반환
String phone = ci.flatMap(c -> c.getphone())
                  .orElse("There is no phone number.");
```                  

##### OptionalInt, OpionalLong, OptionalDouble 클래스
---
Optional 클래스보다 구체화된 클래스. map과 flatMap 메소드가 정의되어 있지 않다.