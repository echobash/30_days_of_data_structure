class Solution:
    def sumBase(self, n: int, k: int) -> int:
        original = n
        ans = ""
        sum_dig = 0
        while n > 0:
            rem = n % k
            n = n//k
            sum_dig += rem
        return sum_dig


sol = Solution()

n = 34
k = 6
print(f"{n = } {k = } {sol.sumBase(n, k) = }")

n = 10
k = 10
print(f"{n = } {k = } {sol.sumBase(n, k) = }")
