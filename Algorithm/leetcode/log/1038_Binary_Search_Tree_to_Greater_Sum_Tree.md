#### [1038_Binary_Search_Tree_to_Greater_Sum_Tree](https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/)
> 428pg


###### My Solution1
```python
class Solution: 
    s = 0
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        self.bstToGst(root.right)
        self.s += root.val
        root.val = self.s
        self.bstToGst(root.left)
        
        return root
```

> Runtime: 32 ms, faster than 61.28% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.

> Memory Usage: 14.3 MB, less than 51.79% of Python3 online submissions for Binary Search Tree to Greater Sum Tree.