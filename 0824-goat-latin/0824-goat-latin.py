class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s=sentence.split()
        ans=[]
        for w in range(len(s)):
            if s[w][0].lower() not in 'aeiou':
                s[w]=list(s[w])
                s[w].append(s[w][0])
                del s[w][0]
                s[w]=''.join(s[w])
            s[w]+='ma'
            s[w]+='a'*(w+1)
            ans.append(s[w])
        return " ".join(ans)