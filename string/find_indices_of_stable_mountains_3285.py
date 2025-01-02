from typing import List


class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        stable_mountains = []
        for i in range(1,len(height)):
            if height[i-1] > threshold:
                stable_mountains.append(i)
        return stable_mountains


sol = Solution()

height = [1,2,3,4,5]
threshold = 2
print(height, threshold, sol.stableMountains(height, threshold))

height = [10,1,10,1,10]
threshold = 3
print(height, threshold, sol.stableMountains(height, threshold))

height = [10,1,10,1,10]
threshold = 10
print(height, threshold, sol.stableMountains(height, threshold))
