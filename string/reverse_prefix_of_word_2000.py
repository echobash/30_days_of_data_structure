class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = len(word)

        breaking_point = -1

        for i in range(n):
            if word[i] == ch:
                breaking_point = i
                break

        # If ch does not exist in word
        if breaking_point == -1:
            return word

        # Handle the case if ch exists in word
        first_part = word[:breaking_point + 1][::-1]
        second_part = word[breaking_point + 1:]
        return first_part + second_part


sol = Solution()

word = "abcdefd"
ch = "d"
print(f"{word = } | {ch = } | {sol.reversePrefix(word, ch) = }")

word = "xyxzxe"
ch = "z"
print(f"{word = } | {ch = } | {sol.reversePrefix(word, ch) = }")

word = "abcd"
ch = "z"
print(f"{word = } | {ch = } | {sol.reversePrefix(word, ch) = }")
