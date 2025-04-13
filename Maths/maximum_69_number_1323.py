class Solution:
    def maximum69Number(self, num: int) -> int:
        # 6 <= num <= 9999
        digits = list(str(num))
        n = len(digits)

        # Keep each digit in list as string
        # iterating on each digit, left to right.
        # As soon as you find a 6, make it 9 and exit the loop
        # Return after joining the digits and typecasting into int

        for i in range(n):
            if digits[i] == '6':
                digits[i] = '9'
                break

        return int("".join(digits))


sol = Solution()

num = 9669
print(f"{num = } {sol.maximum69Number(num) = }")

num = 9999
print(f"{num = } {sol.maximum69Number(num) = }")

n = 9996
print(f"{num = } {sol.maximum69Number(num) = }")