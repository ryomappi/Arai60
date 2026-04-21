class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {")": "(", "}": "{", "]": "["}

        for c in s:
            if c in matching:
                # stack is empty or top of stack is not the matching opening paranthesis
                if not stack or stack[-1] != matching[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)

        # if stack is empty, all parentheses are valid
        return not stack
