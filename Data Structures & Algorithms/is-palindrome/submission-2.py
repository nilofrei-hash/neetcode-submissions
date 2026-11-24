class Solution:
    def isPalindrome(self, s: str) -> bool:
        String = "".join(c.lower() for c in s if c.isalnum())
        left, right = 0, len(String) - 1 
        while left < right:
            if String[left] != String[right]:
                return False 
            left += 1
            right -= 1
        return True 