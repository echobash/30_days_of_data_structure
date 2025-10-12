from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        n = len(words)
        for i in range(1,n):
            if sorted(words[i]) != sorted(words[i-1]):
                result.append(words[i])
        return result


sol = Solution()

words = ["abba","baba","bbaa","cd","cd"]
print(f"{words = } {sol.removeAnagrams(words) = }")


words = ["abba","baba","bbaa","cd"]
print(f"{words = } {sol.removeAnagrams(words) = }")