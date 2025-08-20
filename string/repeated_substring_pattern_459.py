class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]


sol = Solution()

s = "abab"
print(f"{s = } {sol.repeatedSubstringPattern(s) = }")

s = "aba"
print(f"{s = } {sol.repeatedSubstringPattern(s) = }")

s = "abcabcabcabc"
print(f"{s = } {sol.repeatedSubstringPattern(s) = }")
