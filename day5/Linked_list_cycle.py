# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:     
        small = big = head
        while big and big.next:
            small = small.next
            big = big.next.next
            if small == big:
                return True
        return False
