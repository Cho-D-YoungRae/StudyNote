#### 컬렉션 프레임워크 1
---
##### List<E> 인터페이스를 구현하는 컬렉션 클래스들
---
###### ArrayList<E> 클래스
---
`public ArrayList(int initialCapacity)`
> 인자로 전달된 수의 인스턴스를 저장할 수 있는 공간을 미리 확보

`public ArrayList()`
> 10개의 인스턴스를 저장할 수 있는 공간을 미리 확보

###### LinkedList<E> 클래스
---
###### 저장된 인스턴스의 순차적 접근 방법 1: enhanced for문의 사용
---
> List\<E\>는 enhanced for문을 사용할 수 있다. 이를 통해 순차적 접근의 대상이 되려면 
> `public interface Iterable\<T\>를 구현해야 한다

`public interface Collection\<E\> extends Iterable\<E\>`

###### 저장된 인스턴스의 순차적 접근 방법 2
---
`Iterator\<T\> iterator`
for-each문을 통한 순차적 접근과 달리 반복자를 이용하면 반복 중간에 특정 인스턴스를 삭제하는 것이 가능하다. (for-each는 불가능)
```java
while(itr.hasNext()) {  // itr은 반족자
  str = itr.next();
  if(str.equals("Box"))
    itr.remove(); // 위 next 메소드가 반환한 인스턴스 삭제
}
```

for each문도 컴파일 과정에서 다음과 같이 반복자를 이용하는 코드로 수정된다.

###### 배열보다는 컬렉션 인스턴스가 좋다.: 컬렉션 반환
---
`List<String> list = Arrays.asList("Toy", "Robot", "Box");`
- 인자로 전달된 인스턴스들을 저장한 컬렉션 인스턴스의 생성 및 반환
- 하지만 이를 통해 생선된 컬렉션 인스턴스는 새로운 인스턴스의 추가나 삭제가 불가능하다. 반복자의 생성은 가능하나 이를 통해서도 참조만 가능

```java
class ArrayList<E> {
  public ArrayList(Collection<? extends E> c) {...}
}
```
- 새로운 인스턴스의 추가나 삭제가 필요한 상황이라면 위 생성자를 통해서 인스턴스 생성
- 대다수의 컬렉션 클래스들은 다른 컬렉션 인스턴스를 인자로 전달받는 생성자를 가지고 있어서 , 다른 컬렉션 인스턴스에 저장된 데이터를 복사해서 새로운 컬렉션 인스턴스를 생성할 수 있다.
  
```java
List<String> list = Arrays.asList("Toy", "Box", "Robot");
list = new ArrayList<>(list);
list = new LinkedList<>(list);
```

###### 기본 자료형 데이터의 저장과 참조
---
> 컬렉션 인스턴스도 기본 자료형의 값은 저장하지 못하므로 래퍼클래스를 이용하자

###### 연결 리스트만 갖는 양방향 반복자
---
List\<E\>를 구현하는 클래스의 인스턴스들만 얻을 수 있다.
`public ListIterator<E> listIterator()`
Iterator\<E\>를 상속한다.

##### Set\<E\> 인터페이스를 구현하는 컬렉션 클래스들
---
###### Set<\E\>을 구현하는 클래스의 특성과 HashSet<\E\> 클래스
---
Set<\E\>인터페이스를 구현하는 제네릭 클래그의 특성
- 저장 순서가 유지되지 않는다.
- 데이터의 중복 저장을 허용하지 않는다.

Set<\E\>를 구현하는 대표 클래스 HashSet<\E\>

Object 클래스에 정의되어 있는 다음 두 메소드의 호출 결과를 근거로 인스턴스가 동일한지 판단
- `public boolean equals(Object obj)`
- `public int hashCode()`

위 메소드를 적절히 오버라이딩하여 HashSet 에서 같은 값으로 판단하게 만들 수 있다.

###### hashCode 메소드의 다양한 정의
---
클래스를 정의할 때마다 hashCode 메소드를 정의하는 것은 번거로우며 성능까지 고려하며 모든 클래스를 정의하는 것이 쉬운 일은 아니다.

`public static int hash(Object...values)`
> java.util.Objects에 정의된 메소드, 전달된 인자 기반의 해쉬 값 반환

> '가변 인자 선언' 되어있다. -> 전달되는 인자의 수를 메소드 호출 시마다 달리할 수 있다.

```java
@Override
public int hashCode() {
  return Objects.hash(model, color);
}
```

###### TreeSet\<E\> 클래스의 이해와 활용
---
- 트리를 기반으로 정렬된 상태가 유지되면서 인스턴스가 저장됨
- 오름차순을 기준으로 한다.
- 일반적으로 통용되는 것 말고는 다음 인터페이스의 구현을 통해서 크고 작음에 대한 기준을 정해주어야 한다
- `public interface Comparable\<T\>`
- - 이 인터페이스에 위치한 유일한 추상 메소드 `int compareTo(T o)`


Comparable 인터페이스와 제네릭 기반인 Comparable\<T\> 둘 다 추상 메소드의 정의 방법에는 차이가 없다.

###### 인스턴스의 비교 기준을 정의하는 Comparable\<T\> 인터페이스의 구현 기준
---
구현해야 할 추상 메소드 `int compareTo(T o)`
- o가 작으면 양의 정수 반환
- o가 크다면 음의 정수 반환
- o와 같다면 0 반환

###### Comparator\<T\> 인터페이스를 기반으로 TreeSet\<E\>의 정렬 기준 제시하기
---
> 일시적인 기준 변경으로 compareTo 메소드를 수정하는 것은 적절치 않다. 이런 상황을 고려하여 다음 인터페이스가 제공되고 있다.

`public interface Comparator<T>`
- int compare(T o1, T o2) 의 구현을 통해 정렬 기준을 결정할 수 있다.

위 인터페이스를 구현한 클래스의 인스턴스는 TreeSet\<E\>의 다음 생성자를 통해 전달할 수 있다. 

`public TreeSet(Comparator<? super E> comparator)`

**example**
```java
class Person implements Comparable<Person> {
  String name;
  int age;

