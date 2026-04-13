class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans=[]
        for n in range(len(nums)):
            if nums[n]==target:
                ans.append(abs(n-start))
        ans.sort()
        return ans[0]