#### [104_Maximum_Depth_of_Binary_Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
> 387pg


###### My Solution 1

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        return max(self.maxDepth(root.left),
                   self.maxDepth(root.right)) + 1
```
> Runtime: 44 ms, faster than 41.85% of Python3 online submissions for Maximum Depth of Binary Tree.

> Memory Usage: 16.2 MB, less than 33.21% of Python3 online submissions for Maximum Depth of Binary Tree.

###### My Solution 2

```python
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = deque([root])

        result = 0
        while q:
            result += 1
            for i in range(len(q)):
                child = q.popleft()
                if child.left:
                    q.append(child.left)
                if child.right:
                    q.append(child.right)

        return result
```

> Runtime: 40 ms, faster than 72.69% of Python3 online submissions for Maximum Depth of Binary Tree.

> Memory Usage: 15.3 MB, less than 89.44% of Python3 online submissions for Maximum Depth of Binary Tree.
