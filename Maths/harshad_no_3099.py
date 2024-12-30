class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum = 0
        old_no = x
        while x > 0:
            sum += x % 10
            x //= 10

        return sum if old_no % sum == 0 else -1


sol = Solution()

x = 18
print(x,sol.sumOfTheDigitsOfHarshadNumber(x))

x = 23
print(x,sol.sumOfTheDigitsOfHarshadNumber(x))