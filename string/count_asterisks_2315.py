class Solution:
    def count_askterisks(self, word):
        ast_count = 0
        for char in word:
            if char == '*':
                ast_count += 1
        return ast_count

    def countAsterisks(self, s: str) -> int:
        count = 0
        words = s.split("|")

        for i, word in enumerate(words):
            if i % 2 == 0:
                count += self.count_askterisks(word)
        return count


sol = Solution()

s = "l|*e*et|c**o|*de|"
print(f"{s = } {sol.countAsterisks(s) = }")

s = "iamprogrammer"
print(f"{s = } {sol.countAsterisks(s) = }")

s = "yo|uar|e**|b|e***au|tifu|l"
print(f"{s = } {sol.countAsterisks(s) = }")

s = "yo|uar|e**|ve|r**|yb|e***au|tifu|l"
print(f"{s = } {sol.countAsterisks(s) = }")
