class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = list(zip(position, speed))
        pos_speed.sort(key=lambda tup: tup[0], reverse=True)
        times = list(map(lambda x: (target - x[0]) / x[1], pos_speed))
        stack = []
        for t in times:
            if not stack:
                stack.append(t)
                continue
            if t <= stack[-1]:
                continue
            else:
                stack.append(t)
        return len(stack)