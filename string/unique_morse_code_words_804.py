from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_dict = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z": "--.."
        }

        unqiue_morse_encoded_set = set()
        for word in words:
            morse_encoded_strings = []
            for char in word:
                morse_encoded_strings.append(morse_dict[char])
            unqiue_morse_encoded_set.add("".join(morse_encoded_strings))
        return len(unqiue_morse_encoded_set)


sol = Solution()

words = ["gin","zen","gig","msg"]
print(f"{words = }  {sol.uniqueMorseRepresentations(words) = }")

words = ["a"]
print(f"{words = }  {sol.uniqueMorseRepresentations(words) = }")
