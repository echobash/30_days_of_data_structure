from typing import List


class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        vowel_count = 0
        max_count = 0
        vowels = {'a','e','i','o','u'}

        # First Window
        for i in range(k):
            if s[i] in vowels:
                vowel_count += 1
        max_count = vowel_count

        # Rest Windows
        for i in range(k, n):
            # Incoming char
            if s[i] in vowels:
                vowel_count += 1

            # Removing First char
            if s[i-k] in vowels:
                vowel_count -= 1
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
