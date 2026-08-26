class Solution:
    def largestOddNumber(self, num: str) -> str:
        for n in range(len(num)-1,-1,-1):
            if int(num[n])%2!=0:
                return num[:n+1]
        return ''