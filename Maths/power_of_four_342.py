class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True

        if n <= 0:
            return False

        while n > 1:
            if n % 4 != 0:
                return False
            n //= 4

        return True


sol = Solution()

n = 256
print(f"{n = } | {sol.isPowerOfFour(n) = }")

n = 24
print(f"{n = } | {sol.isPowerOfFour(n) = }")

n = -1
print(f"{n = } | {sol.isPowerOfFour(n) = }")
