from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freq_count = dict()
        sorted_dominoes = []
        for domino in dominoes:
            sorted_dominoes.append(sorted(domino))

        for domino in sorted_dominoes:
            if str(domino[0])+str(domino[1]) in freq_count:
                freq_count[str(domino[0])+str(domino[1])] += 1
            else:
                freq_count[str(domino[0])+str(domino[1])] = 1

        total_count =0
        for dom, freq in freq_count.items():
            if freq > 1:
                total_count += (freq * (freq-1)//2)

        return total_count


solution = Solution()

dominoes = [[1,2],[2,1],[3,4],[5,6]]
print(f"{dominoes = } {solution.numEquivDominoPairs(dominoes) = }")

dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2],[4,3],[3,4],[3,3],[4,3]]
print(f"{dominoes = } {solution.numEquivDominoPairs(dominoes) = }")

dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
print(f"{dominoes = } {solution.numEquivDominoPairs(dominoes) = }")
