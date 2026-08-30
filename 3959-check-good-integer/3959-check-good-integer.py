class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitsum=0
        squaresum=0
        for i in str(n):
            digitsum+=int(i)
            squaresum+=int(i)**2
        return (squaresum-digitsum)>=50