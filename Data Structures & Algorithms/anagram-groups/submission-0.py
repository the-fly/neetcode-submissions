class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        annagramsMap = {}
        for string in strs:
            sortedString = "".join(sorted(string))
            if not sortedString in annagramsMap:
                annagramsMap[sortedString] = [string]
            else:
                annagramsMap[sortedString].append(string)
            # annagramsMap[sortedString] = annagramsMap.get(sortedString, []).append(string)

        result = []
        for item in annagramsMap:
            result.append(annagramsMap[item])

        return result
            