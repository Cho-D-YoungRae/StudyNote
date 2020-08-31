#### 컬렉션 프레임워크 2
---
##### 컬렉션 기반 알고리즘
---
###### 정렬
---
List\<E\>를 구현한 컬렉션 클래스들 정렬을 위한 메소드. Collections 클래스에 정의되어 있는 제네릭 메소드이다.
`public static <T extends Comparable<T>> void sort(List<T> list)`
- 메소드 호출 시점에 T가 결정되므로 List\<T\>의 인스턴스는 모두 전달 가능
- T는 Comparable\<T\> 인터페이스를 구현한 상태이어야 한다.

###### \<T extends Comparable\<T\>\> 아니고 \<T extends Comparable\<? super T\>\>
---
`public static <T extends Comparable<? super T>> void sort(List<T> list)`
- Comparable\<T\>가 아닌 Comparable\<? super T\>인 이유는?

```java
class Car implements Comparable<Car> {...}
class ECar extends Car {...}
```
위와 같을 때 ECar는 Comparable\<Car\>를 간접 구현하는 상태가 된다. 이 때 \<T extends Comparable\<T\>\> 라면 'T는 ECar로 결정'되고 그렇다면 ECar는 Comparable\<Ecar\>를 구현해야하므로 sort메소드 호출에 문제가 생긴다. 위 상황을 고려하여 \<T extends Comparable\<? super T\>\> 이와 같이 정의 되었고 ECar 클래스는 Comparable\<Object\>, Comparable\<Car\>, Comparable\<Ecar\> 이 셋 인터페이스 중 하나만 구현해도 sort 메소드 호출은 성공한다.

###### 정렬: Comparator\<T\> 기반
---
> 정렬의 기준을 결정할 수 있다.

`public static <T> void sort(List<T> list, Comparator<? super T> c)`

위와 같은 이유로 
`class CarComp implements Comparator<Car>` 를 통해서 ECar도 정렬할 수 있다.

###### 찾기
---
리스트를 기반으로 탐색할 때 사용할 수 있는 Collections클래스의 다음 메소드

`public static <T> int binarySearch(List<? extends Comparable<? super T>> list, T key)`
> list에서 key를 찾아 그 인덱스 값 반환, 못찾으면 음의 정수 반환

- 첫 번째 인자로 List\<E\> 인스턴스는 무엇이든 올 수 있다.
- E는 Comparable\<T\>를 구현해야 한다.
- 위와 같은 이유로 \<? super T\>

###### 찾기: Comparator\<T\> 기반
---
`public static <T> int binarySearch(List<? extends T> list, T key, Comparator<? super T> c)`
- List\<? extends T\>는 T형 인스턴스를 꺼내는 것만 허용하기 위해
- Comparator\<? super T\>인 이유는 위와 같다.

###### 복사하기
---
`public static <T> void copy(List<? super T> dest, List<? extends T> src)`
- List\<? super T\> 는 dest에 T형 인스턴스를 넣는 것만 허용하기 위해
- List\<? extends T\> 는 src로부터 T형 인스턴스 꺼내는 것만 허용하기 위해
- dest에 전달되는 컬렉션 인스턴스의 저장 공간이 src에 전달되는 것보다 크거나 같아야한다.