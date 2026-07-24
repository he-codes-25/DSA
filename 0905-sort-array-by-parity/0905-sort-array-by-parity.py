class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans1=[]
        ans2=[]
        for n in nums:
            if n%2==0:
                ans1.append(n)
            else:
                ans2.append(n)
        ans1.sort()
        ans2.sort()
        return ans1+ans2