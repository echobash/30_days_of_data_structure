from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]

        for letter in letters:
            if letter > target:
                return letter


sol = Solution()

letters = ["c","f","j"]
target = "a"
print(f"{letters = } {target = } {sol.nextGreatestLetter(letters, target) = }")

letters = ["c","f","j"]
target = "c"
print(f"{letters = } {target = } {sol.nextGreatestLetter(letters, target) = }")

letters = ["x","x","y","y"]
target = "z"
print(f"{letters = } {target = } {sol.nextGreatestLetter(letters, target) = }")

letters = ["c","f","j"]
target = "j"
print(f"{letters = } {target = } {sol.nextGreatestLetter(letters, target) = }")
