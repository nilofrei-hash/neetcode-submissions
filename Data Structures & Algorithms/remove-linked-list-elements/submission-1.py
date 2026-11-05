# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Schritt 1: Entferne alle passenden Elemente am Anfang der Liste
        while head is not None and head.val == val:
            head = head.next
            
        # Schritt 2: Durchlaufe den Rest der Liste
        current = head
        while current is not None and current.next is not None:
            if current.next.val == val:
                # Element überspringen
                current.next = current.next.next
            else:
                # Nur weitergehen, wenn kein Element gelöscht wurde
                current = current.next
                
        return head
