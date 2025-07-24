class Solution:
    def maxProduct(self, n: int) -> int:
        n = str(n)
        digit_list = []
        for digit in n:
            digit_list.append(int(digit))

        digit_list = sorted(digit_list, reverse=True)
        return digit_list[0] * digit_list[1]


sol = Solution()

n = 31
print(f"{n = } {sol.maxProduct(n) = }")

n = 22
print(f"{n = } {sol.maxProduct(n) = }")

n = 124
print(f"{n = } {sol.maxProduct(n) = }")

n = 10
print(f"{n = } {sol.maxProduct(n) = }")