class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        chars1, chars2 = {}, {}
        # chars2 = {letter: 0 for letter in string.ascii_lowercase}

        s1Size = len(s1)
        s2Size = len(s2)
        if s1Size > s2Size:
            return False
        for c in s1:
            chars1[c] = chars1.get(c,0) + 1

        for i in range(len(s1)):
            chars2[s2[i]] = chars2.get(s2[i], 0) + 1
        if chars2 == chars1:
            return True

        for i in range(s1Size, len(s2)):
            cRem = s2[i-s1Size]
            cAdd = s2[i]
            chars2[cRem] -= 1
            if chars2[cRem] == 0:
                chars2.pop(cRem)
            chars2[cAdd] = chars2.get(cAdd, 0) + 1
            if chars2 == chars1:
                return True

        return False



        