from typing import List
from collections import Counter


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1 + " " +s2
        word_count_mapping = Counter(s.split())

        result = []
        for word, word_count in word_count_mapping.items():
            if word_count == 1:
                result.append(word)
        return result


sol = Solution()

s1 = "this apple is sweet"
s2 = "this apple is sour"
print(s1,s2, sol.uncommonFromSentences(s1, s2))

s1 = "apple apple"
s2 = "banana"
print(s1,s2, sol.uncommonFromSentences(s1, s2))
