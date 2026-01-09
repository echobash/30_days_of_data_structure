from typing import List


class Solution:
    def getSquareOfDistanceBetweenTwoPoints(self, x1, y1, x2, y2):
        return ((y2 - y1) ** 2) + (x2 - x1) ** 2

    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        p1p2 = self.getSquareOfDistanceBetweenTwoPoints(p1[0], p1[1], p2[0], p2[1])
        p1p3 = self.getSquareOfDistanceBetweenTwoPoints(p1[0], p1[1], p3[0], p3[1])
        p1p4 = self.getSquareOfDistanceBetweenTwoPoints(p1[0], p1[1], p4[0], p4[1])
        p2p3 = self.getSquareOfDistanceBetweenTwoPoints(p2[0], p2[1], p3[0], p3[1])
        p2p4 = self.getSquareOfDistanceBetweenTwoPoints(p2[0], p2[1], p4[0], p4[1])
        p3p4 = self.getSquareOfDistanceBetweenTwoPoints(p3[0], p3[1], p4[0], p4[1])
        sorted_sides = sorted([p1p2, p1p3, p1p4, p2p3, p2p4, p3p4])
        return (sorted_sides[0] == sorted_sides[1] == sorted_sides[2] == sorted_sides[3] != sorted_sides[4]) and (
                    sorted_sides[4] == sorted_sides[5])

        """
        Logic
        given 4 points, we can form 4C2 i.e 6 lines (4 sides and 2 diagonals)
        but the problem is that we don't know for sure that the cordinates are in order.

        So we find the distance of all 6 lines and it is a sqaure iff
        - 4 distances will be equal
        - 2 distances will be equal
        - not all 6 distance should be equal
        """


sol = Solution()

p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]
print(f"{p1 = } | {p2 = } | {p3 = } | {p4 = } | {sol.validSquare(p1, p2, p3, p4) = }")

p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,12]
print(f"{p1 = } | {p2 = } | {p3 = } | {p4 = } | {sol.validSquare(p1, p2, p3, p4) = }")

p1 = [0,0]
p2 = [0,0]
p3 = [0,0]
p4 = [0,0]
print(f"{p1 = } | {p2 = } | {p3 = } | {p4 = } | {sol.validSquare(p1, p2, p3, p4) = }")

p1 = [0,0]
p2 = [5,0]
p3 = [5,4]
p4 = [0,4]
print(f"{p1 = } | {p2 = } | {p3 = } | {p4 = } | {sol.validSquare(p1, p2, p3, p4) = }")

p1 = [1,0]
p2 = [-1,0]
p3 = [0,1]
p4 = [0,-1]
print(f"{p1 = } | {p2 = } | {p3 = } | {p4 = } | {sol.validSquare(p1, p2, p3, p4) = }")

