class RansomNote:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_freq_dict = {}
        mag_freq_dict = {}

        # Track count for ransomNote characters
        for char in ransomNote:
            if char in ransom_freq_dict:
                ransom_freq_dict[char] = ransom_freq_dict[char] + 1
            else:
                ransom_freq_dict[char] = 1

        # Track count for magazine characters
        for char in magazine:
            if char in mag_freq_dict:
                mag_freq_dict[char] = mag_freq_dict[char] + 1
            else:
                mag_freq_dict[char] = 1

        # Iterate ransom_freq_dict and compare frequecy of each char with...
        # ... mag_freq_dict. Count From ransom_freq_dict should not be ...
        # ... greater than Count From mag_freq_dict for any char.

        for char, count in ransom_freq_dict.items():
            if (char not in mag_freq_dict or ransom_freq_dict[char] > mag_freq_dict[char]):
                return False
        return True


ransomNote = "aa"
magazine = "aab"

ransom_note = RansomNote()
print(ransom_note.canConstruct(ransomNote, magazine))