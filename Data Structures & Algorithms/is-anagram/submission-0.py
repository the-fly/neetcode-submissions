class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chatCountS = {}
        for chars in s:
            if chars in chatCountS:
                chatCountS[chars] += 1
            else:
                chatCountS[chars] = 1
        for chars in t:
            if chars in chatCountS:
                chatCountS[chars] -= 1
            else:
                return False

        for item in chatCountS:
            if chatCountS[item] !=0:
                return False
        return True