class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum = 0
        for digit in str(x):
            sum += int(digit)

        return sum if x % sum == 0 else -1


sol = Solution()

x = 18
print(x,sol.sumOfTheDigitsOfHarshadNumber(x))

x = 23
print(x,sol.sumOfTheDigitsOfHarshadNumber(x))