class Solution:
    def theSequence(self, n):
        """
        f(x) = 1 if x = 0
        f(x) = x + x*f(x-1) if x > 0
        """
        if n == 0:
            return 1

        return n + n * self.theSequence(n - 1)


sol = Solution()

n = 3
print(f"{n = } {sol.theSequence(n) = }")

n = 2
print(f"{n = } {sol.theSequence(n) = }")