class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26


sol = Solution()

sentence = "thequickbrownfoxjumpsoverthelazydog"
print(f"{sentence = }  {sol.checkIfPangram(sentence) = }")

sentence = "echobash"
print(f"{sentence = }  {sol.checkIfPangram(sentence) = }")

sentence = "thequickbrownfoxjumpsoveralazydog"
print(f"{sentence = }  {sol.checkIfPangram(sentence) = }")

sentence = "leetcode"
print(f"{sentence = }  {sol.checkIfPangram(sentence) = }")
