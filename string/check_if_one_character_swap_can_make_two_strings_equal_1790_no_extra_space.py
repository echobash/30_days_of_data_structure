from collections import Counter


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        mismatch_character_count = 0
        first_mismatching_char = ''
        second_mismatching_char = ''
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                mismatch_character_count += 1
                if mismatch_character_count == 1:
                    first_mismatching_char = s1[i]
                    second_mismatching_char = s2[i]
                else:
                    if s1[i] != second_mismatching_char or s2[i] != first_mismatching_char:
                        return False
                if mismatch_character_count > 2:
                    return False

        return mismatch_character_count == 2



sol = Solution()

s1 = "bank"
s2 = "kanb"
print(f" {s1 =} | {s2 =} | {sol.areAlmostEqual(s1, s2) =}")

s1 = "attack"
s2 = "defend"
print(f" {s1 =} | {s2 =} | {sol.areAlmostEqual(s1, s2) =}")

s1 = "kelb"
s2 = "kelb"
print(f" {s1 =} | {s2 =} | {sol.areAlmostEqual(s1, s2) =}")

s1 = "caa"
s2 = "aaz"
print(f" {s1 =} | {s2 =} | {sol.areAlmostEqual(s1, s2) =}")

