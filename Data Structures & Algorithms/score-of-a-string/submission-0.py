class Solution:
    def scoreOfString(self, s: str) -> int:
        Resultat = 0
        for i in range(1, len(s)):
          Resultat += abs(ord(s[i - 1]) - ord(s[i]))
        return Resultat 