class Solution:
    def trap(self, height: List[int]) -> int:
        res, max_val, volume = 0, 0, 0
        for i in height:
            if i<max_val:
                volume += max_val - i
            if i>=max_val:
                res+=volume
                volume = 0
                max_val = i
        max_val, volume = 0, 0
        for i in reversed(height):
            if i<max_val:
                volume += max_val - i
            if i>max_val:
                res+=volume
                volume = 0
                max_val = i
        return res



        