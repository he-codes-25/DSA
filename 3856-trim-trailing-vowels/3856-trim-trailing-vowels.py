class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        s=list(s[::-1])
        ans=s
        for i in range(len(s)):
            if s[i] in 'aeiou':
                ans[i]=''
            else:
                break
        return "".join(ans[::-1])