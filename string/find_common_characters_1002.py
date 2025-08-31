from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first_word_char_freq = Counter(words[0])
        result = []
        n = len(words)
        # b1,e1,l2,a1
        for i in range(1, n):
            temp_char_freq = Counter(words[i])
            for item, freq in first_word_char_freq.items():
                first_word_char_freq[item] = min(temp_char_freq[item], freq)

        for item, freq in first_word_char_freq.items():
            if freq != 0:
                for _ in range(freq):
                    result.append(item)

        return result


sol = Solution()

words = ["bella","label","roller"]
print(f"{words = } |  {sol.commonChars(words) = }")

words = ["cool","lock","cook"]
print(f"{words = } |  {sol.commonChars(words) = }")

words = ["bella"]
print(f"{words = } |  {sol.commonChars(words) = }")
