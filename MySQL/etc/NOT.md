#### NOT

`WHERE` 절에서 조건을 부정할 때 사용된다.

```SQL
SELECT user_num  ,  user_id , user_mobile , user_gender , user_amount  , user_addr  

FROM  User_Table

WHERE NOT user_id  IN ('user1','user3')

ORDER BY user_num DESC;
```

`IN`연산자 등으로 묶이지 않은 하나의 열이라면 굳이 `NOT`연산자를 사용하지 않고 `!=` 또는 `<>` 등의 연산자를 사용해도 된다.