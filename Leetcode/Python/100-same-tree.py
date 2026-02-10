from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both p and q are None that means they're equal
        if not p and not q:
            return True
        # If one p or q is None or p and q have different values
        if not p or not q or p.val != q.val:
            return False

        # Now we check if the left and right subtree of p & q are same or not, and our return will only be True
        # if both of them return True
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
