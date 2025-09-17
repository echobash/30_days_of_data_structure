class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


sol = Solution()

haystack = "sadbutsad"
needle = "sad"
print(f"{haystack = } {needle = } {sol.strStr(haystack, needle) = }")

haystack = "leetcode"
needle = "leeto"
print(f"{haystack = } {needle = } {sol.strStr(haystack, needle) = }")
