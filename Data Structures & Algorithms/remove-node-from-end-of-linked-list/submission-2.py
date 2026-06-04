# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        it = head
        while it:
            length += 1
            it = it.next
        
        if (not head) or length == 1:
            return None
        
        target = length - n

        index = 0
        prev, curr = None, head

        while index<target:
            prev, curr = curr, curr.next
            index+=1
        if not prev:
            head = curr.next
        else:
            prev.next = curr.next

        return head



        