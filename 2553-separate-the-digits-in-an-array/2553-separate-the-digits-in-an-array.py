class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        a=''
        ans=[]
        for n in nums:
            a+=str(n)
        for i in a:
            ans.append(int(i))  
        return ans
