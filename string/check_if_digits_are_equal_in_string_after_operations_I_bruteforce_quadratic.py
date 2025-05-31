class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            while len(s) > 2:
                n = len(s)
                new_s = ""
                for i in range(n-1):
                    new_s += str((int(s[i]) + int(s[i+1])) % 10)
                s = new_s
        return s[0] == s[1]


sol = Solution()

s = "3902"
print(f"{s = }  {sol.hasSameDigits(s) = }")

s = "34789"
print(f"{s = }  {sol.hasSameDigits(s) = }")

s = "242"
print(f"{s = }  {sol.hasSameDigits(s) = }")
