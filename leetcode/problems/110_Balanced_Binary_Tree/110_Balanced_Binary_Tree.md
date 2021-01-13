#### [110_Balanced_Binary_Tree](https://leetcode.com/problems/balanced-binary-tree/)
> 413pg


###### My Solution 1

```python
class Solution:
    result = True
    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                self.result = False

            return max(left, right) + 1

        dfs(root)
        return self.result
```

> Runtime: 52 ms, faster than 57.78% of Python3 online submissions for Balanced Binary Tree.

> Memory Usage: 19.1 MB, less than 41.90% of Python3 online submissions for Balanced Binary Tree.
