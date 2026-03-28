class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ans=set()
        mc=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for w in words:
            word=''
            for l in w:
                word+=mc[ord(l)-ord('a')]
            ans.add(word)
        return len(ans)
