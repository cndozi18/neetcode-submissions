class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = [] # (temp, index)
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stk_temp, stk_idx = stack.pop()
                ans[stk_idx] = i - stk_idx
            stack.append((temp, i))
        return ans