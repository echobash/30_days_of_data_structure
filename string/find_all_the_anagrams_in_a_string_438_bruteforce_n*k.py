from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n,k = len(s), len(p)
        result = []
        p_freq_mapping = defaultdict(int)
        for char in p:
            p_freq_mapping[char] += 1

        if k == 0 or p == 0:
            return []

        for i in range(n-k+1):
            s_freq_mapping = defaultdict(int)
            is_anagram = True
            for j in range(i, i+k):
                s_freq_mapping[s[j]] += 1
            for j in range(i, i + k):
                if s_freq_mapping[s[j]] != p_freq_mapping[s[j]]:
                    is_anagram = False
                    break
            if is_anagram:
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
