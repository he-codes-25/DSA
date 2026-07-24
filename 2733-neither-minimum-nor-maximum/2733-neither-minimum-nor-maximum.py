class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        for n in nums:
            if n==nums[0] or n==nums[-1]:
                pass
            else:
                return n
        return -1