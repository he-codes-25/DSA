class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        b=len(nums)
        for i in list(set(nums)):
            a=nums.count(i)
            if a>b/2:
                return i