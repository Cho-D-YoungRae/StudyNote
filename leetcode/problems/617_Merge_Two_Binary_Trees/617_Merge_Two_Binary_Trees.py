from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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