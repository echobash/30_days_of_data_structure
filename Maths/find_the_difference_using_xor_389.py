class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        xor = 0
        for char in s + t:
            xor ^= ord(char)

        return chr(xor)


s = "abcd"
t = "abcde"
sol = Solution()

print(sol.find_the_difference(s, t))

s = 'abab'
t = "ababb"
print(sol.find_the_difference(s, t))

s = ""
t = "x"
print(sol.find_the_difference(s, t))