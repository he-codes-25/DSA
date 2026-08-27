class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        seen=[]
        answer=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.append(s[right])
            answer=max(answer,right-left+1)
        return answer