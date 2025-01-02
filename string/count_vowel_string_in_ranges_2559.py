from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Store vowels in a set since searching a vowel in it will take O(1)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        n = len(words)

        # Replace each element of words by 1 if it starts and ends with vowel else replace by 0
        for i in range(n):
            words[i] = 1 if (words[i][0] in vowels and words[i][-1] in vowels) else 0

        # words = ["aba","ibcbo","eceb","aa","e"]

        # com.  =  [1,2, 3, 4, 5,6]

        cummulative_count = [0] * n
        cummulative_count[0] = words[0]
        for i in range(1, n):
            cummulative_count[i] = words[i] + cummulative_count[i - 1]

        result = []
        for query in queries:
            if query[0] == 0:
                result.append(cummulative_count[query[1]])
            else:
                result.append(cummulative_count[query[1]] - cummulative_count[query[0] - 1])
        return result


sol = Solution()

words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
print(words, queries, sol.vowelStrings(words, queries))

words = ["a","e","i"]
queries = [[0,2],[0,1],[2,2]]
print(words, queries, sol.vowelStrings(words, queries))

words = ["aba","ibcbo","eceb","aa","e"]
queries = [[0,2],[1,4],[1,1]]
print(words, queries, sol.vowelStrings(words, queries))
