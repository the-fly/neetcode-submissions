class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        maxLen = 0
        left = 0
        if len(s) == 0:
            return 0;
        for right in range(0, len(s)):
            if not s[right] in charSet:
                charSet.add(s[right])
                if right == len(s)-1:
                    maxLen = max(maxLen, right+1-left)

            else:
                maxLen = max(maxLen, right-left)
                while not s[left] == s[right]:
                    charSet.remove(s[left])
                    left += 1
                left += 1
        return maxLen



        # for alphabet in s:
        #     if alphabet in charSet:
        #         maxLen = max(currlen,maxLen)
        #         newString = ""
        #         for alphabet2 in currString:
        #             while not alphabet2 == alphabet:
        #                 continue
        #         charSet.clear()
        #         currLen = 0
        #     else:
        #         charSet.add(alphabet)
        #         currlen += 1
        # return maxLen

        