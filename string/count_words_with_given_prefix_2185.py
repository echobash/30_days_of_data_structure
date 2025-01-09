from typing import List


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        total_count = 0
        for word in words:
            if word.startswith(pref):
                total_count += 1
        return total_count


sol = Solution()

words = ["pay","attention","practice","attend"]
pref = "at"
print(words,pref, sol.prefixCount(words,pref))

words = ["leetcode","win","loops","success"]
pref = "code"
print(words,pref, sol.prefixCount(words,pref))

