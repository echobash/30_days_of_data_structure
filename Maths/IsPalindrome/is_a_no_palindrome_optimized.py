class Solution:
    def is_palindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if 0 <= x <= 9:
            return True

        if x % 10 == 0:
            return False

        # Reverse second half and keep decreasing the no so that by the time we get the reversed second half,
        # we have the first no reduced to half too.

        # Key intuition is that we need two halves basically. if reversed no > remaining half in the loop,
        # it means the reversed_no has more no of digits than first half and it means half is already been
        # reached/crossed

        reversed_no = 0

        while x > reversed_no:
            reversed_no = reversed_no * 10 + x % 10
            # chop the reversed digit from the original no
            x = x // 10

        return x == reversed_no or (x == reversed_no // 10)


solution = Solution()
num_with_odd_no_of_digits = 1245421
print(num_with_odd_no_of_digits, solution.is_palindrome(num_with_odd_no_of_digits))

num_with_even_no_of_digits = 12455421
print(num_with_even_no_of_digits, solution.is_palindrome(num_with_even_no_of_digits))

num_not_palindrome = 15455421
print(num_not_palindrome, solution.is_palindrome(num_not_palindrome))
