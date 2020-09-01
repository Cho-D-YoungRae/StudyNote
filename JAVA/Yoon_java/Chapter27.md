#### 람다 표현식
---
##### 람다와 함수형 인터페이스
---
###### 매개변수가 있고 반환하지 않는 람다식
---
줄임이 없는 람다식

`(String s) -> {System.out.println(s);}`

메소드의 몸체가 하나의 문장으로 이뤄져 있다면 중괄호 생략 가능

`(String s) -> System.out.println(S)` 중괄호 생략 시 세미콜론도 지운다.

매개변수 정보의 String은 컴파일러가 유추가능

`(s) -> System.out.println(S)`

매개변수가 하나일 경우에는 소괄호도 생략 가능

`s -> System.out.println(s)`

###### 매개변수가 있고 반환하는 람다식
---
메소드 몸체가 return문이면 문장이 하나여도 중괄호 생략 불가능

`(a, b) -> { return a + b; }`

아래와 같이 줄일 수 있다.
`(a, b) -> a + b`

메소드 몸체에 연산이 등장하는데, 이 연산이 진행되면 그 결과로 값이 남게 되고, 그러면 이 값은 별도로 명시하지 않아도 반환의 대상이 된다.

###### 매개변수가 없는 람다식
---
```java
Generator gen = () -> {
  Random ran = new Random();
  return rand.nextInt(50);
}
```
- 매개변수를 담는 소괄호가 비어있다.
- 둘 이상의 문장으로 이뤄져 있으면 중괄호로 반드시 감싸야 한다.
- 둘 이상의 문자으로 이뤄져 있으면 값을 반환할 때 return문 반드시 사용해야 한다.

###### 함수형 인터페이스(Functional Interfaces)와 어노테이션
---
람다식은 추상 메소드가 딱 하나만 존재하는 '함수형 인터페이스'를 기반으로 작성이 될 수 있다.
```java
@FunctionalInterface
interface Calculate {
  int cal(int a, int b);
}
```
@FunctionalInterface는 함수형 인터페이스에 부합하는지를 확인하기 위한 어노테이션 타입이다. 위 인터페이스에 둘 이상의 추상 메소드가 존재하면, 이는 함수형 인터페이스가 아니기 때문에 컴파일 오류로 이어진다. 그러나 static, default 선언이 붙은 메소드의 정의는 함수형 인터페이스의 정의에 아무런 영향을 미치지 않는다. 어처피 채워야할 메소드는 하나이기 때문이다.
```java
@FunctionalInterface
interface Calculate {
  int cal(int a, int b);
  default int add(int a, int b) { return a + b; }
  static int sub(int a, int b) { return a - b; }
}
```

###### 람다식과 제네릭
---
```java
@FunctionalInterface
interface Calculate <T> {
  T cal(T a, T b);
}
```
일 때
```java
Calculate<Integer> ci = (a, b) -> a + b;
Calculate<Double> cd = (a, b) -> a + b;
```
두 문장의 람다식은 동일하나 참조변수의 자료형이 다른 관계로 이 둘은 전혀 다른 인스턴스의 생성으로 이어진다.

##### 정의되어 있는 함수형 인터페이스
---
###### 미리 정의되어 있는 함수형 인터페이스
---
자바에서는 메소드의 반환형과 매개변수 선언에 차이를 둔 함수형 인터페이스들을 표준으로 정의하고 있다. 대표적으로 아래 네개가 java.util.function 패키지에 묶여있다.
|인터페이스|메소드|
|---|---|
|Predicate\<T\>|booleand test(T t)|
|Supplier\<T\>|T get()|
|Consumer\<T\>|void accept(T t)|
|Function\<T, R\>| R apply(T t)|

###### Predicate\<T\>
---
이 안에 다음 추상 메소드가 존재한다.

`boolean test(T t);`: 전달된 인자를 대상으로 true, false 판단

```java
import java.util.List;
import java.util.Arrays;
import java.util.function.Predicate;

class PredicateDemo {
    public static int sum(Predicate<Integer> p, List<Integer> lst) {
        int s = 0;
        
        for(int n : lst) {
            if(p.test(n))
                s += n;
        }       
        
        return s;
    }
    
    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(1, 5, 7, 9, 11, 12);
    
        int s;
        s = sum(n -> n%2 == 0, list);
        System.out.println("짝수 합: " + s);

    }
}
```

