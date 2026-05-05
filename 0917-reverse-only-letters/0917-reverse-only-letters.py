class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        ans=[]
        b=[]
        for i in range(len(s)):
            if s[i].isalpha():
                ans.append(s[i])
                b.append(i)
        ans=ans[::-1]
        for j in range(len(b)):
            s[b[j]]=ans[j]
        return "".join(s)