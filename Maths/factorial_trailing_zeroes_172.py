class Solution:
    def trailingZeroes(self, n: int) -> int:
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

n = 13
print(f"{n = } | {sol.trailingZeroes(n) = }")

n = 14
print(f"{n = } | {sol.trailingZeroes(n) = }")

n = 11
print(f"{n = } | {sol.trailingZeroes(n) = }")

n = 15
print(f"{n = } | {sol.trailingZeroes(n) = }")
