class Solution:
    def isUgly(self, n: int) -> bool:
        while n!=1 and n!=2 and n!=3 and n!=5:
            s=n
            if n%2==0:
                n/=2
            elif n%3==0:
                n/=3
            elif n%5==0:
                n/=5
            if n==s:
                return False
        return True
            