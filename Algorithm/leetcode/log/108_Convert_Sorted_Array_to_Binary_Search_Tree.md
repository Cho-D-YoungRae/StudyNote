#### [108_Convert_Sorted_Array_to_Binary_Search_Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
> 425pg


###### My Solution 1

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        mid = len(nums) // 2
        new_node = TreeNode(nums[mid])
        new_node.left = self.sortedArrayToBST(nums[:mid])
        new_node.right = self.sortedArrayToBST(nums[mid+1:])

        return new_node
```

> Runtime: 76 ms, faster than 34.66% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

> Memory Usage: 16.4 MB, less than 71.79% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
