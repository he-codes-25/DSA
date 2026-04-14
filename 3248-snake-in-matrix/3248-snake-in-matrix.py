class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        place=[0,0]
        for c in commands:
            if c=="UP":
                place[1]-=1
            elif c=='DOWN':
                place[1]+=1
            elif c=="RIGHT":
                place[0]+=1
            elif c=='LEFT':
                place[0]-=1
        return (place[1]*n)+place[0]