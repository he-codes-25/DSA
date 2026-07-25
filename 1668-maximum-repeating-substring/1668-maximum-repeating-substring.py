class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        count=0
        r=word
        while r in sequence:
            count+=1
            r+=word
        return count
        