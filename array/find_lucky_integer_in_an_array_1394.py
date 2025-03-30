from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_frequency = Counter(arr)
        max_no = -1
        for number, freq in arr_frequency.items():
            if freq == number:
                max_no = max(max_no, number)
        return max_no


sol = Solution()

arr = [2,2,3,4]
print(arr, sol.findLucky(arr))

arr = [1,2,2,3,3,3]
print(arr, sol.findLucky(arr))

arr = [2,2,2,3,3]
print(arr, sol.findLucky(arr))