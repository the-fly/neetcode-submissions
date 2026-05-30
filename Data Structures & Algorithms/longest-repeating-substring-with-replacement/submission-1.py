class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, buffer = 1, 0
        for i in range(len(s)):
            buffer = k
            size = 1
            j = i + 1
            while j<len(s) and (s[j] == s[i] or buffer >0):
                size += 1
                if not s[j] == s[i]:
                    buffer -= 1
                j += 1
            res = max(res, min(size + buffer, len(s)))
        return res
