from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq_mapping = Counter(s)
        final_result = []

        sorted_chars = sorted(freq_mapping.keys(), key=lambda ch: freq_mapping[ch], reverse=True)

        for char in sorted_chars:
            final_result.extend(char * freq_mapping[char])

        return "".join(final_result)


sol = Solution()

s = "tree"
print(f"{s = } {sol.frequencySort(s) = }")

s = "cccaaa"
print(f"{s = } {sol.frequencySort(s) = }")

s = "Aabb"
print(f"{s = } {sol.frequencySort(s) = }")
