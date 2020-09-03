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

