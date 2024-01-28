# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        if n == 1:
            prev = prev.next
        else:
            prev_node, curr = None, prev
            while curr and n > 1:
                prev_node = curr
                curr = curr.next
                n -= 1
            prev_node.next = curr.next 

        head, curr = None, prev
        while curr:
            next_node = curr.next
            curr.next = head
            head = curr
            curr = next_node   
        return head    
 