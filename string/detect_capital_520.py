from typing import List


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.isupper():
            return True

        n = len(word)
        for i, char in enumerate(word):
            if char.isupper() and i != 0:
                return False
        return True


sol = Solution()

word = "USA"
print(f"{word = } {sol.detectCapitalUse(word) = }")

word = "FlaG"
print(f"{word = } {sol.detectCapitalUse(word) = }")

word = "A"
print(f"{word = } {sol.detectCapitalUse(word) = }")

word = "h"
print(f"{word = } {sol.detectCapitalUse(word) = }")