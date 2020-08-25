#### 콘솔 입력과 출력
##### 콘솔 출력 (Console Output)
###### System.out.println
> 참조 값이 전달되면, 이 값의 인스턴스를 대상으로 toString 메소드를 호출하고 반환되는 문자열을 출력한다.

##### 콘솔 입력 (Console Input)
###### Scanner 클래스
- Scanner(File source)
- Scanner(String source)
- Scanner(InputStream source)
- - `Scanner sc = new Scanner(System.in); // 키보드`

###### Scanner 클래스의 주요 메소드들
- int nextInt()
- byte nextByte()
- String nextLine()
- double nextDouble()
- boolean nextBoolean()
- ...