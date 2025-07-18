from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        count = 0
        for boxType in boxTypes:
            no_of_boxes = boxType[0]
            no_of_units_in_a_box = boxType[1]
            if no_of_boxes <= truckSize:
                count += no_of_boxes * no_of_units_in_a_box
                truckSize -= no_of_boxes
            else:
                count += truckSize * no_of_units_in_a_box
                truckSize = 0
            # If the whole truck is full
            if truckSize == 0:
                return count
        # If truck still has some space left but the boxes are not left
        return count


solution = Solution()

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 4
print(f"{boxTypes = } {truckSize = } {solution.maximumUnits(boxTypes, truckSize) = }")

boxTypes = [[1,3],[2,2],[3,1]]
truckSize = 8
print(f"{boxTypes = } {truckSize = } {solution.maximumUnits(boxTypes, truckSize) = }")

boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
print(f"{boxTypes = } {truckSize = } {solution.maximumUnits(boxTypes, truckSize) = }")

boxTypes = [[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[1,3],[2,5],[3,2]]
truckSize = 35
print(f"{boxTypes = } {truckSize = } {solution.maximumUnits(boxTypes, truckSize) = }")