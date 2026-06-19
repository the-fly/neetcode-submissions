"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        q = deque()
        clones= {node: Node(node.val)}
        q.append(node)

        while(q):
            thisNode = q.popleft()
            if thisNode.neighbors:
                for neighbor in thisNode.neighbors:
                    if neighbor not in clones:
                        clones[neighbor] = Node(neighbor.val)
                        q.append(neighbor)
                    clones[thisNode].neighbors.append(clones[neighbor])
        return clones[node]            


        