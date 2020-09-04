#### I/O 스트림
---
##### I/O 스트림에 대한 이해
---
- `public abstract int read() throws IOException`: java.io.InputStream
- `public abstract void write(int b) throws IOException`: OutputStream

```java
OutputStream out = new FileOutputStream("data.dat");
out.write(7);
out.close();

InputStream in = new FileInputStream("data.dat");
int dat = in.read();
in.close();
```

###### 입출력 스트림 관련 코드의 개선
---
입력 및 출력 스트림의 생성 과정에서 예외가 발생하여 스트림의 생성에 실패하면 close 호출을 생략해야 한다. 그렇지 않으면 또 다른 예외가 발생할 수 있다.
```java
public static void main(STring[] args) throws IOException {
  OutputStream out = null;
  try {
    out = new FileOutputStream("data.dat");
    out.write(7);
  }
  finally {
    if(out != null) // 스트림 생성에 성공 했다면
      out.close();
  }
}
```

try-with-resources문 적용
```java
try(InputStream in = new FileInputStream("data.dat")) {
  int dat = in.read();
  System.out.println(dat);
}
catch(IOException e) {
  e.printStackTrace();
}
```

###### 바이트 단위 입력 및 출력 스트림
---
> 위 입출력 스트림은 '바이트'스트림이다

