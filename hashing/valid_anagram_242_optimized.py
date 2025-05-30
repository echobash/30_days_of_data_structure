from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_freq = Counter(s)
        for char in t:
            if s_freq[char] == 0:
                return False
            s_freq[char] -= 1
        return True


sol = Solution()

s = "anagram"
t = "nagaram"
print(f"{s =} {t= } {sol.isAnagram(s, t) = }")

s = "rat"
t = "car"
print(f"{s =} {t= } {sol.isAnagram(s, t) = }")

s = "caring"
t = "racing"
print(f"{s =} {t= } {sol.isAnagram(s, t) = }")
