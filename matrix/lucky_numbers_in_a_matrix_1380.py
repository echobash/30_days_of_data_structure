from typing import List


class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        result = []
        min_max_set = set()
        """
        Traverse row by row and put min of each row in min_max_set
        Traverse col by col and put max of each col in min_max_set
        Return all elements with count > 1
        """
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            min_max_set.add(min(matrix[i]))

        for i in range(n):
            max_in_col = float('-inf')
            for j in range(m):
                max_in_col = max(matrix[j][i], max_in_col)
            if max_in_col in min_max_set:
                result.append(max_in_col)
        return result


sol = Solution()

matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(f"{matrix = } {sol.luckyNumbers(matrix) = }")

matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(f"{matrix = } {sol.luckyNumbers(matrix) = }")

matrix = [[7,8],[1,2]]
print(f"{matrix = } {sol.luckyNumbers(matrix) = }")

matrix = [[1,2]]
print(f"{matrix = } {sol.luckyNumbers(matrix) = }")