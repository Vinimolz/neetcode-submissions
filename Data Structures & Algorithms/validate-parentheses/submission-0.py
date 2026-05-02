class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        paren_matcher = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in s:

            if char in paren_matcher.values():
                stack.append(char)
                continue

            if len(stack) != 0 and stack[-1] == paren_matcher[char]:
                stack.pop()
            else:
                return False

        return len(stack) == 0          
        