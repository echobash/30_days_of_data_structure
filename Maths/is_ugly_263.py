class Solution:
    def is_ugly(self, n: int) -> bool:
        if n == 0:
            return False

        while n % 2 == 0:
            n //= 2

        while n % 3 == 0:
            n //= 3

        while n % 5 == 0:
            n //= 5

        return n == 1


sol = Solution()

n = 6
print(n, sol.is_ugly(n))

n = 1
print(n, sol.is_ugly(n))

n = 14
print(n, sol.is_ugly(n))

n = 0
print(n, sol.is_ugly(n))

