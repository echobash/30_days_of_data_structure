class Solution:
    def get_color(self, x, y):
        if (x + y) % 2 == 0:
            return "white"
        return "black"

    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        row1, col1, row2, col2 = coordinate1[0], coordinate1[1], coordinate2[0], coordinate2[1]

        char_to_no_mapping = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8
        }
        if self.get_color(char_to_no_mapping[row1], int(col1)) == self.get_color(char_to_no_mapping[row2], int(col2)):
            return True
        return False


sol = Solution()

coordinate1 = "a1"
coordinate2 = "c3"
print(f"{coordinate1 = } {coordinate2 = } {sol.checkTwoChessboards(coordinate1, coordinate2) = }")

coordinate1 = "a1"
coordinate2 = "h3"
print(f"{coordinate1 = } {coordinate2 = } {sol.checkTwoChessboards(coordinate1, coordinate2) = }")