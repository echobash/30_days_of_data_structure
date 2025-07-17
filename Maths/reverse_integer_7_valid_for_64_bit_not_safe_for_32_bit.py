class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False

        if 0 <= x <= 9:
            return x

        if x < 0:
            is_negative = True
            x *= -1

        final_number = 0
        while x != 0:
            final_number = final_number * 10 + x % 10
            x //= 10
        final_number = -1 * final_number if is_negative else final_number
        return final_number if -2 ** 31 <= final_number <= 2 ** 31 - 1 else 0


sol = Solution()

x = 123
print(f"{x = } {sol.reverse(x) = }")

x = -123
print(f"{x = } {sol.reverse(x) = }")

x = 120
print(f"{x = } {sol.reverse(x) = }")

x = 8
print(f"{x = } {sol.reverse(x) = }")