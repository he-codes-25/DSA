class Solution:
    def judgeCircle(self, moves: str) -> bool:
        ms=[0,0]
        for m in moves:
            if m=="U":
                ms[1]=ms[1]-1
            if m=='D':
                ms[-1]+=1
            if m=='R':
                ms[0]-=1
            if m=='L':
                ms[0]+=1
        return ms[-1]==0 and ms[0]==0

