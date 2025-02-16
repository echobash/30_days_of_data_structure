class Solution:
    def finalString(self, s: str) -> str:
        result = []
        for i in range(len(s)):
            if s[i] == 'i':
                result = result[::-1]
            else:
                result.append(s[i])
        return "".join(result)


sol = Solution()

s = "string"
print(f"{s = }  {sol.finalString(s) = }")

s = "poiinter"
print(f"{s = }  {sol.finalString(s) = }")

