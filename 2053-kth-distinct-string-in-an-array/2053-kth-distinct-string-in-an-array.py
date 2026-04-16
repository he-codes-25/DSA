class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans=[]
        for a in arr:
            if arr.count(a)==1:
                ans.append(a)
        if k>len(ans):
            return ''
        return ans[k-1]
        