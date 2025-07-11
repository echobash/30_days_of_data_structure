class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        result = []
        vowels = set('aeiouAEIOU')
        words = sentence.split()
        for i,word in enumerate(words):
            if word[0]  in vowels:
                new_word = word + "ma" + "a" * (i+1)
            else:
                new_word = word[1:] + word[0] + "ma" + "a" * (i+1)
            result.append(new_word)
        return " ".join(result)


sol = Solution()

sentence = "I speak Goat Latin"
print(f"{sentence = } {sol.toGoatLatin(sentence) = }")

sentence = "The quick brown fox jumped over the lazy dog"
print(f"{sentence = } {sol.toGoatLatin(sentence) = }")
