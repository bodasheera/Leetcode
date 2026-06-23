# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        if not head:
            return head
        
       
        curr = head
        prev = None

        while curr:

            while curr and curr.val == val:

                if prev is not None:
                    prev.next = curr.next
                    curr = curr.next
                else:
                    curr = curr.next
                    head = curr
                    
            prev = curr
            curr = curr.next if curr else None

        return head
