class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True

        if n <= 0:
            return False

        while n > 1:
            if n % 3 != 0:
                return False
            n //= 3

        return True


sol = Solution()

n = 81
print(f"{n = } | {sol.isPowerOfThree(n) = }")

n = 24
print(f"{n = } | {sol.isPowerOfThree(n) = }")

n = -1
print(f"{n = } | {sol.isPowerOfThree(n) = }")
