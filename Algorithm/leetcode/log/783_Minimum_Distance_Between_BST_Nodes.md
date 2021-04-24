#### [783_Minimum_Distance_Between_BST_Nodes](https://leetcode.com/problems/minimum-distance-between-bst-nodes/)
> 435pg


###### My Solution 1
```python
class Solution:
    prev = None
    result = float('inf')

    def minDiffInBST(self, root: TreeNode) -> int:
        if root:
            self.minDiffInBST(root.left)
            if self.prev:
                self.result = min(self.result, root.val-self.prev)
            self.prev = root.val
            self.minDiffInBST(root.right)

            return self.result
```

> Runtime: 60 ms, faster than 5.32% of Python3 online submissions for Minimum Distance Between BST Nodes.

> Memory Usage: 14.3 MB, less than 33.33% of Python3 online submissions for Minimum Distance Between BST Nodes.

제일 처음에는 `result`값 갱신을 하지 않기 위해 `prev`에 `None`값으로 초기화 했다. `prev`를 `-float('inf')`으로 하면 `result` 값을 갱신할 때 제일 처음에는 어처피 무한대가 되므로 이렇게 하면 계속 `prev`가 `None`인지 확인하지 않아도 된다.