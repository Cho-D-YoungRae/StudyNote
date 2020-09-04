#### NIO 그리고 NIO.2
---
##### 파일 시스템
---
###### Paths와 Path 클래스
---
> java.nio.file.Path

절대경로
```java
Path pt1 = Paths.get("C:\\JavaStudy\\PathDemo.java");
Path pt2 = pt1.getRoot();
Path pt3 = pt1.getParent();
Path pt4 = pt1.getFileName();

System.out.println("Absolute: " + pt1);
System.out.println("Root: " + pt2);
System.out.println("Parent: " + pt3);
System.out.println("File: " + pt4);
``` 
상대 경로
```java
Path cur = Paths.get("");
String cdir;

if(cur.isAbsolute())  // 절대 경로인가?
    cdir = cur.toString();
else
    cdir = cur.toAbsolutePath().toString();
```            
###### 파일 및 디렉토리의 생성과 소멸
---
- `public static Path createFile(Path path, FileAttribute<?>...attrs) throws IOException`
  - 지정한 경로에 빈 파일 생성, 경로가 유효하지 않거나 파일이 존재하면 예외 발생
- `public static Path createDirectory(Path dir, FileAttribute<?>...attrs) throws IOException`
  - 지정한 경로에 디렉토리 생성, 경로가 유효하지 않으면 예외 발생
- `public static Path createDirectories(Path dir, FileAttuibute<?>...attrs) throws IOException`
  - 지정한 경로의 모든 디렉토리 생성

```java
Path fp = Paths.get("C:\\JavaStudy\\empty.txt");
fp = Files.createFile(fp);

Path dp1 = Paths.get("C:\\JavaStudy\\Empty");
dp1 = Files.createDirectory(dp1);

Path dp2 = Paths.get("C:\\JavaStudy2\\Empty");
dp2 = Files.createDirectories(dp2);
```

###### 파일을 대상으로 하는 간단한 입력 및 출력
---
입출력할 데이터의 양이 적고 성능이 문제 되지 않는 경우에 한해 사용해야 한다.

`java.nio.file.Files`
- `public static byte[] readAllBytes(Path path) throws IOException`
- `public static Path write(Path path, byte[] bytes, OpenOption...options) throws IOException`

```java
Path fp = Paths.get("C:\\JavaStudy\\simple.bin");
fp = Files.createFile(fp);

byte buf1[] = {0x13, 0x14, 0x15};

Files.write(fp, buf1, StandardOpenOption.APPEND);

byte buf2[] = Files.readAllBytes(fp);
```        
`StandardOpenOption`
- `APPEND` : 파일의 끝에 데이터를 추가한다.
- `CREATE` : 파일이 존재하지 않으면 생성한다.
- `CREATE_NEW` : 새 파일을 생성한다. 이미 파일이 존재하면 예외 발생
- `TRUNCATE_EXISTING` : 쓰기 위해 파일을 여는데 파일이 존재하면 파일의 내용을 덮어쓴다.
> 옵션을 하나도 전달하지 않으면 `CREATE`, `TRUNCATE_EXISTING`  기본으로

문자 데이터를 입력 및 출력하는 메소드 `java.nio.file.Files`
- `public static List<String> readAllLines(Path path) throws IOException`
- `public static Path write(Path path, Iterable<? extends CharSequence> lines, OpenOption...options) throws`

```java
Path fp = Paths.get("C:\\JavaStudy\\simple.txt");

String st1 = "One Simple String";
String st2 = "Two Simple String";
List<String> lst1 = Arrays.asList(st1, st2);

Files.write(fp, lst1);

List<String> lst2 = Files.readAllLines(fp);
```

###### 파일 및 디릭터리의 복사와 이동
---
파일뿐만 아니라 디렉토리를 대상으로도 가능하다.
- `public static Path copy(Path source, Path target, CopyOption...options) throws IOException`
- `public static Path move(Path sorce, Path target, CopyOption...options) throws IOException`

copy 메소드에 전달할 수 있는 옵션 두 가지
- `REPLACE_EXISTING`: 이미 파일이 존재한다면 해당 파일을 대체한다.
- `COPY_ATTRIBUTES` : 파일의 속성까지 복사를 한다.

