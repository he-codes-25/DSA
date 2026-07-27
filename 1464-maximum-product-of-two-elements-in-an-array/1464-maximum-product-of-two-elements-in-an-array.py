class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans=[]
        for x in range(len(nums)-1):
            for j in range(x+1,len(nums)):
                ans.append((nums[x]-1)*(nums[j]-1))
        ans.sort()
        return ans[-1]