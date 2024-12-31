class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        column_mapping_with_integer = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8
        }
        row = coordinates[0]
        row = column_mapping_with_integer[row]
        column = int(coordinates[1])

        if (row + column) % 2 == 0:
            return False
        return True


sol = Solution()

coordinates = "a1"
print(coordinates,sol.squareIsWhite(coordinates))

coordinates = "h3"
print(coordinates,sol.squareIsWhite(coordinates))

coordinates = "c7"
print(coordinates,sol.squareIsWhite(coordinates))
