# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         countableHeights = []
#         res = 0

#         for height in heights:
#             barMax = 0
#             countableHeights.append(height)

#             # Update countableHeights
#             for index in reversed(range(len(countableHeights) - 1)):
#                 if countableHeights[index] > height:
#                     countableHeights[index] = height
#                 else:
#                     break
#             # print(countableHeights)
#             for index in reversed(range(len(countableHeights), )):
#                 if index == 0:
#                     barMax = max(countableHeights[index] * (len(countableHeights)-index), barMax)
#                     break

#                 # Identify Corner
#                 if countableHeights[index - 1] < countableHeights[index]:
#                     barMax = max(countableHeights[index] * (len(countableHeights)-index), barMax)
#             res = max(barMax, res)
#         return res

# Better Solution
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # Stores pairs of (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            # If the current bar is shorter than the stack's top bar, 
            # we must pop and calculate areas.
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                # Calculate area with the popped height as the shortest bar
                max_area = max(max_area, height * (i - idx))
                # The current bar can extend backwards to the popped bar's index
                start = idx
                
            stack.append((start, h))
            
        # Calculate area for any remaining bars in the stack
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
            
        return max_area
        