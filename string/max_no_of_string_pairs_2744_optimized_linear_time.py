from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        pair_count = 0
        n = len(words)
        word_count_mapping = set()

        for word in words:
            if word[::-1] in word_count_mapping and word[::-1] != word:
                pair_count += 1
            else:
                word_count_mapping.add(word)
        return pair_count


sol = Solution()

words = ["cd","ac","dc","ca","zz"]
print(f"{words = } {sol.maximumNumberOfStringPairs(words) = }")

words = ["ab","ba","cc"]
print(f"{words = } {sol.maximumNumberOfStringPairs(words) = }")

words = ["aa","ab"]
print(f"{words = } {sol.maximumNumberOfStringPairs(words) = }")
