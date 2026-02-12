from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]) -> list:
            # If the root is Null, means it is balanced and we can return True with depth 0
            if not root:
                return [True, 0]
            # Else we calculate left and right subtree's
            left, right = dfs(root.left), dfs(root.right)
            # If left and right and their depth difference is less or equal to 1, it'll evaluate to True
            # Else False
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            # Now return balanced, with max of left and right depth incremented by 1
            return [balanced, 1 + max(left[1], right[1])]

        # Return the first value of the returned list
        return dfs(root)[0]
