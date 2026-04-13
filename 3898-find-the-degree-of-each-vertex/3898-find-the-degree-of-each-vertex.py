class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:
        ans=["_"]*len(matrix)
        for m in range(len(matrix)):
            ans[m]=sum(matrix[m])
        return ans