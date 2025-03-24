from typing import List


class Solution:
    def find_target_in_row(self,row,target):
        left, right = 0, len(row) - 1
        while left <= right:
            mid = (left+right)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n = len(matrix), len(matrix[0])

        for i in range(m):
            if self.find_target_in_row(matrix[i], target):
                return True
        return False

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