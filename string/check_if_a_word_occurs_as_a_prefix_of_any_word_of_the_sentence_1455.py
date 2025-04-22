class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()
        for i, word in enumerate(words):
            if word.startswith(searchWord):
                return i + 1
        return -1


sol = Solution()

sentence = "i love eating burger"
searchWord = "burg"
print(f"{sentence = }  {searchWord = } {sol.isPrefixOfWord(sentence, searchWord) = }")

sentence = "this problem is an easy problem"
searchWord = "pro"
print(f"{sentence = }  {searchWord = } {sol.isPrefixOfWord(sentence, searchWord) = }")

sentence = "i am tired"
searchWord = "you"
print(f"{sentence = }  {searchWord = } {sol.isPrefixOfWord(sentence, searchWord) = }")


sentence = "i am in abundance"
searchWord = "abun"
print(f"{sentence = }  {searchWord = } {sol.isPrefixOfWord(sentence, searchWord) = }")