class Solution:
    def greatestLetter(self, s: str) -> str:
        a=list()
        for i in s:
            if i==i.upper() and i.lower() in s:
                a.append(i)
        a.sort()
        if list(a)!=[]:
            return a[-1]
        return ""