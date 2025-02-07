from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first_word = ''
        second_word = ''

        for word in word1:
            first_word += word

        for word in word2:
            second_word += word

        return first_word == second_word


sol = Solution()

word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(word1,word2, sol.arrayStringsAreEqual(word1, word2))
