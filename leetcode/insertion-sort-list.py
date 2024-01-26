# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr = None, head
        while curr and curr.next:
            prev = curr
            curr = curr.next
            if prev.val > curr.val:
                prev.next = curr.next
                curr.next = None
                prev_pointer,head_pointer = None, head 
                while curr.val > head_pointer.val:
                    prev_pointer = head_pointer
                    head_pointer = head_pointer.next

                if not prev_pointer:
                    curr.next = head
                    head = curr
                else:
                    next_node = prev_pointer.next
                    prev_pointer.next = curr
                    curr.next = next_node

        return head                


        
        
        