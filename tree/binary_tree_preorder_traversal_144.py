from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderResult(self, root: Optional[TreeNode], result=None):
        curr = root
        if result is None:
            result = []
        result.append(curr.val)
        if curr.left:
            self.preorderResult(curr.left, result)

        if curr.right:
            self.preorderResult(curr.right, result)
        return result

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.preorderResult(root)


sol = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.left.right.left = TreeNode(6)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(9)
print(f" {root.val =}  {sol.preorderTraversal(root) =}")

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(f" {root.val =}  {sol.preorderTraversal(root) =}")

root = None
print(f" {root =}  {sol.preorderTraversal(root) =}")

root = TreeNode(1)
print(f" {root.val =}  {sol.preorderTraversal(root) =}")
