class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [""] * numRows
        curRow = 0
        goingDown = True

        for c in s:
            rows[curRow] += c
            if curRow == numRows - 1:
                goingDown = False
            elif curRow == 0:
                goingDown = True
            curRow += 1 if goingDown else -1

        return "".join(rows)
