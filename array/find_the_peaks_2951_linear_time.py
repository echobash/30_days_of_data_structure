from typing import List


class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        result = []
        for i in range(1, n-1):
            if mountain[i-1] < mountain[i] > mountain[i+1]:
                result.append(i)
        return result


sol = Solution()

mountain = [2,4,4]
print(f" {mountain = } | {sol.findPeaks(mountain) = }")

mountain = [1,4,3,8,5]
print(f" {mountain = } | {sol.findPeaks(mountain) = }")
