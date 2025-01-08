from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        result_count = 0
        for i in range(n):
            for j in range(i+1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    result_count += 1
        return result_count


sol = Solution()

words = ["a","aba","ababa","aa"]
print(words, sol.countPrefixSuffixPairs(words))

words = ["pa","papa","ma","mama"]
print(words, sol.countPrefixSuffixPairs(words))

words = ["abab","ab"]
print(words, sol.countPrefixSuffixPairs(words))