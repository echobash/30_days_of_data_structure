from typing import List


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count


sol = Solution()

patterns = ["a","abc","bc","d"]
word = "abc"
print(f"{patterns = } { word = } {sol.numOfStrings(patterns, word) = }")

patterns = ["a","b","c"]
word = "aaaaabbbbb"
print(f"{patterns = } { word = } {sol.numOfStrings(patterns, word) = }")

patterns = ["a","a","a"]
word = "ab"
print(f"{patterns = } { word = } {sol.numOfStrings(patterns, word) = }")
