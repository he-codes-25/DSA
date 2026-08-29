class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count=0
        for n in range(len(nums)-1):
            if (sum(nums[:n+1])-sum(nums[n+1:]))%2==0:
                print(sum(nums[:n+1]),sum(nums[n+1:]))
                count+=1
        return count