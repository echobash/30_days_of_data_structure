class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        ascii_sum = 0
        for i in range(n-1):
            ascii_sum += abs(ord(s[i]) - ord(s[i+1]))
        return ascii_sum


sol = Solution()

s = "hello"
print(s, sol.scoreOfString(s))

s = "zaz"
print(s, sol.scoreOfString(s))
