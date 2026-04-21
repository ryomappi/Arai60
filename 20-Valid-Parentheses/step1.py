from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        closures = deque()
        for c in s:
            if c == "(":
                closures.append(")")
                continue
            elif c == "{":
                closures.append("}")
                continue
            elif c == "[":
                closures.append("]")
                continue

            if len(closures) == 0:
                return False
            if c == closures.pop():
                continue
            else:
                return False

        if len(closures) == 0:
            return True
        else:
            return False