  @Override
  public int compareTo(Person p){
    // 원래 비교 기준
  }
  ...
}

class PersonComparator implements Comparator<Person> {
  public int compare(Person p1, Person p2){
    // 새로운 비교 기준
  }
}
```
위와 같이 정의 되어 있을 때
```java
TreeSet<Person> tree = new TreeSet<>(new PersonComparator());
tree.add(new Person(...));
...
```

자바에서 제공하는 기본 클래스를 대상으로 정렬 기준을 바꿔야 하는 상황에서 Comparator\<T\>의 구현이 좋은 해결책이 된다.

```java
class StringComparator implements Comparator<String> {
  public int compare(String s1, String s2) {
    // 기존의 사전편찬 순서에서 길이 순서 등으로 기준 바꿀 때
  }
}
```

###### Queue\<E\> 인터페이스와 큐(Queue)의 구현
---
`Queue<String> que = new LinkedList<>();`

###### 스택(Stack)의 구현
---
`public class Stack<E> extends Vector<E>`
자바 초기에 정의된 클래스로써 지금은 호환성 유지를 위해 존재하는 클래스이다.

이를 대신할 수 있는 '덱(Deque)`. 다음 인터페이스를 정의하였다.
`public interface Deque<E> extends Queue<E>`

```java
Deque<String> deq1 = new ArrayDeque<>();  //배열 기반
Deque<String> deq2 = new LinkedList<>();  // 리스트 기반
```

LinkedList\<E\> 클래스는 다음 세 가지 인터페이스를 모두 구현 했으므로 대신할 수 있다.
> Deque\<E\>, List\<E\>, Queue\<E\>

##### Map\<K, V\> 인터페이스를 구현하는 컬렉션 클래스들
---
###### Key-Value 방식의 데이터 저장과 HashMap\<K, V\> 클래스
---
`HashMap<Integer, String> map = new HashMap<>();`

###### HashMap\<K, V\>의 순차적 접근 방법
---
HashMap\<K, V\> 클래스는 Iterable\<T\> 인터페이스를 구현하지 않으니 for-each문을 통해서, 혹은 '반복자'를 얻어서 순차적 접근을 진행할 수 없다. 대신 아래의 메소드가 존재한다.

`public Set<K> keySet()` : 여기에 모든 Key를 담아서 반환

###### TreeMap\<K, V\>의 순차적 접근 방법
---
- 오름차순으로 Key에 접근한다.
- Comparator\<T\> 인터페이스를 기반으로 정렬 기준을 바꿀 수 있다. (TreeSet\<T\>와 동일)

