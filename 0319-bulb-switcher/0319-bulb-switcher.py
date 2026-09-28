class Solution:
    def bulbSwitch(self, n: int) -> int:
        ans=0
        for i in range(1,n+1):
            if i**2<=n:
                ans+=1
            else:
                break
        return ans
        