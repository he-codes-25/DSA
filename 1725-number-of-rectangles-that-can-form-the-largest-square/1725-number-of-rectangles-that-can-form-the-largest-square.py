class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        ans=[]
        for r in rectangles:
            r.sort()
            ans.append(r[0])
        return ans.count((max(ans)))