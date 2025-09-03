class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)

        if n == 1:
            return words[0][-1] == words[0][0]

        for i in range(n - 1):
            if words[i][-1] != words[i + 1][0]:
                return False

        return words[-1][-1] == words[0][0]


sol = Solution()

sentence = "leetcode exercises sound delightful"
print(f"{sentence = } {sol.isCircularSentence(sentence) = }")

sentence = "eetcode"
print(f"{sentence = } {sol.isCircularSentence(sentence) = }")

sentence = "Leetcode is cool"
print(f"{sentence = } {sol.isCircularSentence(sentence) = }")

sentence = "leetcode"
print(f"{sentence = } {sol.isCircularSentence(sentence) = }")

sentence = "Leetcode eisc cool"
print(f"{sentence = } {sol.isCircularSentence(sentence) = }")

sentence = "Leetcode eisc cool delightful"
print(f"{sentence = } {sol.isCircularSentence(sentence) = }")
