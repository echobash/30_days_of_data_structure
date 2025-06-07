from typing import List
from collections import defaultdict


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, k = len(s), len(p)

        if n < k or n * k == 0:
            return []

        result = []
        p_freq_mapping = defaultdict(int)
        s_freq_mapping = defaultdict(int)

        # Maintain the count dictionary for the input p string
        for char in p:
            p_freq_mapping[char] += 1

        # Rest windows
        for i in range(n):
            if i >= k:
                # Remove (i-k)th char from s
                s_freq_mapping[s[i - k]] -= 1

                if s_freq_mapping[s[i - k]] == 0:
                    del s_freq_mapping[s[i - k]]

            # Add i-th char into s
            s_freq_mapping[s[i]] += 1

            if i >= k - 1 and s_freq_mapping == p_freq_mapping:
                result.append(i - k + 1)
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
