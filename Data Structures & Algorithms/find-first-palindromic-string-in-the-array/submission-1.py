class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def is_Palindrom(String):
            if String[::-1] == String:
                return True 
            return False 
        for i in words:
            if is_Palindrom(i):
                return i 
        return ""
