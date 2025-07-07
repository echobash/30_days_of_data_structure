class Solution:
    def clearDigits(self, s: str) -> str:
        result_stack = []
        for char in s:
            if not char.isdigit():
                result_stack.append(char)
            else:
                result_stack.pop()
        return "".join(result_stack)


sol = Solution()

s = "abc"
print(f" {s = } {sol.clearDigits(s) =}")

s = "cb34"
print(f" {s = } {sol.clearDigits(s) =}")

s = ""
print(f" {s = } {sol.clearDigits(s) =}")
