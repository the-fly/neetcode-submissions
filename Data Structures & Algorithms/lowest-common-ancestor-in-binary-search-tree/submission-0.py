# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return

        if p.val > q.val:
            p, q = q, p
        x, l, r = root.val, p.val, q.val
        
        if l <= x <= r:
            return root
        
        if r<x:
            return self.lowestCommonAncestor(root.left, p, q)
        
        else:
            return self.lowestCommonAncestor(root.right, p, q)
        