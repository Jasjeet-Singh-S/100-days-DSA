# https://youtu.be/UuiTKBwPgAo?si=_iBdLgt8Dxl4YtvR

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_ar = 0
        l = 0
        r = len(height)-1
        
        while l<r:
            ar = min(height[l], height[r]) * (r-l)
            if ar>max_ar:
                max_ar = ar
            if height[l]<height[r]:
                l += 1
            else:
                r -= 1
        
        return max_ar