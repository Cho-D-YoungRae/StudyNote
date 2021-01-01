from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