###### Predicate\<T\>를 구체화하고 다양화 한 인터페이스들
---
|인터페이스|메소드|
|---|---|
|IntPredicate|booleand test(int t)|
|LongPredicate|booleand test(Long t)|
|DoublePredicate|booleand test(double t)|
|BiPredicate\<T, U\>| booleand test(T t, U u)|

모두 마찬가지로 java.util.function으로 묶여있다. 위 세개는 함수형 인터페이스이지만 제네릭은 아니다. BiPredicate는 두 개의 인자를 받을 수 있다.

다른 표준으로 정의된 함수형 인터페이스들도 이와 같이 형제들이 각각 존재한다.

###### Supplier\<T\>
---
`T get();` : 단순히 무엇인가 반환할 때
```java
Supplier<Interger> spr = () -> {
  Random rand = new Random();
  return rand.nextInt(50);
};
```
난수를 반환 받을 수 있다.

###### Supplier\<T\>를 구체화 한 인터페이스들
---
|인터페이스|메소드|
|---|---|
|IntSupllier|int getAsInt()|
|LongSupplier|long getAsLong()|
|DoubleSupplier|double getAsDouble()|
|BooleanSupplier|boolean getAsBoolean()|

###### Consumer\<T\>
---
`void accept(T t);` : 전달된 인자 기반으로 '반환' 이외의 결과를 보일 때
```java
Consumer<String> c = s -> System.out.println(s);
```
출력이라는 결과를 보임

###### Consumer\<T\>를 구체화하고 다양화 한 인터페이스들
---
|인터페이스|메소드|
|---|---|
|IntConsumer|void accept(int value)|
|ObjConsumer\<T\>|void accept(T t, int value)|
|LongConsumer|void accept(long value)|
|ObjLongConsumer\<T\>|void accept(T t, long value)|
|DoubleConsumer|void accept(double value)|
|ObjDoubleConsumer|void accept(T t, double value)|
|BiConsumer\<T, U\>|void accept(T t, U u)|

###### Function\<T, R\>
---
`R apply(T t);` : 전달 인자와 반환 값이 모두 존재할 때
```java
Function<String, Integer> f = s -> s.length();
```

###### Function\<T, R\>
---
T와 R을 모두 기본 자료형으로 결정하여 정의한 인터페이스들
|||
|---|---|
|IntToDoubleFunction|double applyAsDouble(int value)|
|DoubleToIntFunction|int applyAsInt(double value)|
|...|...|
T와 R 자료형 일치
|||
|---|---|
|IntUnaryOperator|double applyAsInt(int operand)|
|DoubleUnaryOperator|int applyAsDouble(double operand)|
|...|...|
etc
|||
|---|---|
|BiFunction\<T, U, R\>|R apply(T t, U u)|
|IntFunction\<R\>|R apply(int value)|
|DoubleFunction\<R\>|R apply(double value)|
|ToIntFunction\<T\>|int applyAsInt(T value)|
|ToDoubleFunction\<T\>|double applyAsDouble(T value)|
|ToIntBiFunction\<T, U\>|int applyAsInt(T t, U u)|
|ToDoubleBiFunction\<T, U\>|double applyAsDouble(T t, U u)|

`UnaryOperator<T>`->`Function<T, R>` 상속

`BinaryOperator<T>`->`BiFunction<T, U, R>` 상속

T, R 또는 T, U, R 일치 할 때

###### removeIf 메소드를 사용해 보자.
---
Collection\<E\> 인터페이스에 다음 디폴트 메소드가 정의되어 있다.

`default boolean removeIf(Predicate<? super E> filter)`
```java
List<Integer> ls1 = Arrays.asList(1, -2, 3, -4, 5);
ls1 = new ArrayList<>(ls1);

List<Double> ls2 = Arrays.asList(-1.1, 2.2, 3.3, -4.4, 5.5);
ls2 = new ArrayList<>(ls2);

// <? super E> 로 되어있으므로 아래와 같이 가능하다
Predicate<Number> p = n -> n.doubleValue() < 0.0;
ls1.removeIf(p);
ls2.removeIf(p);
```

