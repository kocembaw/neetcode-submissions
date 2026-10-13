# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        Prev = none
        while curr:
            nxt = curr.next
            curr.next = Prev
            Prev = curr
            curr = nxt
        return Prev