from typing import List
from collections import Counter


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        n = len(s)

        first_half_vowel_count = 0
        for i in range(n // 2):
            if s[i] in vowels:
                first_half_vowel_count += 1

        second_half_vowel_count = 0
        for i in range(n // 2, n):
            if s[i] in vowels:
                second_half_vowel_count += 1
        return second_half_vowel_count == first_half_vowel_count


solution = Solution()

s = "book"
print(s, solution.halvesAreAlike(s))

s = "textbook"
print(s, solution.halvesAreAlike(s))
