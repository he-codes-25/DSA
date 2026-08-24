class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        for i in s:
            if i.isalpha():
                stack.append(i)
            else:
                stack.pop()
        if stack:
            return "".join(stack)
        return ''
