# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return "N"
        queue = deque([root])
        res = []
        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ",".join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        bfs = data.split(',')

        if bfs[0] == "N":
            return None

        root = TreeNode(int(bfs[0])) 

        queue = deque([root])
        index = 1

        while queue:
            node = queue.popleft()
            
            if bfs[index] != "N":
                node.left = TreeNode(int(bfs[index])) 
                queue.append(node.left)
            index += 1

            if bfs[index] != "N":
                node.right = TreeNode(int(bfs[index])) 
                queue.append(node.right)
            index += 1

        return root

        
        


    # def _preorder(self, root: Optional[TreeNode]) -> str:
    #     if not root:
    #         return ''
    #     return str(root.val) + ' ' + self._preorder(root.left) + self._preorder(root.right)
    
    # def _inorder(self, root: Optional[TreeNode]) -> str:
    #     if not root:
    #         return ''
    #     return self._inorder(root.left) + str(root.val) + ' ' + self._inorder(root.right)
    
    # def _createTree(self, preorder: [int], inorder: [int]) -> Optional[TreeNode]:
    #     print('b', preorder,'\n', inorder)
    #     treesize = len(preorder)
    #     if treesize == 0:
    #         return None
        
    #     root = TreeNode(preorder[0])

    #     m = 0
    #     for index in range(treesize):
    #         if inorder[index] == root.val:
    #             m = index
    #             break
    #     root.left = self._createTree(preorder[1:m+1], inorder[0:m]) 
    #     root.right = self._createTree(preorder[m+1:treesize], inorder[m+1:treesize])

    #     return root



