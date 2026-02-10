from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def dfs(l: int, r: int) -> Optional[TreeNode]:
            # If left pointer is greater than right pointer return None
            if l > r:
                return None

            # Calculate middle index
            m = (l + r) // 2
            # Store the mid value in a new TreeNode
            root = TreeNode(nums[m])
            # Call dfs on the left portion of the array
            root.left = dfs(l, m - 1)
            # Call dfs on the right portion of the array
            root.right = dfs(m + 1, r)
            # After we have computed both of the subtree return the root
            return root

        # Kick start the dfs function with 0 and len(nums) - 1 index positions and return the root
        return dfs(0, len(nums) - 1)
