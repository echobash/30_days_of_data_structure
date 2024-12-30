class Solution:
    def sumOfMultiples(self, n: int) -> int:
        sum = 0
        for i in range(1, n+1):
            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                sum += i
        return sum


sol = Solution()

n = 7
print(n,sol.sumOfMultiples(n))

n = 10
print(n,sol.sumOfMultiples(n))

n = 9
print(n,sol.sumOfMultiples(n))

