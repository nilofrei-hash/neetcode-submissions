class Solution:
    def validPalindrome(self, s: str) -> bool:
      for i in range(len(s)):
        strint = s[:i] + s[i + 1:]
        if strint == strint[::-1]:
            return True 
      return False 