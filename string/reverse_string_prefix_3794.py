class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:]


sol = Solution()

s = "abcd"
k = 2
print(f"{s = } {k = } {sol.reversePrefix(s, k) = }")

s = "xyz"
k = 3
print(f"{s = } {k = } {sol.reversePrefix(s, k) = }")

s = "hey"
k = 1
print(f"{s = } {k = } {sol.reversePrefix(s, k) = }")
