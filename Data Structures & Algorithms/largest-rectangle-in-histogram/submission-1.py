class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        countableHeights = []
        res = 0

        for height in heights:
            barMax = 0
            countableHeights.append(height)

            # Update countableHeights
            for index in reversed(range(len(countableHeights) - 1)):
                if countableHeights[index] > height:
                    countableHeights[index] = height
                else:
                    break
            # print(countableHeights)
            for index in reversed(range(len(countableHeights), )):
                if index == 0:
                    barMax = max(countableHeights[index] * (len(countableHeights)-index), barMax)
                    break

                # Identify Corner
                if countableHeights[index - 1] < countableHeights[index]:
                    barMax = max(countableHeights[index] * (len(countableHeights)-index), barMax)
            res = max(barMax, res)
        return res

        