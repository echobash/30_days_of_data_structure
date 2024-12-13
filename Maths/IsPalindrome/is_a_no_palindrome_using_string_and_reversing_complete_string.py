class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if x >= 0 and x <= 9:
            return True

        x = str(x)
        if x[::-1] == x:
            return True
        return False


solution = Solution()
num_with_odd_no_of_digits = 1245421
print(num_with_odd_no_of_digits, solution.isPalindrome(num_with_odd_no_of_digits))

num_with_even_no_of_digits = 12455421
print(num_with_even_no_of_digits, solution.isPalindrome(num_with_even_no_of_digits))

num_not_palindrome = 15455421
print(num_not_palindrome, solution.isPalindrome(num_not_palindrome))