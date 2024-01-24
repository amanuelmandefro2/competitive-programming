# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        merge = ListNode()
        head = merge
        print(head)
        curr_list1 = list1
        curr_list2 = list2
        curr_merge = merge

        while curr_list1 and curr_list2:
            if curr_list1.val <= curr_list2.val:
                curr_merge.next = curr_list1
                curr_merge = curr_merge.next
                curr_list1 = curr_list1.next
            else:
                curr_merge.next  = curr_list2
                curr_merge = curr_merge.next
                curr_list2 = curr_list2.next
        while curr_list1:
            curr_merge.next = curr_list1
            curr_merge = curr_merge.next
            curr_list1 = curr_list1.next 
        while curr_list2:
            curr_merge.next  = curr_list2
            curr_merge = curr_merge.next
            curr_list2 = curr_list2.next  

        head = head.next           
                
        return head
        