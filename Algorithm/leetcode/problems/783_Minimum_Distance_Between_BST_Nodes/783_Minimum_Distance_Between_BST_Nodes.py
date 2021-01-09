from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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