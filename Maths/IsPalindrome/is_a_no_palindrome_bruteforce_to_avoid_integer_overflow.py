import math


class Solution:
    def get_reverse_no(self, num):
        reversed_no = 0
        while num > 0:
            rem = num % 10
            num = num // 10
            reversed_no = reversed_no * 10 + rem
        return reversed_no

    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x >= 0 and x <= 9:
            return True

        n = math.floor(math.log10(x)) + 1

        # If we reverse the complete the full integer no then it's possible that the reverse no can be
        # causing integer overflow.
        # e.g x = 2^31 -1 is the constraint in this question and also biggest integer of 32 bit
        # 2^31 -1 = 2,147,483,647 (10 digit no) and reverse of it will be 7,463,847,412
        # But we can't store 7,463,847,412 into an integer variable
        # Same with any random no e.g 1,000,000,006 will again cause integer overflow.

        # So instead of reversing complete no, we can reverse half of the no and compare it with other half
        # And we won't get any integer overflow as reversing a 5 digit will never cause integer overflow

        # 12455421
        # If n is even i.e even no of digits - do this
        # Get first half of the no by dividing 10000 for this case i.e by dividing by 10^(n//2)
        # Get second half of the no by taking modulo with 10000 for this case i.e by % by 10^(n//2)

        if n % 2 == 0:
            first_half = x // (10 ** (n // 2))
            first_half = self.get_reverse_no(first_half)
            second_half = x % (10 ** (n // 2))
            if first_half == second_half:
                return True
            return False
        else:
            # 1245421
            # If n is odd i.e odd no of digits - do this
            # Get first half of the no by dividing 10000 for this case i.e by dividing by 10^((n//2)+1)
            # Get second half of the no by taking modulo with 10000 for this case i.e by % by 10^(n//2)
            first_half = x // (10 ** ((n // 2) + 1))
            first_half = self.get_reverse_no(first_half)
            second_half = x % (10 ** (n // 2))
            if first_half == second_half:
                return True
            return False


solution = Solution()
num_with_odd_no_of_digits = 1245421
print(num_with_odd_no_of_digits, solution.isPalindrome(num_with_odd_no_of_digits))

num_with_even_no_of_digits = 12455421
print(num_with_even_no_of_digits, solution.isPalindrome(num_with_even_no_of_digits))

num_not_palindrome = 15455421
print(num_not_palindrome, solution.isPalindrome(num_not_palindrome))