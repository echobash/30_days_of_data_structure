from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        result = []
        num_deque = deque()

        for i in range(n):
            if num_deque and i - k == num_deque[0]:
                num_deque.popleft()

            while num_deque and nums[num_deque[-1]] < nums[i]:
                num_deque.pop()

            num_deque.append(i)
            # Then the window are full. At k and onwards, the rest one and 1 before k steps so k - 1
            if i >= k - 1:
                result.append(nums[num_deque[0]])
        return result


sol = Solution()

arr = [1,3,-1,-3,5,3,6,7]
k = 3
print(f" {arr = } | {k = } | {sol.maxSlidingWindow(arr, k) = }")

arr = [1]
k = 1
print(f" {arr = } | {k = } | {sol.maxSlidingWindow(arr, k) = }")

arr = [7,2,4]
k = 2
print(f" {arr = } | {k = } | {sol.maxSlidingWindow(arr, k) = }")

arr = [1,3,-1,-3,5,3,6,7]
k = 2
print(f" {arr = } | {k = } | {sol.maxSlidingWindow(arr, k) = }")

arr = [1,-1]
k = 1
print(f" {arr = } | {k = } | {sol.maxSlidingWindow(arr, k) = }")

arr = [4,3,11]
k = 3
print(f" {arr = } | {k = } | {sol.maxSlidingWindow(arr, k) = }")

arr = [1,3,1,2,0,5]
k = 3
print(f" {arr = } | {k = } | {sol.maxSlidingWindow(arr, k) = }")

arr = [1, 1, 1, 1]
k = 2
print(f" {arr = } | {k = } | {sol.maxSlidingWindow(arr, k) = }")

arr = [1, 1, 1, 1]
k = 3
print(f" {arr = } | {k = } | {sol.maxSlidingWindow(arr, k) = }")
