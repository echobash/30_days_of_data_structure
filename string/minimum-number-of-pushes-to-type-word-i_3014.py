class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        if n <= 8:
            return n

        if 9 <= n <= 16:
            return (n - 8) * 2 + 8

        if 17 <= n <= 24:
            return (n - 16) * 3 + 8 + 16

        if n > 24:
            return (n - 24) * 4 + 8 + 16 + 24


sol = Solution()

word = "abcde"
print(f"{word = } {sol.minimumPushes(word) = }")

word = "xycdefghij"
print(f"{word = } {sol.minimumPushes(word) = }")

word = "acolkxjbizfmhnrdq"
print(f"{word = } {sol.minimumPushes(word) = }")

word = "amrvxnhsewkoipjyuclgtdbfq"
print(f"{word = } {sol.minimumPushes(word) = }")
