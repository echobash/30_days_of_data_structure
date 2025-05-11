from collections import defaultdict


class Solution:
    def minDeletion(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        for char in s:
            char_freq[char] += 1

        no_of_unique_chars_to_delete = len(char_freq) - k

        if no_of_unique_chars_to_delete == 0:
            return 0

        sorted_occurences = sorted(list(char_freq.values()))
        count = 0
        for i in range(no_of_unique_chars_to_delete):
            count += sorted_occurences[i]
        return count


sol = Solution()

s = "abc"
k = 2
print(f"{s = } {k = } {sol.minDeletion(s, k) = }")

s = "aabb"
k = 2
print(f"{s = } {k = } {sol.minDeletion(s, k) = }")

s = "yyyzz"
k = 1
print(f"{s = } {k = } {sol.minDeletion(s, k) = }")
