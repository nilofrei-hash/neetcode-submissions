class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        counter = []
        for i in range(len(nums)):
          counter.append(nums[i] * nums[i])
        return sorted(counter)
        