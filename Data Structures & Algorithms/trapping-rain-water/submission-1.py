class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL = height[l]
        maxR = height[r]
        res = 0
        while l < r:
            if maxL <= maxR:
                l += 1
                val = maxL - height[l]
                if val > 0:
                    res += val
                maxL = max(maxL, height[l])
            else:
                r -= 1
                val = maxR - height[r]
                if val > 0:
                    res += val
                maxR = max(maxR, height[r])
        return res