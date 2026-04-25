class Solution:
    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
        n=list(map(str,nums))
        n="".join(n)
        return n.count(str(digit))