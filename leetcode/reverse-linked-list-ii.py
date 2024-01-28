# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        i = 1
        prev_left, prev, curr = None, None, head
        next_right = None
        while i <= right and curr:
            if i == left:
                prev_left = prev
            if i == right:
                next_right = curr.next   
            i += 1
            prev = curr 
            curr = curr.next
        rev_prev = None    
        
        curr = prev_left.next if prev_left else head
        head_rev = curr
        while curr and curr != next_right:
            next_node = curr.next
            curr.next = rev_prev
            rev_prev = curr
            curr = next_node

        if prev_left:
            prev_left.next = rev_prev
            head_rev.next = next_right
            return head
        else:
            head_rev.next = next_right
            return rev_prev    

        return rev_prev

            
      

                



        