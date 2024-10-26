class Chess:
    def __init__(self, square):
        self.square = square
        self.column_mapping_with_integer = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8
        }

    def get_color(self):
        if not self.is_valid_square():
            return "Invalid chess square"

        row = self.square[0]
        row = self.column_mapping_with_integer[row]
        column = int(self.square[1])

        if (row + column) % 2 == 0:
            return "Black"
        return "White"

    def is_valid_square(self):
        # Do not allow squares with length > 2 e.g e5d,a4hh etc
        if len(self.square) != 2:
            return False

        # Do not allow squares with row no > 8 e.g a9, b9, c9 etc.
        if int(self.square[1]) > 8:
            return False

        # Do not allow squares with column no > h e.g j2, p4, x8 etc.
        if self.square[0] not in self.column_mapping_with_integer:
            return False

        return True


chess = Chess('e4')
print(chess.get_color())