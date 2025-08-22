from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            (s[i],s[n-1-i]) = (s[n-1-i],s[i])
        return



sol = Solution()

s = ["h","e","l","l","o"]
print(f"{s = } {sol.reverseString(s) = } { s = }")

s = ["H","a","n","n","a","h"]
print(f"{s = } {sol.reverseString(s) = } { s = }")