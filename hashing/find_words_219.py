class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Define rows of the keyboard
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            # Convert the word to lowercase to handle case insensitivity
            lower_word = set(word.lower())

            # Check if the word can be typed using letters from one row
            if lower_word.issubset(row1) or lower_word.issubset(row2) or lower_word.issubset(row3):
                result.append(word)

        return result

nums = [1,2,3,1]
k = 3
solution = Solution()
print(solution.findWords(nums, k))
