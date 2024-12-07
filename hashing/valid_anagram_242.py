from collections import defaultdict


class Anagram:
    def isAnagram(self, s: str, t: str) -> bool:
        first_dictionary = defaultdict(int)
        second_dictionary = defaultdict(int)

        # Store character count of both strings in separate dicts
        for char in s:
            first_dictionary[char] += 1

        for char in t:
            second_dictionary[char] += 1

        # Check if both strings have same length
        if (len(s) != len(t)):
            return False

        # Check if count of both strings is same
        for char, count in first_dictionary.items():
            if count != second_dictionary[char]:
                return False

        return True


s = "anagram"
t = "nagaram"
anagram = Anagram()
print(anagram.isAnagram(s, t))
