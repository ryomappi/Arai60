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
