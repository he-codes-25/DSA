class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=str(int("".join(map(str,digits)))+1)
        p=[]
        for i in n:
           p.append(int(i))
        return p