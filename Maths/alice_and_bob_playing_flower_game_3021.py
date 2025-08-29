class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # (mc1 * nc1)//2
        return (m * n)//2


sol = Solution()

n = 3
m = 2
print(f"{n = } | {m = } | {sol.flowerGame(n,m) = }")

n = 1
m = 1
print(f"{n = } | {m = } | {sol.flowerGame(n,m) = }")

n = 4
m = 4
print(f"{n = } | {m = } | {sol.flowerGame(n,m) = }")

