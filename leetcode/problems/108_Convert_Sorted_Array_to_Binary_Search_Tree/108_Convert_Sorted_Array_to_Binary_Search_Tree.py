from typing import *
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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