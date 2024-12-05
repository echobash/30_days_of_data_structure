class WordPattern:
    def it_matches_pattern(self, pattern: str, s: str) -> bool:
        n = len(pattern)
        pattern_word_mapping = {}
        transpose_pattern_word_mapping = {}

        # Break sentence separated by spaces into an array
        s = s.split()

        if(len(s) != len(pattern)):
            return False

        for i in range(n):
            if pattern[i] in pattern_word_mapping:
                if(pattern_word_mapping[pattern[i]] != s[i]):
                    return False
            else:
                if s[i] in transpose_pattern_word_mapping:
                    return False
                else:
                    pattern_word_mapping[pattern[i]] = s[i]
                    transpose_pattern_word_mapping[s[i]] = pattern[i]
        return True


pattern = "ab"
s = "dog dog"

pattern = "abab"
s = "dog cat deer cat"

pattern = "abba"
s = "dog cat cat dog"

word_pattern = WordPattern()
print(word_pattern.it_matches_pattern(pattern, s))