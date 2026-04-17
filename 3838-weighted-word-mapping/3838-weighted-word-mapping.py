class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans=[]
        for w in words:
            summ=0
            for l in w:
                summ+=weights[ord(l)-ord('a')]
            ans.append(chr(ord('z')-summ%26))
        return "".join(ans)