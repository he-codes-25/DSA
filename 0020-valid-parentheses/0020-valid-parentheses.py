class Solution:
    def isValid(self, s: str) -> bool:
        openn=[]
        for i in s:
            if i in '({[':
                openn.append(i)
            else:
                if not openn:
                    return False

                if openn[-1]=='[' and i!=']':
                    return False
                elif openn[-1]=='{' and i!='}':
                    return False
                elif openn[-1]=='(' and i!=')':
                    return False
                else:
                    openn.pop()
        return not openn
