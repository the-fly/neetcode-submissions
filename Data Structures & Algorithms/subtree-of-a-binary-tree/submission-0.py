# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not root and not subRoot:
            return True
        
        if root and not subRoot:
            return False

        if subRoot and not root:
            return False
        
        if root.val == subRoot.val:
            if self.isSame(root, subRoot):
                return True
            
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSame(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if (not root1 and root2) or (root1 and not root2) or (not root1.val == root2.val):
            return False
        
        return self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right)

        