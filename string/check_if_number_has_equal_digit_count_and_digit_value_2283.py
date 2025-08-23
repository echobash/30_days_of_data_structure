from collections import defaultdict


class Solution:
    def digitCount(self, num: str) -> bool:
        digit_freq = defaultdict(int)
        for digit in num:
            digit_freq[int(digit)] += 1

        for i, digit in enumerate(num):
            if digit_freq[i] != int(digit):
                return False
        return True


sol = Solution()

num = "1210"
print(f"{num = } {sol.digitCount(num) = }")

num = "030"
print(f"{num = } {sol.digitCount(num) = }")

num = "1210"
print(f"{num = } {sol.digitCount(num) = }")

num = "1230"
print(f"{num = } {sol.digitCount(num) = }")
