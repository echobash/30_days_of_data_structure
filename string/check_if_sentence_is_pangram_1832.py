class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        n = len(sentence)

        if n < 26:
            return False

        set_of_unique_alphabets_in_sentence = set(sentence)
        return len(set_of_unique_alphabets_in_sentence) == 26


sol = Solution()

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(f"{sentence = }  {sol.checkIfPangram(sentence) = }")

sentence = "echobash"
print(f"{sentence = }  {sol.checkIfPangram(sentence) = }")

sentence = "thequickbrownfoxjumpsoveralazydog"
print(f"{sentence = }  {sol.checkIfPangram(sentence) = }")

sentence = "leetcode"
print(f"{sentence = }  {sol.checkIfPangram(sentence) = }")
