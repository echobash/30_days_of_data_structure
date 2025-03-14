from typing import List


class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            parts = word.split(separator)
            for part in parts:
                if part:
                    result.append(part)
        return result


sol = Solution()

words = ["one.two.three","four.five","six"]
separator = "."
print(f"{words = }  {separator = }  {sol.splitWordsBySeparator(words, separator) = }")

words = ["$easy$","$problem$"]
separator = "$"
print(f"{words = }  {separator = }  {sol.splitWordsBySeparator(words, separator) = }")

words = ["|||"]
separator = "|"
print(f"{words = }  {separator = }  {sol.splitWordsBySeparator(words, separator) = }")
