#### 시각과 날짜의 처리
---
##### 시각과 날짜 관련 코드의 작성
---
###### 시간이 얼마나 걸렸지? : Instant 클래스
---
- `java.time.Instant`
- `java.time.Duration`
```java
Instant start = Instant.now();

// 1970-01-01 00:00:00 기준 경과시간 초단위
System.out.println("시작: " + start.getEpochSecond());

Instant end = Instant.now();

// 보다 높은 정밀도로 시간차 측정
Duration between = Duration.between(start, end);
System.out.println("밀리 초 단위 차:" + between.toMillis());
```

###### 오늘이 며칠이죠? : LocalDate 클래스
---
- `java.time.LocalDate`
```java
LocalDate today = LocalDate.now();
// 2020-09-03 형태로
System.out.println("Today: " + today);

// public static LocalDate of(int year, int month, int dayOfMonth)
LocalDate xmas = LocalDate.of(today.getYear(), 12, 25);

LocalDate eve = xmas.minusDays(1);

Period left = Period.between(today, xmas);
System.out.println("xmas까지 앞으로 " +
                  left.getMonths() + "월 " + left.getDays() + "일");
```

###### 3시간 10분 뒤에 어때? : LocalTime 클래스
---
> `java.time.LocalTime`

```java
LocalTime now = LocalTime.now();
// 22:39:45:13.363 -> 시:분:초(밀리 초 까지)
System.out.println(now);

// public LocalTime plusHours(long hoursToAdd)
LocalTime mt = now.plusHours(2);
mt = mt.plusSeconds(10);

// 시, 분, 초
LocalTime start = Local.of(14, 24, 35);
LocalTime end = Local.of(17, 31, 19);

Duration between = Duration.between(start, end);

// PT3H6M44S 로 출력. 3시간 6분 44초가 지남을 의미
System.out.println(between);
```

###### 지금으로부터 22시간 35분 뒤의 시각과 날짜는? : LocalDateTime 클래스
---
```java
LocalDateTime dt = LocalDateTime.now();
dt = dt.plusMonths(2);
dt = dt.plusMinutes(30);

// 다양하게 오버로딩 되어있다.
LocalDateTime tomorrow = LocalDateTime.of(2020, 09, 04, 22, 56);

if(dt.isBefore(tomorrow)){
  ...
}

Period day = Period.between(dt.toLocalDate(), tomorrow.toLocalDate());
Duration time = Duration.between(dt.toLocalTime(), tomorrow.toLocalTime());
```

##### 시간대를 적용한 코드 작성 그리고 출력 포맷의 지정
---
###### 시간대를 표현하는 ZoneId 클래스
---
```java
ZoneId paris = ZoneId.of("Europe/Paris");
```
###### 시간대를 반영한 ZonedDateTime 클래스
---
```java
ZonedDateTime here = ZoneDateTime.now();
// 년 월 일 시 분 초 [ZoneId]
System.out.println(here);

ZonedDateTime paris = ZonedDateTime.of(
                        here.toLocalDateTime(), ZoneId.of("Europe/Paris"));

Duration diff = Duration.between(here, paris);
```

###### 날짜와 시각 정보의 출력 포맷 지정
---
> `java.time.format.DateTimeFormatter`

`public String format(DateTimeFormatter formatter)` 메소드를 호출하여 포맷에 맞게 문자열로 구성된 날짜와 시각정보 반환. LocalDate, LocalTime, LocalDateTime, ZonedDateTime 클래스에 모두 정의되어 있다.
```java
ZonedDateTime date = ZonedDateTime.of(
  LocalDateTime.of(2019, 4, 25, 11, 20), ZoneId.of("Asia/Seoul"));

  DateTimeFormatter fm1 = 
              DateTimeFormatter.ofPattern("yy-M-d");
  DateTimeFormatter fm2 = 
              DateTimeFormatter.ofPattern("yyyy-MM-d, H:m:s");
  DateTimeFormatter fm3 = // VV는 시간대ID의 출력을 의미
              DateTimeFormatter.ofPattern("yyyy-MM-dd, HH:mm:ss  VV");

  System.out.println(date.format(fm1));
  System.out.println(date.format(fm2));
  System.out.println(date.format(fm3));