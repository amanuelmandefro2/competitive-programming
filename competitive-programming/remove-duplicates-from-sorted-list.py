# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        prev, curr = head, head.next
        while curr:
            if prev.val == curr.val:
                next_node = curr.next
                prev.next = next_node
                curr = next_node
            else:
                prev = curr
                curr = curr.next

        return head           
        