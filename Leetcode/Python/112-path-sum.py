from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [[root, root.val]]
        while stack:
            node, cur_sum = stack.pop()
            # If the current sum is equal to target sum and this node it the leaf node, then return True
            if cur_sum == targetSum and not node.left and not node.right:
                return True
            if node.left:
                stack.append([node.left, cur_sum + node.left.val])
            if node.right:
                stack.append([node.right, cur_sum + node.right.val])
        return False
