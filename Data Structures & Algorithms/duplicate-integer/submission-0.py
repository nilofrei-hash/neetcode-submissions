class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Resultat = []
        for i in range(len(nums)):
          if nums[i] in Resultat:
            return True
          Resultat.append(nums[i])
        return False