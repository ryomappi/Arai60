class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # Skip whitespaces
        while i < n and s[i] == " ":
            i += 1

        # Get sign
        sign = 1
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "+":
                sign = 1
            elif s[i] == "-":
                sign = -1
            i += 1

        # Read numbers and convert
        result = ""
        while i < n and s[i].isdigit():
            result += s[i]
            i += 1
        result = int(result) if result else 0
        result = sign * result

        # Rounding
        return max(-(2**31), min(2**31 - 1, result))
