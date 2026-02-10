from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # We push our root into the stack, whether it is None or not
        stack = [[root, 1]]
        # We start at 0 because if root is empty the if condition won't execute stack becomes empty and we return 0
        res = 0

        # While stack isn't empty
        while stack:
            # Pop the last element or top pair of node and it's depth from the stack
            node, depth = stack.pop()
            # If the node is empty that means it's parent node (non-empty node) depth is the max for this path
            if node:
                # Pick the max value between the res and depth of the current node
                res = max(res, depth)
                # Append the pair of it's left and right node with depth increased by 1
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        # res at this point stores the highest depth value for the binary tree
        return res
