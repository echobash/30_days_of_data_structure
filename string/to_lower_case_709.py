class Solution:
    def toLowerCase(self, s: str) -> str:
        result = []
        for character in s:
            if 65 <= ord(character) <= 90:
                result.append(chr( ord(character) + 32 ))
            else:
                result.append(character)
        return "".join(result)


sol = Solution()

s = "Hello"
print(f"{s = }  {sol.toLowerCase(s) = }")

s = "here"
print(f"{s = }  {sol.toLowerCase(s) = }")

s = "LOVELY"
print(f"{s = }  {sol.toLowerCase(s) = }")
