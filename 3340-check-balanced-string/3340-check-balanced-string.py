class Solution:
    def isBalanced(self, num: str) -> bool:
        if sum(list(map(int,num[::2])))==sum(list(map(int,num[1::2]))):
            return True
        return False