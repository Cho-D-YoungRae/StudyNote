#### 중첩 함수에서 클래스 변수를 사용한 이유


**중첩 함수에서 클래스 변수를 사용한 예**
```python
class Solution:
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)

            # 클래스 변수를 사용하지 않았다면 문제가 될 부분
            self.longest = max(self.longest, left + right + 2)


            return max(left, right) + 1

        dfs(root)
        return self.longest
```

중첩 함수는 부모 함수의 변수를 읽어들일 수 있다. 하지만 중첩 함수에서 부모 함수의 변수를 재할당하게되면 참조 ID가 변경되며 별도의 로컬 변수로 선언이 된다. longest의 값이 숫자나 문자가 아니라 리스트나 딕셔너리 같은 자료형이라면 append() 등의 메소드를 이용해 재할당 없이 조작 가능하여 중첩 함수 내에서도 변수의 값을 조작할 수 있다. 그러나 숫자나 문자인 경우 불변 객체이기 때문에 중첩 함수 내에서는 값을 변경할 수 없다.

> `파이썬 알고리즘 인터뷰` 392pg