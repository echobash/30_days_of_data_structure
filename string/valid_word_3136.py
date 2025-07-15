import string


class Solution:
    def isValid(self, word: str) -> bool:
        n = len(word)
        if n < 3 or not word.isalnum():
            return False

        vowels = set('aeiouAEIOU')
        alphabets = set(string.ascii_letters)  # includes a–z and A–Z
        consonants = alphabets - vowels

        one_vowel = False
        one_consonant = False

        for char in word:
            if char in vowels:
                one_vowel = True
            elif char in consonants:
                one_consonant = True

            if one_vowel and one_consonant:
                return True

        return False


sol = Solution()

word = "234Adas"
print(f"{word = } {sol.isValid(word) = }")

word = "b3"
print(f"{word = } {sol.isValid(word) = }")

word = "a3$e"
print(f"{word = } {sol.isValid(word) = }")
