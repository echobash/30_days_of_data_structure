class Solution:
    def replaceDigits(self, s: str) -> str:
        current_char = ''
        result = ""
        n = len(s)
        i = 0
        while i <= n-1:
            current_char = s[i]
            i += 1
            result += current_char
            if i!= n:
                result += chr(ord(current_char)+int(s[i]))
                i += 1
        return "".join(result)


sol = Solution()

s = "a1c1e1"
print(f"{s = }  {sol.replaceDigits(s) = }")

s = "a1b2c3d4e"
print(f"{s = }  {sol.replaceDigits(s) = }")

s = "a1b2c3d4"
print(f"{s = }  {sol.replaceDigits(s) = }")

s = "a1"
print(f"{s = }  {sol.replaceDigits(s) = }")
