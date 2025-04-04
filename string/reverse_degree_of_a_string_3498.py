class Solution:
    def reverseDegree(self, s: str) -> int:
        reverse_alpha_values = {chr(i + 97): 26 - i for i in range(26)}
        n = len(s)
        sum = 0
        for i in range(n):
            sum += (reverse_alpha_values[s[i]] * (i+1))
        return sum


sol = Solution()

s = "abc"
print(f"{s = } {sol.reverseDegree(s) = }")

s = "zaza"
print(f"{s = } {sol.reverseDegree(s) = }")