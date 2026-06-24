class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text=list(text)
        still=True
        count=0

        while still:
            for l in 'balloon':
                if l in text:
                    text.remove(l)
                else:
                    still=False
            if still:
                count+=1
        return count