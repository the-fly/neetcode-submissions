# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # print(4)
        length = 0
        it = head
        while it:
            # print(3)
            length += 1
            it = it.next
        
        it = head
        index, middle = 0, length // 2 

        while (index<middle):
            # print(1)
            index += 1
            it = it.next
        if length % 2:
            it = it.next
        
        list1, list2 = head, it

        list2 = self._reverList(list2)

        it1, it2 = list1, list2
        index = 0

        while(it2):
            # print(2)
            index += 1
            it1.next, it2.next, it1, it2 = it2, it1.next, it1.next, it2.next
        it1.next = None
        return 


    def _reverList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev


        