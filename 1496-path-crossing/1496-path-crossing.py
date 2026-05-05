class Solution:
    def isPathCrossing(self, path: str) -> bool:
        d=[[0,0]]
        for p in path:
            if p=='S':
                if [d[-1][0],d[-1][1]+1] not in d:
                    d.append([d[-1][0],d[-1][1]+1])
                else:
                    return True
            if p=='N':
                if [d[-1][0],d[-1][1]-1] not in d:
                    d.append([d[-1][0],d[-1][1]-1])
                else:
                    return True
            if p=='E':
                if [d[-1][0]-1,d[-1][1]] not in d:
                    d.append([d[-1][0]-1,d[-1][1]])
                else:
                    return True
            if p=='W':
                if [d[-1][0]+1,d[-1][1]] not in d:
                    d.append([d[-1][0]+1,d[-1][1]])
                else:
                    return True
        return False