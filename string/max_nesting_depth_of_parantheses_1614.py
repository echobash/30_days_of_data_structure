class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth = 0
        for character in s:
            if character == "(":
                depth += 1
            elif character == ")":
                max_depth = max(max_depth, depth)
                depth -= 1
        return max_depth


sol = Solution()

s = "(1+(2*3)+((8)/4))+1"
print(f"{s = }  {sol.maxDepth(s) = }")

s = "(1)+((2))+(((3)))"
print(f"{s = }  {sol.maxDepth(s) = }")

Input: s = "()(())((()()))"
print(f"{s = }  {sol.maxDepth(s) = }")
