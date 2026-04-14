class Solution:
    def sortVowels(self, s: str) -> str:
        s=list(s)
        hp=[]
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                hp.append(s[i])
                s[i]='_'
        hp.sort()
        c=0
        for h in range(len(s)):
            if s[h]=='_':
                s[h]=hp[c]
                c+=1
        return "".join(s)
                