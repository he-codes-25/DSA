class Solution:
    def numberOfMatches(self, n: int) -> int:
        m=0
        while True:
            if n==1:
                return int(m)
            elif n%2==0:
                m+=n/2
                n=n/2
            elif n%2!=0:
                m+=(n-1)/2
                n=(n - 1) / 2 + 1
        