#### [1_Two_Sum](https://leetcode.com/problems/two-sum/)


###### My Solution 1

python
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 주어진 배열을 인덱스, 값 쌍으로 저장
        idx_val = list(enumerate(nums))
        # 값에 대하여 오른차순 정렬
        idx_val.sort(key = lambda x: x[1])

        # 투 포인터
        first, last = 0, len(nums)-1


        while first < last:
            # 두 값의 합
            sum_of_nums = idx_val[first][1] + idx_val[last][1]
            
            # 오름차순으로 정렬했으므로
            # 왼쪽 포인터 증가하면 합이 증가하고
            # 오른쪽 포인터 감소하면 값이 감소한다.
            if sum_of_nums > target:
                last -= 1
            elif sum_of_nums < target:
                first += 1
            else:
                break

        return [idx_val[first][0], idx_val[last][0]]
```        


---
교재 다른 풀이도 확인하자.