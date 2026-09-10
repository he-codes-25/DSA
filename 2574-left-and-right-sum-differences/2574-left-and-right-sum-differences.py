class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ans=[]
        if len(nums)==1:
            return [0]
        if len(nums)==2:
            return nums[::-1]
        for i in range(len(nums)):
            ans.append(abs(sum(nums[0:i])-(sum(nums[i+1:-1])+nums[-1])))
            if i==len(nums)-1 and len(nums)>1:
                ans[-1]+=nums[i]
        return ans