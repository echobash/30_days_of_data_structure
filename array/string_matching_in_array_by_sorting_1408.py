from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        result = set()
        words = sorted(words, key=len)
        for i in range(n):
            for j in range(i+1, n):
                if words[i] in words[j]:
                    result.add(words[i])
        return list(result)



sol = Solution()

words = ["mass","as","hero","superhero"]
print(words, sol.stringMatching(words))

words = ["leetcode","et","code"]
print(words, sol.stringMatching(words))

words = ["blue","green","bu"]
print(words, sol.stringMatching(words))

