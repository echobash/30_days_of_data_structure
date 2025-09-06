class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n <= 4:
            return 0

        count = 0
        while n >= 5:
            n //= 5
            count += n
        return count


sol = Solution()

n = 3
print(f"{n = } | {sol.trailingZeroes(n) = }")

n = 5
print(f"{n = } | {sol.trailingZeroes(n) = }")

n = 0
print(f"{n = } | {sol.trailingZeroes(n) = }")

n = 10
print(f"{n = } | {sol.trailingZeroes(n) = }")

n = 15
print(f"{n = } | {sol.trailingZeroes(n) = }")
