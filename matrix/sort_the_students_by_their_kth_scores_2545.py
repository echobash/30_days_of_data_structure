from typing import List


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        # Parse the matrix and take kth column and store in array as tuplie with their index -> O(N)
        # Sort this 1-D array in desc-> O(NLogN)
        # Initialize an empty result array
        # Iterate the sorted array to get the sorted index order
        # Append into result in the above index order
        # Return Result
        # TC -> O(n logn + n)

        m, n = len(score), len(score[0])

        kth_col = []
        for i in range(m):
            kth_col.append((score[i][k], i))

        kth_col = sorted(kth_col, reverse=True)
        # (11,1) (9,0) (3,2)

        result = []

        for val, index in kth_col:
            result.append(score[index])

        return result


sol = Solution()

score = [[10,6,9,1],[7,5,11,2],[4,8,3,15]]
k = 2
print(f"{score = } {k = } {sol.sortTheStudents(score, k) = }")

score = [[3,4],[5,6]]
k = 0
print(f"{score = } {k = } {sol.sortTheStudents(score, k) = }")

score = [[5],[6]]
k = 0
print(f"{score = } {k = } {sol.sortTheStudents(score, k) = }")

score = [[3]]
k = 0
print(f"{score = } {k = } {sol.sortTheStudents(score, k) = }")