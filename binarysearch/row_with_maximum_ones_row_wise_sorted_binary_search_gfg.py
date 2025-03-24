from typing import List


class Solution:
    def find_no_of_ones_in_row(self,row):
        n = len(row)
        left, right = 0, n - 1
        ans = n
        while left <= right:
            mid = (left + right )//2
            if row[mid] == 1:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return n - ans

    def rowWithMax1s(self, arr: List[List[int]]) ->int:
        m, n = len(arr), len(arr[0])
        max_count = 0
        result_index = -1
        for i in range(m):
            no_of_ones_in_ith_row = 0
            # Apply binary search in each row to find first occurrence of 1
            # count of 1 will be n
            no_of_ones_in_ith_row = self.find_no_of_ones_in_row(arr[i])
            if no_of_ones_in_ith_row > max_count:
                max_count = no_of_ones_in_ith_row
                result_index = i
        return result_index


sol = Solution()

mat = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
print(f" {mat = } | {sol.rowWithMax1s(mat) = }")

mat =  [[0,0],[1,1], [1,1]]
print(f" {mat = } | {sol.rowWithMax1s(mat) = }")

mat = [[0,0], [0,0]]
print(f" {mat = } | {sol.rowWithMax1s(mat) = }")
