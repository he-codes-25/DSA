class Solution(object):
    def threeSum(self, nums):
        ans=[]
        nums.sort()
        for n in range(len(nums)):
            left=n+1
            right=len(nums)-1
            while left<right:
                target=nums[left]+nums[right]+nums[n]
                if target==0 and [nums[left],nums[right],nums[n]] not in ans:
                    ans.append([nums[left],nums[right],nums[n]])
                    right-=1
                    left+=1
                elif target>0:
                    right-=1
                else:
                    left+=1
        return ans