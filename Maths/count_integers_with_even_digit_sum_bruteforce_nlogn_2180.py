class Solution:
    def isDigitSumEven(self, x):
        sum_of_digits = 0
        while x > 0:
            sum_of_digits += x % 10
            x //= 10
        return sum_of_digits % 2 == 0

    def countEven(self, num: int) -> int:
        count = 0
        for i in range(1, num + 1):
            if self.isDigitSumEven(i):
                count += 1
        return count


sol = Solution()

n = 4
print(f"{n = } {sol.countEven(n) = }")

n = 30
print(f"{n = } {sol.countEven(n) = }")

n = 324
print(f"{n = } {sol.countEven(n) = }")

n = 116
print(f"{n = } {sol.countEven(n) = }")