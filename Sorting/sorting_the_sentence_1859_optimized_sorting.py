class Solution:
    def sortSentence(self, s: str) -> str:
        original_sentence = ''
        s = s.split()

        result = sorted(s, key=lambda word: word[-1])
        for word in result:
            original_sentence += word[:-1] + " "
        return original_sentence[:-1]


sol = Solution()

s = "is2 sentence4 This1 a3"
print(s, sol.sortSentence(s))


s = "Myself2 Me1 I4 and3"
print(s, sol.sortSentence(s))