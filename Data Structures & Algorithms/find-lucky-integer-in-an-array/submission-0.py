class Solution:
    def findLucky(self, arr: List[int]) -> int:
        Biggest = -1
        for m in arr:
          if arr.count(m) == m:
            Biggest = m 
        return Biggest 
            