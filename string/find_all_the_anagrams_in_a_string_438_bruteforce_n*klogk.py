from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,k = len(s), len(p)
        result = []

        if k == 0 or p == 0:
            return []

        for i in range(n-k+1):
            curr_substring = []
            for j in range(i, i+k):
                curr_substring.append(s[j])
            if sorted(curr_substring) == sorted(p):
                result.append(i)
        return result


sol = Solution()

s = "cbaebabacd"
p = "abc"
print(f"{s = } {p = } {sol.findAnagrams(s, p) = }")

s = "abab"
p = "ab"
print(f"{s = } {p = } {sol.findAnagrams(s, p) = }")

s = "ba"
p = "ab"
print(f"{s = } {p = } {sol.findAnagrams(s, p) = }")

s = "bx"
p = "ab"
print(f"{s = } {p = } {sol.findAnagrams(s, p) = }")

s = "x"
p = "x"
print(f"{s = } {p = } {sol.findAnagrams(s, p) = }")

s = "x"
p = "y"
print(f"{s = } {p = } {sol.findAnagrams(s, p) = }")

s = "abab"
p = "a"
print(f"{s = } {p = } {sol.findAnagrams(s, p) = }")

s = ""
p = "a"
print(f"{s = } {p = } {sol.findAnagrams(s, p) = }")

s = "a"
p = ""
print(f"{s = } {p = } {sol.findAnagrams(s, p) = }")
