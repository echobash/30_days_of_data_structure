class Solution:
    def removeStars(self, s: str) -> str:
        char_stack = []
        for char in s:
            if char != '*':
                char_stack.append(char)
            else:
                char_stack.pop()
        return "".join(char_stack)


sol = Solution()

s = "leet**cod*e"
print(f" {s = } {sol.removeStars(s) =}")

s = "erase*****"
print(f" {s = } {sol.removeStars(s) =}")

s = "a*b*c*"
print(f" {s = } {sol.removeStars(s) =}")

s = "e*"
print(f" {s = } {sol.removeStars(s) =}")
