#### [617_Merge_Two_Binary_Trees](https://leetcode.com/problems/merge-two-binary-trees/)
> 404pg


###### My Solution 1
```python
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None

        merged = TreeNode()

        if t1 and not t2:
            merged.val = t1.val
            merged.left = self.mergeTrees(t1.left, None)
            merged.right = self.mergeTrees(t1.right, None)
        elif not t1 and t2:
            merged.val = t2.val
            merged.left = self.mergeTrees(None, t2.left)
            merged.right = self.mergeTrees(None, t2.right)
        else:
            merged.val = t1.val + t2.val
            merged.left = self.mergeTrees(t1.left, t2.left)
            merged.right = self.mergeTrees(t1.right, t2.right)

        return merged
```

> Runtime: 100 ms, faster than 18.66% of Python3 online submissions for Merge Two Binary Trees.

> Memory Usage: 15.5 MB, less than 63.17% of Python3 online submissions for Merge Two Binary Trees.