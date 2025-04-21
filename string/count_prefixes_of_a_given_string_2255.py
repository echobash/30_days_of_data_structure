from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        total_count = 0
        for word in words:
            if s.startswith(word):
                total_count += 1
        return total_count


sol = Solution()

words = ["a","b","c","ab","bc","abc"]
s = "abc"
print(f"{words = } {s = } {sol.countPrefixes(words, s) = }")

words = ["a","a"]
s = "aa"
print(f"{words = } {s = } {sol.countPrefixes(words, s) = }")

words = ["ab","ax"]
s = "dd"
print(f"{words = } {s = } {sol.countPrefixes(words, s) = }")