```java
try(InputStream in = new FileInputStream(src) ;
            OutputStream out = new FileOutputStream(dst)) {

  int data;
  while(true) {
      data = in.read();             
      if(data == -1)
          break;             
      out.write(data);
  }
}
````
read는 파일로부터 읽어 들인 1바이트의 유효한 데이터에 3바이트의 0을 채워서 4바이트의 int형 데이터로 반환한다. 스트림의 끝에 도달해서 더 이상 읽어 들일 데이터가 없는 경우 -1 반환한다. write는 전달되는 int형 데이터의 첫 번째 바이트만을 파일에 저장한다.

**속도의 개선**
```java
try(InputStream in = new FileInputStream(src) ;
            OutputStream out = new FileOutputStream(dst)) {
    byte buf[] = new byte[1024];
    int len;

    while(true) {
        len = in.read(buf);             
        if(len == -1)
            break;             
        out.write(buf, 0, len);
    }
}
```        
`public int read(byte[] b) throws IOException`
- 파일에 저장된 데이터를 b로 전달된 배열에 저장
- 읽어들인 바이트의 수를 반환
- 끝에 도달하면 -1 반환

`public void write(byte[] b, int off, int len) throws IOException`
- b로 전달된 배열의 데이터를 인덱스 off에서부터 len 바이트만큼 파일에 저장

##### 필터 스트림의 이해와 활용
---
###### 바이트 단위로 데이터를 읽고 쓸 줄은 알지만
---
- `DataInputStream`: 기본 자료형 데이터의 입력을 위한 필터 스트림
- `DataOutputStream`: 기본 자료형 데이터의 출력을 위한 필터 스트림

```java
try(DataOutputStream out = 
                 new DataOutputStream(new FileOutputStream("data.dat"))) {
    out.writeInt(370);
    out.writeDouble(3.14);
}
catch(IOException e) {
    e.printStackTrace();       
}
```
- `public final void writeInt(int v) throws IOException`
- `public final void writeDouble(double v) throws IOException`

```java
try(DataInputStream in = 
                 new DataInputStream(new FileInputStream("data.dat"))) {
    int num1 = in.readInt();
    double num2 = in.readDouble();

    System.out.println(num1);
    System.out.println(num2);
}
catch(IOException e) {
    e.printStackTrace();       
}
```     
- `public final int readInt() throws IOException`
- `public final double readDouble() throws IOException`

###### 버퍼링 기능을 제공하는 필터 스트림
- `BufferedInputStream`
- `BufferedOutputStream`

1바이트 단위로 데이터를 읽고 쓰지만 버퍼링 기능을 제공하는 필터 스트림을 사용
```java
try(BufferedInputStream in = 
                   new BufferedInputStream(new FileInputStream(src)) ;
            BufferedOutputStream out = 
                   new BufferedOutputStream(new FileOutputStream(dst))) {

    int data;
    while(true) {
        data = in.read();             
        if(data == -1)
            break;             
        out.write(data);
    }
}
catch(IOException e) {
    e.printStackTrace();       
}
```      
###### 버퍼링 기능에 대한 대책, flush 메소드의 호출
---
`public void flush() throws IOException`  

###### 파일에 기본 자료형 데이터를 저장하고 싶은데, 버퍼링 기능도 추가하면 좋겠다!
---
```java
try(DataOutputStream out = 
                 new DataOutputStream(
                     new BufferedOutputStream(
                         new FileOutputStream("data.dat")))) {
    out.writeInt(370);
    out.writeDouble(3.14);
}
catch(IOException e) {
    e.printStackTrace();       
}
```        
```java
try(DataInputStream in = 
                 new DataInputStream(
                     new BufferedInputStream(
                         new FileInputStream("data.dat")))) {
    int num1 = in.readInt();
    double num2 = in.readDouble();

    System.out.println(num1);
    System.out.println(num2);
}
catch(IOException e) {
    e.printStackTrace();       
}
```

##### 문자 스트림의 이해와 활용
---
###### 바이트 스트림과 문자 스트림의 차이
---
문자를 입출력할 때에는 약간의 데이터 수정이 필요하다. 영어와 특수문자는 1바이트, 한글은 2바이트 등 다르게 표현되어 있기 때문이다.
```java
try(Writer out = new FileWriter("data.txt")) {
  out.write('A');
  out.write('한');
}
catch(IOException e) {
  e.printStackTrace();
}
```

###### FileReader & FileWriter
---
- `FileInputStream` -> `InputStream`
- `FileOutputStream` -> `OutputStream`
- `FileReader` -> `Reader`
- `FileWriter` -> `Writer`

1. 문자만 저장되어 있는 파일을 복사하려고 한다. 이때 필요한 스트림은?
> 문자스트림을 통해서도 복사를 진행할 수 있다. 그러나 기본적으로 파일 복사는 파일의 내용에 상관없이 있는 그대로의 바이트 정보가 저장된 파일을 하나 더 만드는 일이다. 따라서 바이트 스트림을 생성해서 복사를 진행하는 것이 원칙이다.

2. 자바 프로그램에서 문자 하나를 파일에 저장했다가 다시 읽어 들이려 한다. 이때 필요한 스트림은?
> 이 경우 파일에 문자를 저장하는 주체도, 저장된 문자를 읽는 주체도 자바 프로그램이다. 따라서 문자를 유니코드로 저장하고 읽어 들이면 충분하므로 바이트 스트림을 생성하는 것이 옳다. 물론 문자 스트림을 생성해서 이 일을 처리할 수도 있다. 그러나 그 과정에서 불필요하게 문자의 인코딩을 변경하는 일만 생기게 된다.
3. 운영체제상에서 만든 텍스트 파일의 내용을 자바 프로그램에서 읽어서 출력하려 한다. 이때 필요한 스트림은?
> 운영체제상에서 만든 텍스트 파일은 메모장과 같은 프로그램을 실행해서 원하는 내용을 담은 파일을 의미한다. 그리고 이렇게 만들어진 파일에 저장된 문자들은 해당 운영체제의 기본 문자 인코딩 방식을 따른다. 따라서 이 문자들을 실행 중인 자바 프로그램에서 읽어 들이려면 유니코드로의 인코딩 변화가 필요하다. 그러므로 이 경우에는 문자 스트림을 생성해야 한다.

<br>

- read()의 반환형이 int인 이유는 반환할 문자가 없을 때 -1을 반환하기 위함이다. 따라서 문자를 출력할 때에는 char 형으로의 형 변환이 필요하다. 형 변환을 하지 않으면 int로 인식되어 정수가 출력된다.


###### BuferedReader & BufferedWriter
---
- `BufferedReader`
  - `public String readLine() throws IOException` : 문자열 반환, 반환할 문자열 없으면 null 반환
- `BufferedWriter`
  - `public void writer(String s, int off, int len)` : 문자열 s를 인덱스 off에서부터 len개의 문자까지 저장

```java
try(BufferedWriter bw = 
                new BufferedWriter(new FileWriter("String.txt"))) {   
    bw.write(ks, 0, ks.length());
    bw.newLine();   // 줄바꿈 -> 운영체제가 달라도 가능
    bw.write(es, 0, es.length()); 
}
catch(IOException e) {
    e.printStackTrace();       
}
```
```java
try(BufferedReader br = new BufferedReader(new FileReader("String.txt"))) {
    String str;

    while(true) {
        str = br.readLine();
        if(str == null)
            break;
        System.out.println(str);
    }
}
catch(IOException e) {
    e.printStackTrace();       
}
```

##### IO 스트림 기반의 인스턴스 저장
---
> 바이트 스트림을 통해서 인스턴스를 통째로 저장하고 꺼내는 것도 가능하다. 이렇듯 인스턴스를 통째로 저장하는 것을 가리켜 '객채 직렬화(Object Serialization)'라 하고, 역으로 저장된 인스턴스를 꺼내는 것을 가리켜 '객체 역 직렬화(Object deserialization)'이라 한다.

###### ObjectInputStream & ObjectOutputStream
---
- `ObjectInputStream` : 인스턴스를 입력하는 스트림
- `ObjectOutputStream` : 인스턴스를 출력하는 스트림
위 두 스트림은 사용방법이 필터 스트림과 유사하다. 하지만 필터 스트림이 상속하는 `FilterInputStream`, `FilterOutputStream` 을 상속하지 않으므로 필터스트림이 아니다.

입출력의 대상이 되는 인스턴스의 클래스는 `java.io.Serializable`(마커 인터페이스)을 구현해야 한다.

```java
try(ObjectOutputStream oo = 
                new ObjectOutputStream(new FileOutputStream("Object.bin"))) {
    oo.writeObject(box1);
    oo.writeObject(box2);
}
catch(IOException e) {
    e.printStackTrace();       
}
```
- `public final void writeObject(Object obj) throws IOException`
- 다양한 writeXXX 메소드가 정의되어 있어서 문자열 및 기본 자료형 데이터도 하나의 파일에 함께 담을 수 있다.

```java
try(ObjectInputStream oi = 
                new ObjectInputStream(new FileInputStream("Object.bin"))) {
    SBox box1 = (SBox) oi.readObject();
    System.out.println(box1.get());

    SBox box2 = (SBox) oi.readObject();
    System.out.println(box2.get());            
}
catch(ClassNotFoundException e) {
    e.printStackTrace();       
}
catch(IOException e) {
    e.printStackTrace();       
}
```   
- `public final Object readObject() throws IOException, ClassNotFoundException`
- 반환형이 Object이므로 명시적으로 형 변환을 진행할 필요가 있다.

인스턴스를 저장하면 인스턴스 변수가 참조하는 인스턴스까지 함께 저장되고 그러기 위해서는 참조되는 인스턴스도 `Serializable`을 구현하고 있어야 한다.

참조하는 인스턴스의 저장을 원치 않으면 다음과 같이 `transient`선언을 추가하면 된다.
```java
public class SBox implements java.io.Serializable {
    transient String s;
    ...
}
```
`transient`선언을 추가한 변수가 복원되었을 때 null(0) 으로 초기화 된다.