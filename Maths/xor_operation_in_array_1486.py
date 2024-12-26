class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = 0
        for i in range(n):
            result ^= start + 2 * i
        return result


sol = Solution()

n = 5
start = 0

print(n, sol.xorOperation(n, start))

n = 4
start = 3
print(n, sol.xorOperation(n, start))
