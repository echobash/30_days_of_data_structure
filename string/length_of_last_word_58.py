class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s[::-1]
        first_space_from_left = -1
        n = len(s)
        if n == 1:
            return n

        for i in range(n):
            if s[i] == ' ':
                return i
            elif i == n - 1:
                return n


sol = Solution()

s = "Hello World"
print(f"{s = } {sol.lengthOfLastWord(s) = }")

s = "   fly me   to   the moon  "
print(f"{s = } {sol.lengthOfLastWord(s) = }")

s = "luffy is still joyboy"
print(f"{s = } {sol.lengthOfLastWord(s) = }")

s = "a"
print(f"{s = } {sol.lengthOfLastWord(s) = }")

s = "y"
print(f"{s = } {sol.lengthOfLastWord(s) = }")

s = "    day"
print(f"{s = } {sol.lengthOfLastWord(s) = }")

s = "n b n"
print(f"{s = } {sol.lengthOfLastWord(s) = }")
