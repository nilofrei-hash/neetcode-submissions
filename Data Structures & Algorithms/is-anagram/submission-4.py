class Solution:
    
        
        
        
    
  def isAnagram(self, s: str, t: str) -> bool:
    d = list(map(chr, sorted([ord(i) for i in s])))
    m = list(map(chr, sorted([ord(i) for i in t])))
    if m == d:
      return True 
    return False 


        