from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m = len(grid)
        n = len(grid[0])

        # For row Cut
        sum_row_arr = [0] * m
        for i in range(m):
            sum_row = 0
            for j in range(n):
                sum_row += grid[i][j]
            sum_row_arr[i] = sum_row

        prefix_sum = []
        pref_sum = 0
        for i in range(m):
            pref_sum += sum_row_arr[i]
            prefix_sum.append(pref_sum)

        arr_sum = sum(sum_row_arr)

        for i in range(m):
            if prefix_sum[i] == arr_sum - prefix_sum[i]:
                return True

        # For Column Cut
        sum_col_arr = [0] * n
        for i in range(n):
            sum_col = 0
            for j in range(m):
                sum_col += grid[j][i]
            sum_col_arr[i] = sum_col
        print(f"{ sum_col_arr = } { sum(sum_col_arr) = }")

        prefix_sum = []
        pref_sum = 0
        for i in range(n):
            pref_sum += sum_col_arr[i]
            prefix_sum.append(pref_sum)

        arr_sum = sum(sum_col_arr)

        for i in range(n):
            if prefix_sum[i] == arr_sum - prefix_sum[i]:
                return True
        return False


sol = Solution()

grid = [[1,4],[2,3]]
print(f"{grid = } | {sol.canPartitionGrid(grid) = }")

grid = [[1,3],[2,4]]
print(f"{grid = } | {sol.canPartitionGrid(grid) = }")

grid = [[1,3],[2,4]]
print(f"{grid = } | {sol.canPartitionGrid(grid) = }")

grid = [[1,5],[2,1],[7,4]]
print(f"{grid = } | {sol.canPartitionGrid(grid) = }")