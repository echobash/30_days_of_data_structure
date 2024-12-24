class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
                if count == k:
                    return i

        return -1


n = 12
k = 3
sol = Solution()

print(n,sol.kthFactor(n, k))

n = 7
k = 2
print(n,sol.kthFactor(n, k))

n = 4
k = 4
print(n,sol.kthFactor(n, k))

n = 100
k = 8
print(n,sol.kthFactor(n, k))