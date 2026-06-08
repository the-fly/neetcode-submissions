# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # n1, ls, rs

        # n1, n2, ls2, rs2, n3, ls3, rs3

        # ls, r, rs

        # ls2, n2, rs2, n1, ls3, n3, rs3

        # i = 1, j = 0
        # node = root = preorder[0]
        # stack = [node]
        # while node != inorder[0]:
        #     node.left = preoder[i]
        #     node = node.left
        #     stack.push(node)
        #     i += 1
    
        if len(preorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        m = 0
        while (inorder[m] != preorder[0]):
            m += 1
        root.left = self.buildTree(preorder[1:m+1], inorder[0:m])
        root.right = self.buildTree(preorder[m+1:len(preorder)], inorder[m+1:len(preorder)])
        return root

