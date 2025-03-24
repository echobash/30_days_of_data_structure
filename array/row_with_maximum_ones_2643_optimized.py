from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        result = [0,0]
        for i in range(m):
            # count of 1 in row mat[i], will be sum of row mat[i]
            no_of_ones_in_ith_row = sum(mat[i])
            if no_of_ones_in_ith_row > result[1]:
                result[0] = i
                result[1] = no_of_ones_in_ith_row
        return result


sol = Solution()

mat = [[0,1],[1,0]]
print(f" {mat = } | {sol.rowAndMaximumOnes(mat) = }")

mat = [[0,0,0],[0,1,1]]
print(f" {mat = } | {sol.rowAndMaximumOnes(mat) = }")

mat = [[0,0],[1,1],[0,0]]
print(f" {mat = } | {sol.rowAndMaximumOnes(mat) = }")

mat = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
print(f" {mat = } | {sol.rowAndMaximumOnes(mat) = }")

mat = [[0,0], [0,0]]
print(f" {mat = } | {sol.rowAndMaximumOnes(mat) = }")
