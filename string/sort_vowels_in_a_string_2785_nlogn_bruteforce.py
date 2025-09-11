class Solution:
    def isConsonant(self, char):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        if char not in vowels:
            return True
        return False

    def sortVowels(self, s: str) -> str:
        n = len(s)
        t = [""] * n
        occurred_vowels = []
        for i, char in enumerate(s):
            if self.isConsonant(char):
                t[i] = char
            else:
                occurred_vowels.append(char)

        occurred_vowels = sorted(occurred_vowels, reverse=True)
        for i, char in enumerate(t):
            if char == "":
                t[i] = occurred_vowels.pop()
        return "".join(t)


sol = Solution()

s = "lEetcOde"
print(f"{s = } {sol.sortVowels(s) = }")

s = "lYmpH"
print(f"{s = } {sol.sortVowels(s) = }")
