class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(current, open, close):
            if len(current) == 2 * n:
                result.append(current)
                return
            if open < n:
                generate(current + "(", open + 1, close)
            if close < open:
                generate(current + ")", open, close + 1)

        generate("", 0, 0)
        return result

class Solution:
    def __init__(self):
        self.result = []

    def generateParenthesis(self, n: int) -> List[str]:
        self._generate("", 0, 0, n)
        return self.result

    def _generate(self, current, open, close, n):
        if len(current) == 2 * n:
            self.result.append(current)
            return
        if open < n:
            self._generate(current + "(", open + 1, close, n)
        if close < open:
            self._generate(current + ")", open, close + 1, n)
