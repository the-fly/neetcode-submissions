class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            # print(s)
            res += s
            res += "\n"
        # print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        currStr = ""
        for c in s:
            # print(3, currStr, c)
            if c == "\n":
                res.append(currStr)
                # print(4, currStr, c)
                currStr = ""
            else:
                currStr += c
        return res
