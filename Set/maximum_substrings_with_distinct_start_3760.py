class Solution:
    def maxDistinct(self, s: str) -> int:
        dist_chars = set()
        for char in s:
            if char not in dist_chars:
                dist_chars.add(char)
        return len(dist_chars)

    """
    Logic - 
    Since we have to find the substrings that begin with distinct letters(chars), it will be same thing as
    calculating no of distinct letters(chars)
    """


sol = Solution()

s = "abab"
print(f"{ s = } {sol.maxDistinct(s) = }")

s = "abcd"
print(f"{ s = } {sol.maxDistinct(s) = }")

s = "abxcdyx"
print(f"{ s = } {sol.maxDistinct(s) = }")