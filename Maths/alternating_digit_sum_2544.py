class Solution:
    def alternateDigitSum(self, n: int) -> int:
        no_string = str(n)
        length = len(no_string)
        total_sum = 0
        for i in range(length):
            total_sum += int(no_string[i]) * ((-1) ** i)
        return total_sum


sol = Solution()

n = 521
print(f"{n = } {sol.alternateDigitSum(n) = }")

n = 111
print(f"{n = } {sol.alternateDigitSum(n) = }")

n = 886996
print(f"{n = } {sol.alternateDigitSum(n) = }")