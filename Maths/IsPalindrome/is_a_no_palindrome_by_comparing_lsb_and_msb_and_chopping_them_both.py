import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x >= 0 and x <= 9:
            return True

        # get no of digits in the given no x
        n = math.floor(math.log10(x)+1)

        while(x > 0):
            lsb = x % 10
            msb = x // (10 ** (n-1))

            if lsb != msb:
                return False

            # Chop used msb
            x = x % (10 ** (n-1))

            # Chop used lsb
            x = x // 10

            n = n - 2

        return True


solution = Solution()
num_with_odd_no_of_digits = 1245421
print(num_with_odd_no_of_digits, solution.isPalindrome(num_with_odd_no_of_digits))

num_with_even_no_of_digits = 12455421
print(num_with_even_no_of_digits, solution.isPalindrome(num_with_even_no_of_digits))

num_not_palindrome = 15455421
print(num_not_palindrome, solution.isPalindrome(num_not_palindrome))