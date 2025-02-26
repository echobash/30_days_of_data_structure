from math import ceil
from typing import List


class Solution:
    def book_allocation(self, arr: List[int], m: int, max_page: int) -> int:
        student_count = 1
        n = len(arr)
        i = 0
        print(arr)
        while i <= n-2:
            if arr[i] + arr[i+1] > max_page:
                student_count += 1
                i += 1
            else:
                while arr[i] + arr[i+1] <= max_page:
                    i += 1
                    print(f"i inside while {i}")
                student_count += 1
            # print(f"{arr[i] + arr[i+1] = } | {max_page = } | {student_count = } | {i = }")
        return student_count



sol = Solution()

# arr = [25,46,28,49,24]
# m = 4
# max_page = 72
# print(f"{arr = } |  {max_page = } | {sol.book_allocation(arr, m, max_page) = }")
#
arr = [25,46,28,49,24]
m = 4
max_page = 49
print(f"{arr = } |  {max_page = } | {sol.book_allocation(arr, m, max_page) = }")
#
arr = [25,46,28,49,24]
m = 4
max_page = 100
print(f"{arr = } |  {max_page = } | {sol.book_allocation(arr, m, max_page) = }")


arr = [25,46,28,49,24]
m = 4
max_page = 72
print(f"{arr = } |  {max_page = } | {sol.book_allocation(arr, m, max_page) = }")
