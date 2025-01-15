from collections import defaultdict


class Solution:
    def sortSentence(self, s: str) -> str:
        original_sentence = ''
        s = s.split()
        word_order_mapping = defaultdict(int)

        for word in s:
            word_order_mapping[int(word[-1:])] = word[:-1]

        for i in range(1,len(s)+1):
            original_sentence += word_order_mapping[i] + " "

        return original_sentence[:-1]


sol = Solution()

s = "is2 sentence4 This1 a3"
print(s, sol.sortSentence(s))


s = "Myself2 Me1 I4 and3"
print(s, sol.sortSentence(s))