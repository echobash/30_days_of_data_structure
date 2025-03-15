from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:  # Edge case: Empty tree
            return []

        queue = deque([root])
        while queue:
            temp = []
            n = len(queue)
            for _ in range(n):
                popped_element = queue.popleft()
                temp.append(popped_element.val)

                if popped_element.left:
                    queue.append(popped_element.left)
                if popped_element.right:
                    queue.append(popped_element.right)
            result.append(temp)
        return result


sol = Solution()

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(root, sol.levelOrder(root))

root = TreeNode(1)
print(root, sol.levelOrder(root))

root = None
print(root, sol.levelOrder(root))
