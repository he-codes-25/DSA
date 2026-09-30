class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans=[]
        total=0
        gain.insert(0,0)
        for i in range(len(gain)):
            total+=gain[i]
            ans.append(total)
        return max(ans)