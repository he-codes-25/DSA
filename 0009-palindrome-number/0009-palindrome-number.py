class Solution(object):
    def isPalindrome(self, x):
        x=str(x)
        reverse=''
        for i in range(len(x)-1, -1, -1):
            reverse += x[i]
        return x==reverse
        