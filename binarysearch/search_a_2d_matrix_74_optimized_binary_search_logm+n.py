from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        # Look in the last column, and find the possible row (log n)
        # After than search in the row (log m)
        # i.e total two binary searches
        # Total T.C = log n + log m = log (m*n)
        left, right = 0, m -1
        possible_index = -1
        while left <= right:
            mid = (left+right)//2
            if matrix[mid][n-1] >= target:
                possible_index = mid
                right = mid - 1
            else:
                left = mid + 1

        # Now search in possible_index row
        left, right = 0, n - 1
        while left <= right:
            mid = (left+right)//2
            if matrix[possible_index][mid] == target:
                return True
            elif matrix[possible_index][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    # O(log m*n)

sol = Solution()

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(f" {matrix = } | {target = } | {sol.searchMatrix(matrix, target) = }")

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
print(f" {matrix = } | {target = } | {sol.searchMatrix(matrix, target) = }")

matrix = [[1],[10]]
target = 10
print(f" {matrix = } | {target = } | {sol.searchMatrix(matrix, target) = }")