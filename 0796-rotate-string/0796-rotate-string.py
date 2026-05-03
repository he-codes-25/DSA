class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ans=list(s)
        for i in s:
            ans.remove(i)
            ans.append(i)
            if ans==list(goal):
                return True
        return False