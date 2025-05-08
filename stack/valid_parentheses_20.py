class Solution:
    def isValid(self, s: str) -> bool:
        complement_brackets = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        n = len(s)
        if n % 2 != 0:
            return False

        bracket_stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                bracket_stack.append(char)
            else:
                if len(bracket_stack) == 0:
                    return False
                else:
                    if complement_brackets[char] != bracket_stack[-1]:
                        return False
                    else:
                        bracket_stack.pop()
        return len(bracket_stack) == 0


sol = Solution()

s = "()"
print(f" {s = } {sol.isValid(s) =}")

s = "()[]{}"
print(f" {s = } {sol.isValid(s) =}")

s = "(]"
print(f" {s = } {sol.isValid(s) =}")

s = "([])"
print(f" {s = } {sol.isValid(s) =}")

s = ")("
print(f" {s = } {sol.isValid(s) =}")