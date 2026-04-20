class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptr = 0
        for c in t:
            if ptr == len(s):
                break
            if s[ptr] == c:
                ptr += 1
        return ptr == len(s)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t_iter = iter(t)
        return all(c in t_iter for c in s)
