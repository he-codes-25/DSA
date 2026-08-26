class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        n=nums.index(max(nums))
        num=nums.pop(n)
        if num>=max(nums)*2:
            return n
        return -1