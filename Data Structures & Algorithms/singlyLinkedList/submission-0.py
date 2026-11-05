class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node()
        self.tail = self.head

    def get(self, index: int) -> int:
        m = self.head.next 
        counter = 0
        while m is not None:
            if index == counter:
                return m.val 
            counter += 1
            m = m.next
        return -1

    def insertHead(self, val: int) -> None:
        m = Node(val, self.head.next)
        self.head.next = m
        if not m.next:
            self.tail = m

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        m = self.head
        counter = 0
        while m is not None and counter < index:
            m = m.next
            counter += 1
            
        if m is None or m.next is None:
            return False
            
        m.next = m.next.next
        if m.next is None:
            self.tail = m
        return True

    def getValues(self) -> List[int]:
        m = self.head.next 
        Liste = []
        while m is not None:
            Liste.append(m.val)
            m = m.next 
        return Liste