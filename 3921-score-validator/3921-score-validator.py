class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score=0
        counter=0
        for e in events:
            if counter<10:
                if e in ['0','1','2','3','4','6']:
                    score+=int(e)
                if e=='W':
                    counter+=1
                if e=="WD" or e=="NB":
                    score+=1
        return [score,counter]