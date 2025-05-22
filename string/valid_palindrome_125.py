class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string_chars = []
        n = len(s)
        for char in s:
            if char.isalnum():
                new_string_chars.append(char.lower())
        new_string = "".join(new_string_chars)
        return new_string == new_string[::-1]


sol = Solution()

s = "A man, a plan, a canal: Panama"
print(f"{s = } {sol.isPalindrome(s) = }")

s = "race a car"
print(f"{s = } {sol.isPalindrome(s) = }")

s = " "
print(f"{s = } {sol.isPalindrome(s) = }")

s = "0P"
print(f"{s = } {sol.isPalindrome(s) = }")
