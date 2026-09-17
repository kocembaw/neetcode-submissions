# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1.next and list2.next:
            if list1.val < list2.val:
                tail.next = list1
                list1.next = list1
            elif list1.val > list2.val:
                tail.next = list2
                list2.next = list2
            
            tail = tail.next
        
        tail.next = list1.next or list2.next

        return dummy.next
        