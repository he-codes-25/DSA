class Solution:
    def maxProduct(self, n: int) -> int:
        s=str(n)
        l=[]
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                l.append(int(s[i])*int(s[j]))
        return max(l)