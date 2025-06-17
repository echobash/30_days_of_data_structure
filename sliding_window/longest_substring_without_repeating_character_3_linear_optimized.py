class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_length = 0
        left = 0
        char_set = set()

        # Start iterating s from i = 0 to n
        # if s[i] not in set - curr_length = len(set), update max_length
        # else: - while s[i] in set, remove s[left] from set and set curr_length = len(set), left +=1 and
        # add s[i] in set

        for i in range(n):
            while s[i] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[i])
            max_length = max(max_length, i - left + 1)
        return max_length



sol = Solution()

s = "abcabcbb"
print(f"{s = } {sol.lengthOfLongestSubstring(s) = }")

s = "bbbbb"
print(f"{s = } {sol.lengthOfLongestSubstring(s) = }")

s = "pwwkew"
print(f"{s = } {sol.lengthOfLongestSubstring(s) = }")

s = "abccbcbb"
print(f"{s = } {sol.lengthOfLongestSubstring(s) = }")

s = "abc dbcbb"
print(f"{s = } {sol.lengthOfLongestSubstring(s) = }")

s = " "
print(f"{s = } {sol.lengthOfLongestSubstring(s) = }")

s = "        "
print(f"{s = } {sol.lengthOfLongestSubstring(s) = }")
