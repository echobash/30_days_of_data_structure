from collections import defaultdict


class Solution:
    def find_the_difference(self, s: str, t: str) -> str:
        # if s is empty and t has only character. It means t is what was added
        if len(t) == 1:
            return t

        larger_string_count_mapping = defaultdict(int)
        smaller_string_count_mapping = defaultdict(int)

        for char in t:
            larger_string_count_mapping[char] += 1

        for char in s:
            smaller_string_count_mapping[char] += 1

        for key, count in larger_string_count_mapping.items():
            if count != smaller_string_count_mapping[key]:
                return key


s = "abcd"
t = "abcde"
sol = Solution()

print(sol.find_the_difference(s, t))

s = 'abab'
t = "ababb"
print(sol.find_the_difference(s, t))

s = ""
t = "x"
print(sol.find_the_difference(s, t))