from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        # Look in the last column, and find the possible row (log n)

        # After than search in the row (log m)
        # i.e total two binary searches
        # Total T.C = log n + log m = log (m*n)
        """
        Look in the last column where our target should be if it was present.
        Or in other words, find element just >= target using BS.
        l, r = 0, m - 1
        mid = (l + r )//2
        search by matrix[mid][n-1]

        Once, we found that element, we have our desired row with us say 'desired_row'

        Now in this 'row', check for our target using BS again.
        l, r = 0, n - 1
        mid = (l + r )//2
        search by matrix[desired_row][mid]
        If found return True, otherwise return False at the exit of the BS
        """
        # Check if the last element of last row, last column < target, we won't find the target
        desired_row = -1

        l, r = 0, m - 1
        while l <= r:
            mid = (l + r) // 2
            curr = matrix[mid][n - 1]
            if curr == target:
                return True
            elif curr > target:
                desired_row = mid
                r = mid - 1
            else:
                l = mid + 1
        if desired_row == -1:
            return False

        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            curr = matrix[desired_row][mid]
            if curr == target:
                return True
            elif curr > target:
                r = mid - 1
            else:
                l = mid + 1
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

matrix = [[1]]
target = 2
print(f" {matrix = } | {target = } | {sol.searchMatrix(matrix, target) = }")

matrix = [[1]]
target = 1
print(f" {matrix = } | {target = } | {sol.searchMatrix(matrix, target) = }")

matrix = [[1,3,4]]
target = 3
print(f" {matrix = } | {target = } | {sol.searchMatrix(matrix, target) = }")

matrix = [[1],[3],[5]]
target = 3
print(f" {matrix = } | {target = } | {sol.searchMatrix(matrix, target) = }")

matrix = [[1,1]]
target = 2
print(f" {matrix = } | {target = } | {sol.searchMatrix(matrix, target) = }")
