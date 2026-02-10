from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # if both left and rigth are empty means they're same
            if not left and not right:
                return True
            # If one of left or right is empty or left and right val isn't equal
            if not left or not right or left.val != right.val:
                return False

            # Calling dfs on pair of outer and inner nodes of the sub tree and return True if they both evaluate to True
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        # Call the dfs function to start the dfs recursion
        return dfs(root.left, root.right)
