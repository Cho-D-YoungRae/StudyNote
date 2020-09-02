#### 스트림 1
---
##### 스트림의 이해와 스트림의 생성
---
###### 스트림의 이해
---
```java
int[] ar = {1, 2, 3, 4, 5};
IntStream stm1 = Arrays.stream(ar); // ar로부터 스트림 생성
IntStream stm2 = stm1.filter(n -> n % 2 == 1);  // 중간 연산
int sum = stm2.sum();
```

###### 스트림의 특성
---
실제로는 아래 방식으로 작성한다.
```java
int sum = Arrays.stream(ar)
                .filter(n -> n % 2 == 1)
                .sum();
```
`public static IntStream stream(int[] array)`

`Intstream filter(IntPredicate predicate)`

스트림의 연산은 효율과 성능을 고려하여 '지연(Lazy) 처리'방식으로 동작한다. 메소드 호출이 filter에서 sum으로 이어지지만, 정장 sum이 호출될 때까지 filter의 호출 결과는 스트림에 반영되지 않는다. 즉 최종 연산인 sum이 호출되어야 filter의 호출 결과가 스트림에 반영되고, 이어서 sum의 호출결과가 스트림에 반영된다. 최종 연산이 생략되면 중간 연산을 진행 했다 하더라도 결과가 보이지 않는다.

###### 스트림 생성하기: 배열
---
`public static <T> Stream<T> stream(T[] array)`: Arrays클래스에 정의

```java
String[] names = {"Yoon", "Lee", "Park"};
Stream<String> stm = Arrays.stream(names);  // 스트림 생성
stm.foreach(s -> System.out.println(s));  // 최종 연산
```
위의 forEach메소드는 Iterable\<T\>에 정의되어 있는 디폴트 메소드였던 forEach 메소드와 존재하는 위치가 다르다. 하지만 기능은 동일하고 매개변수 형이 Consumer\<T\> 이다. 위 처럼 중간 연산 없이 최종 연산을 진행할 수도 있다.

기본 자료형의 값을 담고 있는 배열을 대상으로 하는 스트림
- `public static IntStream stream(int[] array)`
- `public static IntStream stream(int[] array, int startInclusive, int endExclusive)`
- - 배열의 일부분을 대상으로
- 다른 기본 자료형 값도 있다..

###### 스트림 생성하기: 컬렉션 인스턴스
---
java.util.Collection\<E\>에 디폴트 메소드로 다음과 같이 정의되어있다.

`default Stream<E> stream()`

##### 필터링(Filtering)과 맵핑(Mapping)
---
###### 필터링(Filtering)
---
`Stream<T> filter(Predicate<? super T> predicate)`

###### 맵핑(Mapping) `
---
`<R> Stream<R> map(Function<? super T, ? extends R> mapper)`
```java
List<String> ls = Arrays.asList("Box", "Robot", "Simple");

ls.stream()
  .map(s -> s.length())
  .forEach(n -> System.out.print(n -> System.out.print(n + "\t")));
```
> 3 5 6

위 예제는 잘 작동하지만 map의 인자로 `R apply(T t)`에 대한 람다식을 전달하기 때문에 정수의 반환 과정에서 오토 박싱이 진행된다. 기본 자료형의 값을 반환하는 경우를 고려하여 다음 맵핑 관련 메소드들도 제공하고 있다.
- `IntStream mapToInt(ToIntFunction<? super T> mapper)`
- `LongStream mapToLong(ToLongFunction<? super T> mapper)`
- `DoubleStream mapToDouble(ToDoubleFunction<? super T> mapper)`

###### 맵핑(Mapping) 2
---
> 필터링, 맵핑 같이 할 수 있다.

##### 리덕션(Reduction), 병렬 스트림(Parallel Streams)
---
###### 리덕션과 reduce 메소드
---
`T reduce(T identity, BinaryOperator<T> accumulator)`

`BinaryOperator<T>  T apply(T t1, T t2)`

- reduce 호출 시 내부적으로 apply를 실행한다. d1, d2, d3, d4 가 있을 때, d1과 d2를 인자로 전달하여 r1을 얻고 r1과 d3을 절달하여 r2를 얻는다. 마지막으로 r2와 d4를 전달하여 r3을 얻는 식으로 줄여 나간다.
- identity는 스트림이 빈 경우에 반환을 한다. 비어 있지 않은 경우에는 이를 첫 번째 데이터로 간주하고 리덕션을 진행한다.

###### 병렬 스트림(Parallel Streams)
---
> 하나의 작업을 둘 이상의 작업으로 나누어서 동시에 진행하는 것

```java
String str = ls.parallelStream()
                .reduce("", lc);
                // lc는 BinaryOperator
```

이전과 다르게 parellelStream을 호출한다.

병렬처리의 핵심은 연산의 횟수를 줄이는데 있지 않고 연산의 단계를 줄이는데 있다.