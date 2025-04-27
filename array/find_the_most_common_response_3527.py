from collections import defaultdict
from typing import List


class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        n = len(responses)
        word_count = defaultdict(int)
        for i in range(n):
            ithrowresponses = list(set(responses[i]))
            for word in ithrowresponses:
                word_count[word] += 1

        max_count = 0
        for val in word_count.values():
            max_count = max(max_count, val)

        result = []
        for word, total_count in word_count.items():
            if total_count == max_count:
                result.append(word)
        return sorted(result)[0]


sol = Solution()

responses = [["good", "ok", "good", "ok"], ["ok", "bad", "good", "ok", "ok"], ["good"], ["bad"]]
print(f" {responses = } | {sol.findCommonResponse(responses) = }")

responses = [["good","ok","good"],["ok","bad"],["bad","notsure"],["great","good"]]
print(f" {responses = } | {sol.findCommonResponse(responses) = }")
