class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1
            count += 1
        return count


sol = Solution()

n = 14
print(n, sol.numberOfSteps(n))

n = 8
print(n, sol.numberOfSteps(n))

n = 123
print(n, sol.numberOfSteps(n))