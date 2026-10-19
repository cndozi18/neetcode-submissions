class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        count = [0] * 26
        for c in s1:
            i = ord(c) - ord('a')
            count[i] += 1
        size = len(s1)
        win = [0] * 26
        l, r = 0, size - 1
        for c in s2[:size]:
            i = ord(c) - ord('a')
            win[i] += 1
        while r < len(s2):
            if win == count:
                return True
            prev = ord(s2[l]) - ord('a')
            if r == len(s2) - 1:
                return False
            next = ord(s2[r + 1]) - ord('a')
            win[prev] -= 1
            win[next] += 1
            l += 1
            r += 1
        return False
