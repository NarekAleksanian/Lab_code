# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head == None:
            return head
        
        while head and head.val == val:
            head = head.next
            
        head_node = head
        while head_node:
            if head_node.next and head_node.next.val == val:
                head_node.next = head_node.next.next
            else:
                head_node = head_node.next
        return head
        
        
