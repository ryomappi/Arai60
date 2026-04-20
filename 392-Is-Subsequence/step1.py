class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        for c in t:
            if ptr >= len(s):
                break
            if s[ptr] == c:
                ptr += 1
        if ptr != len(s):
            return False
        else:
            return True
