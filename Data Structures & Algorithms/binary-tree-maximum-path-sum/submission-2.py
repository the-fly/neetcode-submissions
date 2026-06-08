# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.longestPathAndRes(root)[1]

    def longestPathAndRes(self, root: Optional[TreeNode]) -> (int, int):
        if not root:
            return (-1001, -1001)
        
        longestLeft, resLeft = self.longestPathAndRes(root.left)
        longestRight, resRight = self.longestPathAndRes(root.right)

        res = max(resLeft, resRight, max(longestLeft, 0)+ max(longestRight,0) + root.val)
        longestPath = max(longestLeft, longestRight, 0) + root.val
        # print(root.val, res, longestPath)
        return (longestPath, res)       