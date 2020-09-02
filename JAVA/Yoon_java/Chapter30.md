#### 스트림 2
---
##### 스트림의 생성과 연결
---
###### 스트림의 생성과 연결
---
Stream\<T\> 인터페이스에 정의되어 있는 static 메소드
- `static <T> Stream<T> of(T t)`
- `static <T> Stream<T> off(T...values)`

###### DoubleStream, IntStream, LongStream
---
위 스트림과 같이 인터페이스와 같이 정의되어있다.

다음 메소드들을 통해서 범위 내에 있는 값들로 스트림을 구성할 수도 있다.
- `static IntStream range(int startInclusive, int endExclusive)`
- `static IntStream rangeClosed(int startInclusive, int endInclusive)`
- - endInclusive를 포함

```java
IntStream is3 = IntStream.range(5, 8);
```

###### 병렬 스트림으로 변경
---
이미 스트림을 생성한 상태에서 이를 기반으로 병렬 스트림을 생성하기를 원한다면 다음 메소드를 호출하면 된다.
- `Stream<T> parallel()`
- `IntStream parallel()`
- ....

###### 스트림의 연결
---
- `static <T> Stream<T> concat(Stream<? extends T> a, Stream<? extends T> b)`
- `IntStrean concat(IntStream a, IntStream b)`
- ....

##### 스트림의 중간 연산
---
- `<R> Stream<R> map(Function<T, R> mapper)`
- 기본 연산자에 대해....
- `<R> Stream<R> flatMap(Function<? super T, ? extends Stream<? extends R>> mapper)`
- 기본 연산자에 대해...

flatMap에 전달할 람다식 에서는 '스트림을 생성하고 이를 반환'해야한다. 반면 map에 전달할 람다식에서는 스트림을 구성할 데이터만 반환하면 되기 때문에 위와 같이 정의되어 있다.

map은 일 대 일 로 매핑을 진행하였지만 flatMap은 일대 다의 매핑을 진행할 수 있다.

###### 정렬
---
- `Stream<T> sorted(comParator<? super T> comparator)`
- `Stream<T> sorted()`
- `IntStream sorted()`
- ...

###### 루핑
---
스트림을 이루는 모든 데이터 각각을 대상으로 특정 연산을 진행하는 행위를 '루핑'이라 한다. 대표적은 루핑으로는 forEach가 있다. 그러나 이는 '최종 연산'이다. 반면 '중간 연산'에도 루핑을 위한 메소드 들이 존재한다.
- `Stream peek(Consumer<? super T> action)`
- `IntStream peek(IntConsumer action)`
- ...

최종 연산을 해야 중간 연산이 실행 된다.

##### 스트림의 최종 연산
---
###### sum(), count(), average(), min(), max()
---
IntStream의 메소드들
- `int sum()`
- `long count()`
- `OptionalDouble average()`
- `OptionalInt min()`
- `OptionalInt max()`

DoubleStream의 메소드들

...

###### forEach
---

###### allMatch, anyMatch, noneMatch
---
Stream\<T\>의 메소드들
- `boolean allMatch(Predicate<? super T> predicate)`: 모두 만족?
- `boolean anyMatch(Predicate<? super T> predicate)`: 하나라도 만족?
- `boolean noneMatch(Predicate<? super T> predicate)`: 하나도 만족 안 함?

IntStream의 메소드들

...

###### collect
---
> 저장을 위한

- `<R> R collect(Supplier<R> supplier, Biconsumer<R, ? super T> accumulator, BiConsumer<R, R> combiner)`
- `<R> R collect(Supplier<R> supplier, ObjIntconsumer<R, ? super T> accumulator, BiConsumer<R, R> combiner)`
- ...

```java
String[] words = {"Hello", "Box", "Robot", "Toy"};
Stream<String> ss = Arrays.stream(words);

List<String> ls = ss.filter(s -> s.length() < 5)
                    .collect(() -> new ArrayList<>(),
                              (c, s) -> c.add(s),
                              (lst1, lst2) -> lst1.addAll(lst2));
```
- `() -> new ArrayList<>()` 를 기반으로 데이터를 저장할 저장소 생성
- `(c, s) -> c.add(s)` c는 위를 통해서 생성된 컬렉션 인스턴스이고, s는 스트림을 이루는 데이터들이다.
- `(lst1, lst2) -> lst1.addAll(lst2))` 병렬 스트림이 아닌 순차스트림의 경우 세 번째 인자는 사용되지 않지만 null을 전달하면 예외가 발생한다.