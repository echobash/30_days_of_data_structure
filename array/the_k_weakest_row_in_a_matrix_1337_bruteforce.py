from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers_rowwise_count = []
        m, n = len(mat), len(mat[0])

        for i in range(m):
            soldiers_rowwise_count.append((sum(mat[i]), i))

        frequency_order = sorted(soldiers_rowwise_count)
        result = []
        for i in range(k):
            result.append(frequency_order[i][1])
        return result


sol = Solution()

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]

k=3
print(f"{mat = } {k = } {sol.kWeakestRows(mat, k) = } ")

mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]

k=2
print(f"{mat = } {k = } {sol.kWeakestRows(mat, k) = } ")

mat = [[1,0,0,0],
 [1,1,1,1],
 [0,0,0,0],
 [1,0,0,0]]

k=2
print(f"{mat = } {k = } {sol.kWeakestRows(mat, k) = } ")

# T.C - O(m*n + mlogm)