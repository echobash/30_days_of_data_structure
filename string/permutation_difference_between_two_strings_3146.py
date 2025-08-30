class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        s_index_mapping = dict()
        result = 0

        for i, char in enumerate(s):
            s_index_mapping[char] = i

        for i, char in enumerate(t):
            result += abs(i - s_index_mapping[char])

        return result


sol = Solution()

s = "abc"
t = "bac"
print(f"{s = } | {t = }|   {sol.findPermutationDifference(s, t) = }")

s = "abcde"
t = "edbac"
print(f"{s = } | {t = }|   {sol.findPermutationDifference(s, t) = }")

s = "p"
t = "p"
print(f"{s = } | {t = }|   {sol.findPermutationDifference(s, t) = }")
