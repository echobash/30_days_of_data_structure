from typing import List

# T.C - O(m*log n + m*log m)


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers_row_wise_count = []
        m, n = len(mat), len(mat[0])

        for i in range(m):
            left, right = 0, n-1
            ans = -1

            while left <= right:
                mid = (left + right)//2
                if mat[i][mid] == 1:
                    ans = mid
                    left = mid + 1
                else:
                    right = mid - 1
            soldiers_row_wise_count.append((ans + 1, i))

        frequency_order = sorted(soldiers_row_wise_count)
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
