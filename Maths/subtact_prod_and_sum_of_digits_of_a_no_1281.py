class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0

        while n > 0:
            last_digit = n % 10
            n //= 10
            product *= last_digit
            sum += last_digit
        return product - sum


n = 234
sol = Solution()

print(n,sol.subtractProductAndSum(n))

n = 4421
print(n,sol.subtractProductAndSum(n))

n = 223423
print(n,sol.subtractProductAndSum(n))

n = 449421
print(n,sol.subtractProductAndSum(n))
