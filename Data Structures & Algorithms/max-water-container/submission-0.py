class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(0, len(heights)-1):
            for j in range(i+1, len(heights)):
                volume = (j-i)*min(heights[i], heights[j])
                if volume > res:
                    res = volume
        return res
