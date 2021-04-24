#### [543_Diameter_of_Binary_Tree](https://leetcode.com/problems/diameter-of-binary-tree/)
> 390pg

###### My Solution 1
```python
class Solution:
    result = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def diameter(node: TreeNode, depth: int) -> int:
            if not node:
                return 0

            # 왼쪽 깊이, 오른쪽 깊이
            lchild_d = diameter(node.left, depth + 1)
            rchild_d = diameter(node.right, depth + 1)

            # 최대 직경 갱신
            # max 내 맨 마지막은 뺴도 된다
            self.result = max(self.result,
                              lchild_d + rchild_d,
                              max(lchild_d, rchild_d) + depth)

            return max(lchild_d, rchild_d) + 1

        diameter(root, 0)
        return self.result
```
> Runtime: 40 ms, faster than 88.17% of Python3 online submissions for Diameter of Binary Tree.

> Memory Usage: 16.5 MB, less than 14.98% of Python3 online submissions for Diameter of Binary Tree.

###### 교재풀이 참조

