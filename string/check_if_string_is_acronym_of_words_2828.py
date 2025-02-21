from typing import List


class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        n = len(words)
        if n != len(s):
            return False

        for i in range(n):
            if words[i][0] != s[i]:
                return False
        return True


sol = Solution()

words = ["alice","bob","charlie"]
s = "abc"
print(f"{s = } {words = } {sol.isAcronym(words, s) = }")

words = ["an","apple"]
s = "a"
print(f"{s = } {words = } {sol.isAcronym(words, s) = }")

words = ["never","gonna","give","up","on","you"]
s = "ngguoy"
print(f"{s = } {words = } {sol.isAcronym(words, s) = }")

words = ["bring","your","own","bag"]
s = "byob"
print(f"{s = } {words = } {sol.isAcronym(words, s) = }")

