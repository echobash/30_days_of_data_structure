from typing import List
import heapq


# O(m* log n + m* log k)

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers_row_wise_count = []
        m, n = len(mat), len(mat[0])

        # O(m* log n)
        for i in range(m):
            left, right = 0, n - 1
            ans = -1

            while left <= right:
                mid = (left + right) // 2
                if mat[i][mid] == 1:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            soldiers_row_wise_count.append((ans + 1, i))

        # O(mlogm) would cost if if sorted fully.
        # So use min-heap nsmallest for k smallest element. in O(mlogk)
        # O(m* log k)
        kweakest = heapq.nsmallest(k, soldiers_row_wise_count)
        return [row for freq, row in kweakest]


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
