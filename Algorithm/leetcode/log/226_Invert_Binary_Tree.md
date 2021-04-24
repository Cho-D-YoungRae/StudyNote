#### [226_Invert_Binary_Tree](https://leetcode.com/problems/invert-binary-tree/)
> 397pg


###### My Solution 1
```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
```

> Runtime: 32 ms, faster than 57.09% of Python3 online submissions for Invert Binary Tree.

> Memory Usage: 14.2 MB, less than 60.10% of Python3 online submissions for Invert Binary Tree.

###### 오답 -> 교재 참조함

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        # 고쳐야할 부분
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(root.left)

        return root
```

위와 같이 쓰면 왼쪽 자식 먼저 계산되고 그 다음 오른쪽 자식을 계산하는데 계산이 된 왼쪽 자식을 통해 계산하므로 잘못된 결과나 나온다

> Your input
[4,2,7,1,3,6,9]

> Output
[4,7,7,9,9,9,9]

> Expected
[4,7,2,9,6,3,1]

```python
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        # 개선
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root
```

위와 같이 해야 왼쪽 자식과 오른쪽 자식을 계산하고 동시에 값을 받을 수 있다.

###### 교재 풀이 참조