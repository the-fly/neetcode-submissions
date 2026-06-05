# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if self._depth(root) == -1:
            return False
        
        return True

    def _depth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        
        left_depth = self._depth(root.left)
        if left_depth == -1:
            return left_depth
        right_depth = self._depth(root.right)
        if right_depth == -1:
            return right_depth

        if abs(left_depth - right_depth) > 1:
            return -1
        
        return 1+ max(left_depth, right_depth)

        