from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root:
            self.rangeSumBST(root.left, low, high)
            self.rangeSumBST(root.right, low, high)
            if low <= root.val <= high:
                self.result += root.val

            return self.result