class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = [0] * 26
        window = [0] * 26

        for c in s1:
            target[ord(c) - ord('a')] += 1

        for c in s2[:len(s1)]:
            window[ord(c) - ord('a')] += 1

        if window == target:
            return True

        left = 0

        for right in range(len(s1), len(s2)):
            outgoing = ord(s2[left]) - ord('a')
            incoming = ord(s2[right]) - ord('a')

            window[outgoing] -= 1
            window[incoming] += 1

            left += 1

            if window == target:
                return True

        return False
