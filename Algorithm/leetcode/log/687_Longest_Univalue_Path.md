#### [687_Longest_Univalue_Path](https://leetcode.com/problems/longest-univalue-path/)
> 393pg


###### My Solution 1
```python
class Solution:
    result = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node:
                return -1

            left = dfs(node.left) + 1
            right = dfs(node.right) + 1

            long_path = sum_path = 0

            if node.left and node.left.val == node.val:
                long_path = max(long_path, left)
                sum_path += left
            if node.right and node.right.val == node.val:
                long_path = max(long_path, right)
                sum_path += right

            self.result = max(self.result, sum_path)

            return long_path

        dfs(root)
        return self.result
```

> Runtime: 380 ms, faster than 76.83% of Python3 online submissions for Longest Univalue Path.

> Memory Usage: 18.1 MB, less than 19.91% of Python3 online submissions for Longest Univalue Path.