# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        m = head 
        Liste = []
        while m is not None:
          Liste.append(m.val)
          m = m.next 
        return Liste == Liste[::-1]