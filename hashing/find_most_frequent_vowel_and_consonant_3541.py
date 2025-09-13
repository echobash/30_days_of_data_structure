from collections import Counter


class Solution:
    def maxFreqSum(self, s: str) -> int:
        maxFreqVowelCount = 0
        maxFreqConsonantCount = 0
        vowels = {'a', 'e', 'i', 'o', 'u'}
        char_freq = Counter(s)

        for char, freq in char_freq.items():
            if char in vowels:
                maxFreqVowelCount = max(maxFreqVowelCount, freq)
            else:
                maxFreqConsonantCount = max(maxFreqConsonantCount, freq)

        return maxFreqVowelCount + maxFreqConsonantCount


sol = Solution()

s = "successes"
print(f"{s = } {sol.maxFreqSum(s) = }")

s = "education"
print(f"{s = } {sol.maxFreqSum(s) = }")

s = "aeiaeia"
print(f"{s = } {sol.maxFreqSum(s) = }")
