#### [938_Range_Sum_of_BST](https://leetcode.com/problems/range-sum-of-bst/)


###### My Solution 1
```python
class Solution:
    result = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root:
            self.rangeSumBST(root.left, low, high)
            self.rangeSumBST(root.right, low, high)
            if low <= root.val <= high:
                self.result += root.val

            return self.result
```

> Runtime: 268 ms, faster than 24.59% of Python3 online submissions for Range Sum of BST.

> Memory Usage: 22.3 MB, less than 9.16% of Python3 online submissions for Range Sum of BST.

> 모든 노드를 다 돌아야 한다.


###### 교재 풀이 확인