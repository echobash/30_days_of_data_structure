from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        result = []
        arr = sorted(arr)
        n = len(arr)
        min_abs_diff = float('inf')
        for i in range(n - 1):
            if abs(arr[i] - arr[i + 1]) <= min_abs_diff:
                min_abs_diff = abs(arr[i] - arr[i + 1])

        for i in range(n - 1):
            if abs(arr[i] - arr[i + 1]) == min_abs_diff:
                result.append([arr[i], arr[i + 1]])
        return result


sol = Solution()

arr = [4,2,1,3]
print(f"{arr = } | {sol.minimumAbsDifference(arr) = }")

arr = [1,3,6,10,15]
print(f"{arr = } | {sol.minimumAbsDifference(arr) = }")

arr = [3,8,-10,23,19,-4,-14,27]
print(f"{arr = } | {sol.minimumAbsDifference(arr) = }")
