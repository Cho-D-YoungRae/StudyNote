#### NULL
---

**WHERE 에서**

IS NULL 로 NULL값인지 판단한다. = NULL 로 하면 안된다.
```SQL
SELECT ANIMAL_ID
    FROM ANIMAL_INS
    WHERE NAME IS NULL; -- IS NULL
```

**IFNULL()**

`IFNULL(널 값을 확인할 칼럼(널아니면 출력될 칼럼), 널 값일 경우 보여줄 대체 데이터 칼럼(혹은 값))`

```SQL
SELECT IDX , NAME , IFNULL(CPHONE,TEL) as CONTACT , ADDR
FROM TABLE;
```

WHERE 절에서 활용
```SQL
SELECT *
FROM TABLE_TEMP2
WHERE IFNULL(TOTAL_SAL,0) < 25000000
```