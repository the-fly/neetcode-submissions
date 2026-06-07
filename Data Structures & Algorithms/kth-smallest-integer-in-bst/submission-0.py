# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.countAndFind(root, k)[1]
    
    def countAndFind(self, root: Optional[TreeNode], k: int) -> (int, int):
        if not root:
            return 0, -1
        print('a', root.val, k)

        elementsOnLeft, kthSmallest = self.countAndFind(root.left, k)
        print('b', root.val, elementsOnLeft, kthSmallest)

        if elementsOnLeft == k:
            print('d', root.val, elementsOnLeft, kthSmallest)
            return (k, kthSmallest)
        
        if elementsOnLeft == (k - 1):
            print('c', root.val, elementsOnLeft, kthSmallest)
            return (k, root.val)

        elementsOnRight, kthSmallest = self.countAndFind(root.right, k - elementsOnLeft - 1)
        if elementsOnLeft + elementsOnRight +1 <k:
            return (elementsOnLeft + elementsOnRight +1, -1)
        return k, kthSmallest
        
        