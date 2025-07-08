from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        for i in range(left, right + 1):
            if words[i][0] in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'} and words[i][-1] in  {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                count += 1
        return count


sol = Solution()

words = ["are","amy","u"]
left = 0
right = 2
print(f"{words = } {left = } {right = } {sol.vowelStrings(words,left, right) = }")

words = ["hey","aeo","mu","ooo","artro"]
left = 1
right = 4
print(f"{words = } {left = } {right = } {sol.vowelStrings(words,left, right) = }")
