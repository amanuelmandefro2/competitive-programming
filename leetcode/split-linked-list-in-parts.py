# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size=0
        curr=head
        while(curr):
            size+=1
            curr=curr.next

        count=0
        ans=[]
        curr=head

        while(k>0):
            nodecount=ceil((size-count)/k)
            if nodecount==0:
                ans.append(None)
            else:
                ans.append(curr)
                prev=curr
                while(nodecount>0 and curr):
                    prev=curr
                    curr=curr.next
                    count+=1
                    nodecount-=1
                prev.next=None
            k-=1
            
        return ans