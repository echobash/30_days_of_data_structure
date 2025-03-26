class Solution:


    def checkString(self, s: str) -> bool:
        return "ba" in s


sol = Solution()

s = "aaabbb"
print(f"{s = }  {sol.checkString(s) = }")

s = "abab"
print(f"{s = }  {sol.checkString(s) = }")

s = "bbb"
print(f"{s = }  {sol.checkString(s) = }")

s = "aaa"
print(f"{s = }  {sol.checkString(s) = }")
