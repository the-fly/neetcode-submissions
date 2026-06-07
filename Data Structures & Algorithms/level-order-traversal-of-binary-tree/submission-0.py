# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
        
        level = [root]

        res = []

        while len(level) != 0:
            levelInt = []                
            # res.append(level)
            nextLevel = []
            for node in level:
                levelInt.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            res.append(levelInt)
            level = nextLevel
        return res



        