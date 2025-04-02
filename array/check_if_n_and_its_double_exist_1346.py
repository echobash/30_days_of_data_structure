from typing import List


from collections import defaultdict


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        numbers_freq = defaultdict(int)
        n = len(arr)

        for num in arr:
            numbers_freq[num] += 1

        for i in range(n):
            if arr[i] * 2 in numbers_freq:
                if (arr[i] == 0 and numbers_freq[0] > 1) or arr[i] != 0:
                    return True
        return False


sol = Solution()

arr = [10,2,5,3]
print(f" {arr = } | {sol.checkIfExist(arr) = }")

arr = [3,1,7,11]
print(f" {arr = } | {sol.checkIfExist(arr) = }")