class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        total=0
        for i in str(n):
            total+=int(i)
        return total