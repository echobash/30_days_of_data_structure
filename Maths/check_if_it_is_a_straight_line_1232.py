from typing import List


class Solution:
    def getSlope(self, first_coordinates, second_coordinates):
        return (second_coordinates[1] - first_coordinates[1]) / (second_coordinates[0] - first_coordinates[0])

    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)

        # Two points are always collinear
        if n == 2:
            return True

        isSomePortionParallelToYAxis = False
        for i in range(n - 1):
            if coordinates[i][0] == coordinates[i + 1][0]:
                isSomePortionParallelToYAxis = True

        """
        Now we know if slope can be infinity or not based on isSomePortionParallelToYAxis
        if isSomePortionParallelToYAxis == true, it means all x should be equal in order to be a straight line
        """

        if isSomePortionParallelToYAxis == True:
            for i in range(n - 1):
                if coordinates[i][0] != coordinates[i + 1][0]:
                    return False
            return True
        else:
            slope = self.getSlope(coordinates[0], coordinates[1])
            for i in range(n - 1):
                if self.getSlope(coordinates[i], coordinates[i + 1]) != slope:
                    return False
            return True


sol = Solution()

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(f"{coordinates = } {sol.checkStraightLine(coordinates) = }")

coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(f"{coordinates = } {sol.checkStraightLine(coordinates) = }")

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(f"{coordinates = } {sol.checkStraightLine(coordinates) = }")

coordinates = [[1,2],[1,3],[1,4]]
print(f"{coordinates = } {sol.checkStraightLine(coordinates) = }")
