class DynamicArray:
    
    def __init__(self, capacity: int):
      self.capacity = capacity 
      self.counter = 0
      self.array = [0 for i in range(capacity)] 

    def get(self, i: int) -> int:
      return self.array[i]

    def set(self, i: int, n: int) -> None:
      self.array[i] = n  

    def pushback(self, n: int) -> None:
      if self.counter == self.capacity:
        self.resize()
      self.array[self.counter] = n
      self.counter += 1 
      


    def popback(self) -> int:
       s = self.array[self.counter - 1]
       self.array.pop()
       self.counter -= 1 
       return s
    
    def resize(self) -> None:
      for i in range(self.capacity):
        self.array.append(0)
      self.capacity *= 2 
      
      

    def getSize(self) -> int:
      return self.counter 
        
    
    def getCapacity(self) -> int:
      return self.capacity 
