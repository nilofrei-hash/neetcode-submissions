class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        self.s = s 
        k = s.split()
        return len(k[-1])
      