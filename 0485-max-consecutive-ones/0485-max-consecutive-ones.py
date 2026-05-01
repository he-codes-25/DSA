class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=[]
        streak=0
        for n in range(len(nums)):
            if nums[n]==1:
                streak+=1
                if n==len(nums)-1:
                    ans.append(streak)
            elif nums[n]==0:
                ans.append(streak)
                streak=0
        return max(ans)