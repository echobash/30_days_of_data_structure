from typing import List
from collections import Counter


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        string_count_mapping = Counter(s)
        return len(set(string_count_mapping.values())) == 1


sol = Solution()

s = "abacbc"
print(s, sol.areOccurrencesEqual(s))

s = "aaabb"
print(s, sol.areOccurrencesEqual(s))
