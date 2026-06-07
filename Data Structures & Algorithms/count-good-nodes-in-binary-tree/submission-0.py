# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self._goodNodes(root, -101)

    def _goodNodes(self, root:TreeNode, prevMax) -> int:

        if not root: return 0

        if root.val >= prevMax:
            prevMax = root.val
            return 1+ self._goodNodes(root.left, prevMax) + self._goodNodes(root.right, prevMax)

        return self._goodNodes(root.left, prevMax) + self._goodNodes(root.right, prevMax)


        