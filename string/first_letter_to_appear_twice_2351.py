from collections import defaultdict


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        string_count_mapping = defaultdict(int)
        for character in s:
            string_count_mapping[character] += 1
            if string_count_mapping[character] == 2:
                return character


sol = Solution()

s = "abccbaacz"
print(s, sol.repeatedCharacter(s))

s = "abcdd"
print(s, sol.repeatedCharacter(s))
