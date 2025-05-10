from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set('aeiou')
        consonants = set('abcdefghijklmnopqrstuvwxyz') - vowels
        char_freq = Counter(s)
        max_vowel_freq = 0
        max_consonants_freq = 0

        for vowel in vowels:
            if char_freq[vowel] > max_vowel_freq:
                max_vowel_freq = char_freq[vowel]

        for consonant in consonants:
            if char_freq[consonant] > max_consonants_freq:
                max_consonants_freq = char_freq[consonant]

        return max_vowel_freq + max_consonants_freq


sol = Solution()

s = "successes"
print(f"{s = } {sol.maxFreqSum(s) = }")

s = "aeiaeia"
print(f"{s = } {sol.maxFreqSum(s) = }")

s = "i"
print(f"{s = } {sol.maxFreqSum(s) = }")

s = "k"
print(f"{s = } {sol.maxFreqSum(s) = }")
