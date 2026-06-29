class Solution:
    def numDecodings(self, s: str) -> int:
        res = 1
        preRes = 0
        pre = "3"
        prePre = "3"

        postSet = set(["0", "1", "2", "3", "4", "5", "6"])
        for char in s:
            temp = res
            if char == "0":
                if pre not in ["1", "2"]:
                    return 0 
                elif prePre in ["1", "2"]:
                    res = preRes
            elif pre == "1" or (pre == "2" and char in postSet):
                if prePre in ["1","2"]:
                    res = res + preRes
                else:
                    res = res + res
            preRes = temp
            prePre = pre
            pre = char
        
        return res

        