# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        head_node = head
        while head_node.next:
            current_node = head_node.next
            head_node.next = current_node.next
            current_node.next = head
            head = current_node
        return head
