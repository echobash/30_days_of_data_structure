from typing import List


class Solution:
    def is_palindrome(self,word):
        n = len(word)
        for i in range(n // 2):
            if word[i] != word[n - i - 1]:
                return False
        return True

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.is_palindrome(word) == True:
                return word
        return ""


sol = Solution()

words = ["abc","car","ada","racecar","cool"]
print(f"{words = }  {sol.firstPalindrome(words) = }")

words = ["notapalindrome","racecar"]
print(f"{words = }  {sol.firstPalindrome(words) = }")

words = ["def","ghi"]
print(f"{words = }  {sol.firstPalindrome(words) = }")
