class Solution:
    def hasCycle(self, head):
      Slow = head
      Fast = head
      while Fast is not None and Fast.next is not None:
         
         Fast = Fast.next.next 
         Slow = Slow.next 
         if Fast == Slow:
            return True
      return False       