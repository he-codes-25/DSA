class Solution(object):
    def mergeAlternately(self, word1, word2):
        ans=''
        a1=len(word1)
        a2=len(word2)
        for i,w in enumerate(word1):
            if a2!=0:
                ans+=w
                ans+=word2[i]
                a1-=1
                a2-=1
        if a1>a2:
            return ans+word1[-a1:]
        if a1<a2:
            return ans+word2[-a2:]
        return ans