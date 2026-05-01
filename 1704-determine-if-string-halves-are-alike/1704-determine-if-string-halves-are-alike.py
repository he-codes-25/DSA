class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a=0
        b=0
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU' and len(s)/2-1>=i:
                a+=1
            elif s[i] in 'aeiouAEIOU' and len(s)/2-1<i:
                b+=1
        return a==b