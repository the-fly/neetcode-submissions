class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # smallest index with largest height

        if len(text2) > len(text1):
            text1, text2 = text2, text1
        
        len1, len2 = len(text1), len(text2)

        subLength = [0 for _ in range(len1)]

        for index2 in range(len2):
            longestSubSeq = 0
            
            for index1 in range(len1):
                if text1[index1] != text2[index2]:
                    longestSubSeq = max(subLength[index1], longestSubSeq)
                    continue
                # print(index1, index2, longestSubSeq)
                if longestSubSeq + 1 > subLength[index1]:
                    subLength[index1] = longestSubSeq + 1
                else: longestSubSeq = subLength[index1]
                # else:
                #     subLength[index1] += 1
            # print (subLength)
        return max(subLength)
                
                
                
