# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        sorted_list_it = head = ListNode()

        while True:
            next_min = float('inf')
            min_it = None

            # Find list with lowest First node
            for it in range(len(lists)):
                node = lists[it]
                if node and node.val<next_min:
                    next_min = node.val
                    min_it = it

            # If not found, all lists are now empty, break and return sorted list
            if next_min == float('inf'):
                break

            #If found, add that node to sorted list, shift original list by one element
            else:
                sorted_list_it.next, lists[min_it] = lists[min_it], lists[min_it].next
                sorted_list_it = sorted_list_it.next
                sorted_list_it.next = None
        
        return head.next

                    

        