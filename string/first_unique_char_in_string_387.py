from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_freq = Counter(s)
        for i,char in enumerate(s):
            if char_freq[char] == 1:
                return i
        return -1


sol = Solution()

s = "leetcode"
print(f"{s = } {sol.firstUniqChar(s) = }")

s = "loveleetcode"
print(f"{s = } {sol.firstUniqChar(s) = }")

s = "aabb"
print(f"{s = } {sol.firstUniqChar(s) = }")
