class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            n = len(s)
            new_s = []
            for i in range(n-1):
                new_s.append(str((int(s[i]) + int(s[i+1])) % 10))
            s = "".join(new_s)
        return s[0] == s[1]


sol = Solution()

s = "3902"
print(f"{s = }  {sol.hasSameDigits(s) = }")

s = "34789"
print(f"{s = }  {sol.hasSameDigits(s) = }")

s = "2345223"
print(f"{s = }  {sol.hasSameDigits(s) = }")

s = "242"
print(f"{s = }  {sol.hasSameDigits(s) = }")
