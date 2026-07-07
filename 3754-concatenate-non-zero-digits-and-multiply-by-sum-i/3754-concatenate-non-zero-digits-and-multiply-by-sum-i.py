class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=''
        summ=0
        for i in str(n):
            if i!='0':
                summ+=int(i)
                x+=i
        if x=='':
            return 0
        return int(x)*summ