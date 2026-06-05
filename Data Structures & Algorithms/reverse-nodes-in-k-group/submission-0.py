# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        prev_end, curr_start = None, head
        k_next = self._next_skip_node(curr_start, k)
        while curr_start != k_next:
            prev, curr = k_next, curr_start
            while curr!=k_next:
                curr.next, prev, curr = prev, curr, curr.next
            if prev_end:
                prev_end.next = prev
            else:
                head = prev
            prev_end, curr_start = curr_start, curr
            k_next = self._next_skip_node(curr_start, k)
        return head
                

    def _next_skip_node(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        it = head
        for i in range(k):
            if it:
                it = it.next
            else: return head
        return it

