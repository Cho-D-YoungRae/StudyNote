#### [105_Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/submissions/)
> 444pg


###### My Solution 1

```python
class Solution:
    idx: int = 0

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        
        new_node = TreeNode(preorder[self.idx])
        divide_idx = inorder.index(preorder[self.idx])
        self.idx += 1
        new_node.left = self.buildTree(preorder, inorder[:divide_idx])
        new_node.right = self.buildTree(preorder, inorder[divide_idx+1:])

        return new_node
```

> Runtime: 180 ms, faster than 36.67% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.

> Memory Usage: 53.2 MB, less than 34.45% of Python3 online submissions for Construct Binary Tree from Preorder and Inorder Traversal.
