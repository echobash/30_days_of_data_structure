from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first_word = "".join(word1)
        second_word = "".join(word2)
        return first_word == second_word


sol = Solution()

word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(word1,word2, sol.arrayStringsAreEqual(word1, word2))
