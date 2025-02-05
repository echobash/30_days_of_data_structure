from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        if Counter(s1) != Counter(s2):
            return False

        mismatch_character_count = 0
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                mismatch_character_count += 1
        return mismatch_character_count == 2


sol = Solution()

s1 = "bank"
s2 = "kanb"
print(f" {s2 =} | {s2 =} | {sol.areAlmostEqual(s1, s2) =}")

s1 = "attack"
s2 = "defend"
print(f" {s2 =} | {s2 =} | {sol.areAlmostEqual(s1, s2) =}")

s1 = "kelb"
s2 = "kelb"
print(f" {s2 =} | {s2 =} | {sol.areAlmostEqual(s1, s2) =}")

s1 = "caa"
s2 = "aaz"
print(f" {s2 =} | {s2 =} | {sol.areAlmostEqual(s1, s2) =}")

