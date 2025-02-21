from typing import List


class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        pair_count = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1,n):
                if words[j][::-1] == words[i]:
                    pair_count += 1
        return pair_count


sol = Solution()

words = ["cd","ac","dc","ca","zz"]
print(f"{words = } {sol.maximumNumberOfStringPairs(words) = }")

words = ["ab","ba","cc"]
print(f"{words = } {sol.maximumNumberOfStringPairs(words) = }")

words = ["aa","ab"]
print(f"{words = } {sol.maximumNumberOfStringPairs(words) = }")
