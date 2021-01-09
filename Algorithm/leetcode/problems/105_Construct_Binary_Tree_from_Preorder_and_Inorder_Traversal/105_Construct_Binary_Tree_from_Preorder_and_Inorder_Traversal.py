from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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



