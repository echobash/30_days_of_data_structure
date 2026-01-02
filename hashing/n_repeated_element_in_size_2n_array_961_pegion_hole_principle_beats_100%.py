from collections import defaultdict
from typing import List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        num_freq = defaultdict(int)
        n = len(nums) // 2
        for num in nums:
            num_freq[num] += 1

            """
            We know that there are n+1 unique element (n unique + 1 duplicate n times)
            So as soon as we get an element that occurs more than 1, that's our duplicate element
            We used pegionhole principle here
            """
            if num_freq[num] > 1:
                return num


sol = Solution()

nums = [1,2,3,3]
print(f"{nums = } {sol.repeatedNTimes(nums) = }")

nums = [2,1,2,5,3,2]
print(f"{nums = } {sol.repeatedNTimes(nums) = }")

nums = [5,1,5,2,5,3,5,4]
print(f"{nums = } {sol.repeatedNTimes(nums) = }")