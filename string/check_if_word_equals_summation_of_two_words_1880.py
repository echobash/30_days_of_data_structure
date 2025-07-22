class Solution:
    def __init__(self):
        self.char_position_mapping = {
    'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6',
    'h': '7', 'i': '8', 'j': '9', 'k': '10', 'l': '11', 'm': '12',
    'n': '13', 'o': '14', 'p': '15', 'q': '16', 'r': '17', 's': '18',
    't': '19', 'u': '20', 'v': '21', 'w': '22', 'x': '23', 'y': '24', 'z': '25'}
    def getLetterValue(self,word):
        result = []
        for char in word:
            result.append(self.char_position_mapping[char])
        return int("".join(result))


    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        if self.getLetterValue(firstWord) + self.getLetterValue(secondWord) == self.getLetterValue(targetWord):
            return True
        return False


sol = Solution()

firstWord = "acb"
secondWord = "cba"
targetWord = "cdb"
print(f"{firstWord = } {secondWord = } {targetWord = } {sol.isSumEqual(firstWord,secondWord,targetWord) = }")

firstWord = "aaa"
secondWord = "a"
targetWord = "aab"
print(f"{firstWord = } {secondWord = } {targetWord = } {sol.isSumEqual(firstWord,secondWord,targetWord) = }")

firstWord = "aaa"
secondWord = "a"
targetWord = "aaaa"
print(f"{firstWord = } {secondWord = } {targetWord = } {sol.isSumEqual(firstWord,secondWord,targetWord) = }")
