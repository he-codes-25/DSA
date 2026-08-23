class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        n=len(prices)
        ans=prices.copy()
        stack=[]
        for i in range(n):
            while stack and prices[stack[-1]]>=prices[i]:
                prev=stack.pop()
                ans[prev]-=ans[i]
            stack.append(i)
        return ans