from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        max_count = 0
        for i in range(n-k+1):
            vowel_count = 0
            for j in range(i, i+k):
                if s[j] in {'a','e','i','o','u'}:
                    vowel_count += 1
                    max_count = max(max_count, vowel_count)
        return max_count


sol = Solution()

s = "abciiidef"
k = 3
print(f" {s = } | {k = } | {sol.maxVowels(s, k) = }")

s = "aeiou"
k = 2
print(f" {s = } | {k = } | {sol.maxVowels(s, k) = }")

s = "leetcode"
k = 3
print(f" {s = } | {k = } | {sol.maxVowels(s, k) = }")
