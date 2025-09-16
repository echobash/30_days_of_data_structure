from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1_freq = Counter(words1)
        words2_freq = Counter(words2)

        count = 0

        for word, freq in words1_freq.items():
            if freq == 1 and words2_freq[word] == 1:
                count += 1

        return count


sol = Solution()

words1 = ["leetcode","is","amazing","as","is"]
words2 = ["amazing","leetcode","is"]
print(f"{words1 = } {words2 = } {sol.countWords(words1, words2) = }")

words1 = ["b","bb","bbb"]
words2 = ["a","aa","aaa"]
print(f"{words1 = } {words2 = } {sol.countWords(words1, words2) = }")

words1 = ["a","ab"]
words2 = ["a","a","a","ab"]
print(f"{words1 = } {words2 = } {sol.countWords(words1, words2) = }")
