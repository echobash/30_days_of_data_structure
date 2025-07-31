class Solution:
    def generateTheString(self, n: int) -> str:
        """
        n = even -> odd+odd
        n = odd -> same char occur n times
        """
        if n % 2 == 0:
            return "a"+(n-1)*"b"
        return "a"*n


sol = Solution()

n = 1
print(f"{n = } {sol.generateTheString(n) = }")

n = 2
print(f"{n = } {sol.generateTheString(n) = }")

n = 3
print(f"{n = } {sol.generateTheString(n) = }")

n = 4
print(f"{n = } {sol.generateTheString(n) = }")

n = 5
print(f"{n = } {sol.generateTheString(n) = }")

n = 468
print(f"{n = } {sol.generateTheString(n) = }")