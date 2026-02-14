from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # We'll use BFS to solve this
        if not root:
            return 0
        queue = deque([[root, 1]])
        while queue:
            node, depth = queue.popleft()
            # The first node we find that has no left and right node, return that node's depth
            if not node.left and not node.right:
                return depth
            # Else if the left and right node exists, append them with depth + 1
            if node.left:
                queue.append([node.left, depth + 1])
            if node.right:
                queue.append([node.right, depth + 1])
