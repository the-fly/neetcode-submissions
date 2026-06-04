"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        
        nodesMap = {}
        it2 = newHead = Node(head.val)
        nodesMap[head] = newHead
        it = head

        while it:
            if it.next:
                it2.next = Node(it.next.val)
                nodesMap[it.next] = it2.next
            else:
                it2.next = None

            it, it2 = it.next, it2.next
        
        it, it2 = head, newHead

        while it2:
            if it.random:
                it2.random = nodesMap[it.random]
            it, it2 = it.next, it2.next
        return newHead
            




        