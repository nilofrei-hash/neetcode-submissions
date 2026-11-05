# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        m = head 
        prev = None 
        while m is not None:
            next_node = m.next
            m.next = prev 
            prev = m
            m = next_node         
        return prev 