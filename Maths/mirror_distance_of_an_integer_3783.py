class Solution:
    def mirrorDistance(self, n: int) -> int:
        return abs(int(str(n)[::-1]) - n)


sol = Solution()

n = 25
print(f"{n = } | {sol.mirrorDistance(n) = }")

n = 5
print(f"{n = } | {sol.mirrorDistance(n) = }")

n = 10
print(f"{n = } | {sol.mirrorDistance(n) = }")

n = 13
print(f"{n = } | {sol.mirrorDistance(n) = }")

n = 14
print(f"{n = } | {sol.mirrorDistance(n) = }")

n = 11
print(f"{n = } | {sol.mirrorDistance(n) = }")

n = 15
print(f"{n = } | {sol.mirrorDistance(n) = }")
