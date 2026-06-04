# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        it1, it2 = l1, l2
        carry = 0
        while it1:
            a = it1.val if it1 else 0
            b = it2.val if it2 else 0
            sum = a + b + carry
            it1.val = sum%10
            carry = sum // 10

            if not it1.next and it2 and it2.next:
                it1.next ,it2.next = it2.next, it1.next
            
            if (not it1.next and carry):
                it1.next = ListNode(carry)
                carry = 0
            it1 = it1.next 
            it2 = it2.next if it2 else None
        


        
        return l1


        