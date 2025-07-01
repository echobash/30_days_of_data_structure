class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        count = 0
        while num1 != 0 and num2 != 0:
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            count += 1
        return count


sol = Solution()

num1 = 2
num2 = 3
print(f"{num1 = } {num2 = } {sol.countOperations(num1, num2) = }")

num1 = 10
num2 = 10
print(f"{num1 = } {num2 = } {sol.countOperations(num1, num2) = }")
