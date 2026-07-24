class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        check=[]
        pair=0
        for n in nums:
            if n in check:
                pair+=1
                del check[check.index(n)]
            else:
                check.append(n)
        return [pair,len(nums)-(pair*2)]