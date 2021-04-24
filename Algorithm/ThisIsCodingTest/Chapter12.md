#### Chapter 12. 구현 문제

###### 8. 문자열 재정렬 (322pg)
**My Solution #1** - python
```python
if __name__ == '__main__':
    S = input()

    alpha_str = ""
    num_sum = 0

    for c in S:
        if c.isalpha():
            alpha_str += c
        else:
            num_sum += int(c)

    print("".join(sorted(alpha_str)) + str(num_sum))
```    
