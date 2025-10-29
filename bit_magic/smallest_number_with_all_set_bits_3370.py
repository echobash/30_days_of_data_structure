class Solution:
    def smallestNumber(self, n: int) -> int:
        i = n
        while True:
            if i & (i+1) == 0:
                return i
            i += 1


sol = Solution()

n = 5
print(f"{n = } | {sol.smallestNumber(n) = }")

n = 10
print(f"{n = } | {sol.smallestNumber(n) = }")

n = 3
print(f"{n = } | {sol.smallestNumber(n) = }")