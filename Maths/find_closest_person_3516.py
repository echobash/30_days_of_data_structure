class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        """
        x y z
        y x z

        x z y
        y z x

        z x y
        z y x
        """
        if abs(x - z) > abs(y - z):
            return 2
        elif abs(y - z) > abs(x - z):
            return 1
        return 0


sol = Solution()

x = 2
y = 7
z = 4
print(f"{x = } | {y = } | {z = } | {sol.findClosest(x,y,z) = }")

x = 2
y = 5
z = 6
print(f"{x = } | {y = } | {z = } | {sol.findClosest(x,y,z) = }")

x = 1
y = 5
z = 3
print(f"{x = } | {y = } | {z = } | {sol.findClosest(x,y,z) = }")
