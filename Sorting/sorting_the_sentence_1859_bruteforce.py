class Solution:
    def sortSentence(self, s: str) -> str:
        original_sentence = ''
        s = s.split()
        no_of_words = len(s)
        for i in range(1,no_of_words+1):
            for word in s:
                if word.endswith(str(i)):
                    original_sentence += word[:-1]+" "
        return original_sentence[:-1]


sol = Solution()

s = "is2 sentence4 This1 a3"
print(s, sol.sortSentence(s))


s = "Myself2 Me1 I4 and3"
print(s, sol.sortSentence(s))