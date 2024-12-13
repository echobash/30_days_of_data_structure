class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        if 0 <= x <= 9:
            return True

        x = str(x)
        n = len(x)
        left = 0
        right = n-1

        while left <= right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1
        return True


solution = Solution()
num_with_odd_no_of_digits = 1245421
print(num_with_odd_no_of_digits, solution.isPalindrome(num_with_odd_no_of_digits))

num_with_even_no_of_digits = 12455421
print(num_with_even_no_of_digits, solution.isPalindrome(num_with_even_no_of_digits))

num_not_palindrome = 15455421
print(num_not_palindrome, solution.isPalindrome(num_not_palindrome))