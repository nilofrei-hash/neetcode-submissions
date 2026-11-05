class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.nums = nums 
        liste = []
        for i in range(len(nums)):
            if nums[i] in liste:
                return True 
            else:
                liste.append(nums[i])
        return False 
        