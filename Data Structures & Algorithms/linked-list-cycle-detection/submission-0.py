# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        it = head
        nodeSet = set()
        while it:
            if it in nodeSet:
                return True
            nodeSet.add(it)
            it = it.next
        return False
        