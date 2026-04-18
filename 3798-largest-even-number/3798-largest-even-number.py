class Solution:
    def largestEven(self, s: str) -> str:
        s=list(s)
        while s!=[] and int(s[-1])%2!=0:
            s.pop()
        return "".join(s)