from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        cur = root
        # Keep on iterating until both cur and stack becomes none/empty
        while cur or stack:
            # Keep on looping until cur becomes None
            while cur:
                # Append every node into stack that we visit while going to the leftmost part of the tree
                stack.append(cur)
                # shift the pointer to the left
                cur = cur.left
            # Now pop the last non-empty node from the stack
            cur = stack.pop()
            # Store it's node value in res list
            res.append(cur.val)
            # Since we have the checked the leftmost part of the last non-empty node, it's time to check the right side
            cur = cur.right
        # Return res, containing all the node values in inorder traversal
        return res
