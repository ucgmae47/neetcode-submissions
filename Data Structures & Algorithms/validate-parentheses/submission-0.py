class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')': '(',
                    '}': '{',
                    ']': '[',}
        stack = []
        for c in s:
            if c in ('(', '{', '['):
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif stack[-1] == mapping[c]:
                stack.pop()
            else:
                return False
        return not stack