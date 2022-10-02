# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None: return head

        ls = head

        while (ls.next != None):
            if ls.val == ls.next.val:
                ls.next = ls.next.next
            else:
                ls = ls.next

        return head
