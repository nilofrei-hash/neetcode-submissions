# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1. Wir behalten einen festen Zeiger auf den Start des Dummy-Knotens
        start = ListNode()
        # 'current' wandert jetzt durch die Liste, 'start' bleibt am Anfang stehen
        current = start
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2 
                list2 = list2.next 
            current = current.next  # Das können wir einmal am Ende der Schleife machen
            
        # 2. Hier hängen wir den verbleibenden Rest der längeren Liste an
        current.next = list1 if list1 else list2
        
        # 3. Wir geben das Element NACH dem Dummy-Knoten zurück (der echte Start)
        return start.next


        