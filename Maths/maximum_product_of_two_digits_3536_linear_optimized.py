from collections import defaultdict


class Solution:
    def maxProduct(self, n: int) -> int:
        digit_freq = defaultdict(int)

        while n > 0:
            digit_freq[n % 10] += 1
            n //= 10

        product = 1
        count = 0
        for i in range(9, -1, -1):
            if digit_freq[i] == 0:
                continue
            elif digit_freq[i] >= 2:
                if count == 0:
                    return i * i
                else:
                    product *= i
                    count += 1
            else:
                product *= i
                count += 1
            if count == 2:
                return product


sol = Solution()

n = 31298429
print(f"{n = } {sol.maxProduct(n) = }")

n = 22
print(f"{n = } {sol.maxProduct(n) = }")

n = 324
print(f"{n = } {sol.maxProduct(n) = }")

n = 116
print(f"{n = } {sol.maxProduct(n) = }")