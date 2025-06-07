from typing import List
from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, k = len(s2), len(s1)

        if n < k or n * k == 0:
            return False

        result = []
        s1_freq_mapping = defaultdict(int)
        s2_freq_mapping = defaultdict(int)

        # Maintain the count dictionary for the input s1 string
        for char in s1:
            s1_freq_mapping[char] += 1

        # Rest windows
        for i in range(n):
            if i >= k:
                # Remove (i-k)th char from s2
                s2_freq_mapping[s2[i - k]] -= 1

                if s2_freq_mapping[s2[i - k]] == 0:
                    del s2_freq_mapping[s2[i - k]]

            # Add i-th char into s2
            s2_freq_mapping[s2[i]] += 1

            if i >= k - 1 and s2_freq_mapping == s1_freq_mapping:
                return True
        return False


sol = Solution()

s1 = "ab"
s2 = "eidbaooo"
print(f"{s1 = } {s2 = } {sol.checkInclusion(s1, s2) = }")

s2= "abab"
s1 = "ab"
print(f"{s2 = } {s1 = } {sol.checkInclusion(s1, s2) = }")

s2= "ba"
s1 = "ab"
print(f"{s2 = } {s1 = } {sol.checkInclusion(s1, s2) = }")

s2= "bx"
s1 = "ab"
print(f"{s2 = } {s1 = } {sol.checkInclusion(s1, s2) = }")

s2= "x"
s1 = "x"
print(f"{s2 = } {s1 = } {sol.checkInclusion(s1, s2) = }")

s2= "x"
s1 = "y"
print(f"{s2 = } {s1 = } {sol.checkInclusion(s1, s2) = }")

s2= "abab"
s1 = "a"
print(f"{s2 = } {s1 = } {sol.checkInclusion(s1, s2) = }")

s2= ""
s1 = "a"
print(f"{s2 = } {s1 = } {sol.checkInclusion(s1, s2) = }")

s2= "a"
s1 = ""
print(f"{s2 = } {s1 = } {sol.checkInclusion(s1, s2) = }")
