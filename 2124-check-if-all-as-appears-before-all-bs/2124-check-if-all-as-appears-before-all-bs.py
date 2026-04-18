class Solution:
    def checkString(self, s: str) -> bool:
        s=list(s)
        a=s.copy()
        s.sort(reverse=False)
        return a==s