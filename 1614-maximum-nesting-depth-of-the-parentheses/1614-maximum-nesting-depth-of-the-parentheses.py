class Solution:
    def maxDepth(self, s: str) -> int:
        ans=0
        for i in range(len(s)):
            if (s[i:].count(')')-s[i:].count('('))>ans:
                ans=s[i:].count(')')-s[i:].count('(')
        return ans