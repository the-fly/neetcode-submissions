# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        else:
            leftDepth, leftMax = self._depth_and_dia(root.left)
            rightDepth, rightMax = self._depth_and_dia(root.right)
            return max(leftMax, rightMax, leftDepth + rightDepth + 1) -1

    
    def _depth_and_dia(self, root: Optional[TreeNode]) -> (int, int):
        if not root:
            return 0, 0

        else:
            leftDepth, leftMax = self._depth_and_dia(root.left)
            rightDepth, rightMax = self._depth_and_dia(root.right)
            return (max(leftDepth, rightDepth) + 1, max(leftMax, rightMax, leftDepth + rightDepth + 1))
