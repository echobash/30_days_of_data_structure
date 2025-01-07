from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        n = len(words)
        result = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                if words[i] in words[j]:
                    result.append(words[i])
                    # as soon as we found that this string is subset of atleast one other string,break and come out and look for next element otherwise duplicates may be caught
                    break
        return result



sol = Solution()

words = ["mass","as","hero","superhero"]
print(words, sol.stringMatching(words))

words = ["leetcode","et","code"]
print(words, sol.stringMatching(words))

words = ["blue","green","bu"]
print(words, sol.stringMatching(words))

