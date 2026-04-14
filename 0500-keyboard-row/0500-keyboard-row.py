class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans=[]
        for w in words:
            s=None
            for l in w.lower():
                if s==None:
                    if l in "qwertyuiop":
                        s="qwertyuiop"
                    elif l in "asdfghjkl":
                        s="asdfghjkl"
                    elif l in "zxcvbnm":
                        s="zxcvbnm"
                elif l not in s:
                    break
            else:
                ans.append(w)
        return ans