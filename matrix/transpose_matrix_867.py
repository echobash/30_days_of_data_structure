from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        result = []
        for i in range(n):
            temp = []
            for j in range(m):
                temp.append(matrix[j][i])
            result.append(temp)
        return result


sol = Solution()

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(f"{matrix = } {sol.transpose(matrix) = }")

matrix = [[1,2,3],[4,5,6]]
print(f"{matrix = } {sol.transpose(matrix) = }")

matrix = [[1,2,3]]
print(f"{matrix = } {sol.transpose(matrix) = }")

matrix = [[1], [2], [3]]
print(f"{matrix = } {sol.transpose(matrix) = }")

