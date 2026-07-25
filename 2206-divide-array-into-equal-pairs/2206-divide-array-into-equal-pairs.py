class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for n in nums:
            if nums.count(n)%2!=0:
                return False
        return True