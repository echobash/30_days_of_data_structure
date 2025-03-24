from typing import List


class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        result = [0,0]
        for i in range(m):
            count_one = 0
            for j in range(n):
                if mat[i][j] == 1:
                    count_one += 1
                    if count_one > result[1]:
                        result[0] = i
                        result[1] = count_one
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
