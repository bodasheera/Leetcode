# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head

        prev = head 
        curr = head.next

        while curr != None:

            temp = None

            while curr is not None and curr.val == prev.val :
                temp = curr
                curr = curr.next

            if temp:
                temp.next = None
                prev.next = curr 

            prev = curr 
            curr = curr.next if curr is not None else None

        return head

            


        