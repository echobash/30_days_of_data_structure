from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            valid = 1
            for char in word:
                if char not in allowed:
                    valid = 0
                    break
            if valid == 1:
                count += 1
        return count


sol = Solution()

allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
print(words, allowed, sol.countConsistentStrings(allowed,words))

allowed = "abc"
words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
print(words, allowed, sol.countConsistentStrings(allowed,words))

allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
print(words, allowed, sol.countConsistentStrings(allowed,words))
