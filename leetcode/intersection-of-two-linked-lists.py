# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        location_one = set()
        curr = headA
        while curr:
            location_one.add(curr)
            curr = curr.next
        curr2  = headB
        while curr2:
            if curr2 in location_one:
                return curr2
            curr2 = curr2.next        
            