class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        ans=[[1]]
        for i in range(1,numRows):
            ans2=[1]
            for j in range(len(ans[i-1])-1):
                total=0
                total+=(ans[i-1][j]+ans[i-1][j+1])
                ans2.append(total)
            ans2.append(1)
            ans.append(ans2)
        return ans