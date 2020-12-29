from typing import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    result = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def diameter(node: TreeNode, depth: int) -> int:
            if not node:
                return 0

            lchild_d = diameter(node.left, depth + 1)
            rchild_d = diameter(node.right, depth + 1)

            self.result = max(self.result,
                              lchild_d + rchild_d,
                              max(lchild_d, rchild_d) + depth)

            return max(lchild_d, rchild_d) + 1

        diameter(root, 0)
        return self.result
