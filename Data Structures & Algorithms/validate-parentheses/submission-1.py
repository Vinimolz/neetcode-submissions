class Solution:
    def isValid(self, s: str) -> bool:
        p_stack = []

        opening = {"(", "[", "{"}
        
        matches = {")": "(",
                   "]": "[",
                   "}": "{"}
        

        for i in range(len(s)):
            if s[i] in opening:
                p_stack.append(s[i])
                continue
            
            if len(p_stack) != 0 and p_stack[-1] == matches.get(s[i]):
                p_stack.pop()
                continue
            
            return False
        return len(p_stack) == 0
