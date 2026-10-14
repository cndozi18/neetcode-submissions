class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0]
        for i in range(1, len(height)):
            maxL.append(max(height[i - 1], maxL[i - 1]))
        maxR = [0]
        for i in range(len(height) - 2, -1, -1):
            maxR.insert(0, max(height[i + 1], maxR[0]))
        minLR = [min(l, r) for l,r in zip(maxL, maxR)]
        res = 0
        for i in range(len(height)):
            val = minLR[i] - height[i]
            if val > 0:
                res += val
        return res