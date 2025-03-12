class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        longer_string = ""
        m = len(word1)
        n = len(word2)
        common_length = min(m, n) if m != n else m

        for i in range(common_length):
            result.append(word1[i])
            result.append(word2[i])

        if m > n:
            longer_string = word1
        elif m < n:
            longer_string = word2

        for j in range(common_length, len(longer_string)):
            result.append(longer_string[j])

        return "".join(result)


sol = Solution()

word1 = "abc"
word2 = "pqr"
print(f"{word1 = } | {word2 = } | {sol.mergeAlternately(word1, word2) = }")

word1 = "ab"
word2 = "pqrs"
print(f"{word1 = } | {word2 = } | {sol.mergeAlternately(word1, word2) = }")

word1 = "abcd"
word2 = "pq"
print(f"{word1 = } | {word2 = } | {sol.mergeAlternately(word1, word2) = }")

word1 = "abcdefghijk"
word2 = "pq"
print(f"{word1 = } | {word2 = } | {sol.mergeAlternately(word1, word2) = }")
