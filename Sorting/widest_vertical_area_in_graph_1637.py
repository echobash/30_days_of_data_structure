from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        maxWidth = 0
        xCord = []

        for x,y in points:
            xCord.append(x)

        xCord = sorted(xCord, reverse=True)

        n = len(xCord)
        for i in range(n-1):
            if xCord[i] - xCord[i+1] > maxWidth:
                maxWidth = xCord[i] - xCord[i+1]

        return maxWidth


solution = Solution()

points = [[8,7],[9,9],[7,4],[9,7]]
print(solution.maxWidthOfVerticalArea(points))

points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(solution.maxWidthOfVerticalArea(points))
