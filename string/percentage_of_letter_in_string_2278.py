from collections import Counter


class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        char_frequency  = Counter(s)
        return int(char_frequency[letter]/len(s)*100)


sol = Solution()

s = "foobar"
letter = "o"
print(f"{s = } {letter = }  {sol.percentageLetter(s,letter) = }")

s = "jjjj"
letter = "k"
print(f"{s = } {letter = }  {sol.percentageLetter(s,letter) = }")

s = "jjjj"
letter = "j"
print(f"{s = } {letter = }  {sol.percentageLetter(s,letter) = }")