##### NIO.2 기반의 I/O 스트림 생성
---
###### 바이트 스트림의 생성
---
이전에 보인 바이트 입력 스트림의 생성 방법
```java
InputStream in new FileInputStream("data.dat");
```
NIO.2의 방법
```java
Path fp = Paths.get("data.dat");
InputStream in = Files.newInputStream(fp);
```

```java
Path fp = Paths.get("data.dat");
try(DataOutputStream out = 
                 new DataOutputStream(Files.newOutputStream(fp))) {
    out.writeInt(370);
    out.writeDouble(3.14);
}
catch(IOException e) {
    e.printStackTrace();       
}
```
```java
Path fp = Paths.get("data.dat");
try(DataInputStream in = 
          new DataInputStream(Files.newInputStream(fp))) {
    int num1 = in.readInt();
    double num2 = in.readDouble();

    System.out.println(num1);
    System.out.println(num2);
}
catch(IOException e) {
    e.printStackTrace();       
}
```        

###### 문자 스트림의 생성
---
이전 방법
```java
BufferedWriter bw = new BufferedWriter(new FileWriter("String.txt"));
```
NIO.2의 방법
```java
Path fp = Paths.get("String.txt");
BufferedWriter bw = Files.newBufferedWriter(fp);
```
```java
try(BufferedWriter bw = Files.newBufferedWriter(fp)) {   
    bw.write(ks, 0, ks.length());
    bw.newLine();
    bw.write(es, 0, es.length()); 
}
catch(IOException e) {
    e.printStackTrace();       
}
```
```java
try(BufferedReader br = Files.newBufferedReader(fp)) {
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

##### NIO 기반의 입출력
---
###### NIO의 채널(Channel)과 버퍼(Buffer)
---
스트림은 입력, 출력이 구분되지만 채널은 하나로 읽고 쓰는 것이 가능하다. 채널은 반드시 버퍼에 연결해서 사용해야 한다.
```java
try(FileChannel ifc = 
        FileChannel.open(src, StandardOpenOption.READ); 
    FileChannel ofc = 
        FileChannel.open(dst, StandardOpenOption.WRITE, 
                              StandardOpenOption.CREATE)) {
    int num;

    while(true) {
        num = ifc.read(buf);    // 채널에서 버퍼로 읽어들임
        if(num == -1)
            break; 
        
        buf.flip();     // 버퍼에 저장된 데이터를 읽을 수 있는 상태로 변경
        ofc.write(buf);     // 버퍼에서 채널로 데이터 전송           
        buf.clear();    // 버퍼 지우기
    }
}
catch(IOException e) {
    e.printStackTrace();       
}
```        
버퍼에 저장된 데이터를 읽어 들였다고 해서 버퍼가 지워지는 것은 아니다. 때문에 다음 두 문장 중 하나를 실행해서 버퍼를 비우는 과정을 거쳐야 한다.
- `buf.clear()`
- `buf.compact()`

###### 성능 향상 포인트는 어디에?
---
이전에는 입력 스트림과 출력 스트림 각각에, 즉 두 개의 버퍼 스트림을 연결해야만 했다. 그리고 입력 버퍼에 저장된 데이터를 출력 버퍼로 이동하는 '버퍼 사이의 데이터 이동 과정'을 반드시 거쳐야 했다. 그러나 NIO 모델에서는 생략할 수 있다. 또 Direct 버펴를 생성할 수 있다.
```java
ByteBuffer buf = ByteBuffer.allocate(1024); // Non-Direct
ByteBuffer buf = ByteBuffer.allocateDirect(1024) // Direct
```
Direct 버퍼의 할당과 해제에 드는 시간적 비용이 Non-Direct에 비해 다소 높으므로 입출력할 파일의 크기가 크지 않거나 버퍼를 빈번히 할당하고 해제해야 하는 상황이라면 오히려 Non-direct 버퍼를 사용

###### 파일 랜덤 접근(File Random Access)
---
```java
try(FileChannel fc = FileChannel.open(fp, 
                        StandardOpenOption.CREATE, 
                        StandardOpenOption.READ, 
                        StandardOpenOption.WRITE)) {
    
    wb.flip(); 
    fc.write(wb);   

    ByteBuffer rb = ByteBuffer.allocate(1024);
    fc.position(0);
    fc.read(rb);
    
    rb.flip();
    rb.position(Integer.BYTES * 2);
} catch(IOException e) {
    e.printStackTrace();       
}
```