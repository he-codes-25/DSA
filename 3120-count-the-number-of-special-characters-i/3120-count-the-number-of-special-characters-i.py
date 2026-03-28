class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count=0
        used=[]
        for w in word:
            if w not in used and w.upper() in word and w.lower() in word:
                count+=1
                used.append(w.lower())
                used.append(w.upper())
        return count