class Solution:
    def isValid(self, s: str) -> bool:

        maps = {']':'[', '}':'{', ')':'('}
        stack = []

        for p in s:
            if p in maps:
                if stack and stack[-1] == maps[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        if stack:
            return False
        
        return True