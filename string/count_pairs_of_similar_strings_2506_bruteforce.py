from typing import List


class Solution:
    def checkIfConsistOfSameChars(self, word1, word2):
        return sorted(set(word1)) == sorted(set(word2))

    def similarPairs(self, words: List[str]) -> int:
        ans = 0

        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if self.checkIfConsistOfSameChars(words[i], words[j]):
                    ans += 1
        return ans

sol = Solution()

words = ["aba","aabb","abcd","bac","aabc"]
print(words, sol.similarPairs(words))

words = ["aabb","ab","ba"]
print(words, sol.similarPairs(words))

words = ["nba","cba","dba"]
print(words, sol.similarPairs(words))

words = ["aabb","ab","ba","bca","aabbbcca"]
print(words, sol.similarPairs(words))
