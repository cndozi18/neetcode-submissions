from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        mid = 0
        while l <= r:
            mid = (l + r) // 2
            time = 0
            for pile in piles:
                time += ceil(float(pile) / mid)
            if time > h:
                l = mid + 1
            else:
                res = mid
                r = mid - 1
        return res
        