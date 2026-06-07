# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self._isValidBST(root, float('-inf'), float('inf'))
        

    def _isValidBST(self, root: Optional[TreeNode], minLim: int, maxLim: int) -> bool:
        print('a', root.val)
        if not root or (root and not root.left and not root.right):
            print('b', root.val)
            return True
        
        validLeft = True
        if root.left:
            print('c', root.left.val)
            validLeft = minLim<root.left.val<root.val and self._isValidBST(root.left, minLim, root.val)
            print ('c1', validLeft)
        validRight = True
        if root.right:
            print('d', root.right.val)
            validRight = root.val < root.right.val < maxLim and self._isValidBST(root.right, root.val, maxLim)
        # print(left, root.val, right)
        return validLeft and validRight

        