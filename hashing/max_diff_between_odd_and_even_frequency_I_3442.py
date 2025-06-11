from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        s_freq = Counter(s)

        max_odd_freq = 0
        min_odd_freq = len(s)

        for freq in s_freq.values():
            if freq % 2 == 1 and freq > max_odd_freq:
                max_odd_freq = freq

            if freq % 2 == 0 and freq < min_odd_freq:
                min_odd_freq = freq
        return max_odd_freq - min_odd_freq


sol = Solution()

s = "aaaaabbc"
print(f" {s = } | {sol.maxDifference(s) = }")

s = "abcabcab"
print(f" {s = } | {sol.maxDifference(s) = }")

s = "aaaabbb"
print(f" {s = } | {sol.maxDifference(s) = }")
