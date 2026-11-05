# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 1. Dummy-Knoten erstellen, der vor dem Head zeigt
        dummy = ListNode(next=head)
        m = dummy
        
        # 2. Die Liste durchlaufen
        while m.next is not None:
            if m.next.val == val:
                # Zeiger überspringen (Knoten löschen)
                m.next = m.next.next 
            else:
                # Nur weitergehen, wenn kein Knoten gelöscht wurde
                m = m.next 
        
        # 3. Den neuen Start der Liste zurückgeben
        return dummy.next
