from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        values_set = set()

        # Check isValid row by row
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in values_set:
                    return False
                else:
                    values_set.add(board[i][j])
            values_set.clear()

        # Check isValid col by col
        for i in range(9):
            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in values_set:
                    return False
                else:
                    values_set.add(board[j][i])
            values_set.clear()

        # Check isValid box by box
        for i in range(3):
            for j in range(3):
                if board[i][j] == ".":
                    continue

                if board[i][j] in values_set:
                    return False
                else:
                    values_set.add(board[i][j])
        values_set.clear()

        for i in range(3):
            for j in range(3,6):
                if board[i][j] == ".":
                    continue
                if board[i][j] in values_set:
                    return False
                else:
                    values_set.add(board[i][j])
        values_set.clear()

        for i in range(3):
            for j in range(6,9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in values_set:
                    return False
                else:
                    values_set.add(board[i][j])
        values_set.clear()

        for i in range(3,6):
            for j in range(3):
                if board[i][j] == ".":
                    continue
                if board[i][j] in values_set:
                    return False
                else:
                    values_set.add(board[i][j])
        values_set.clear()

        for i in range(3,6):
            for j in range(3,6):
                if board[i][j] == ".":
                    continue
                if board[i][j] in values_set:
                    return False
                else:
                    values_set.add(board[i][j])
        values_set.clear()

        for i in range(3,6):
            for j in range(6,9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in values_set:
                    return False
                else:
                    values_set.add(board[i][j])
        values_set.clear()

        for i in range(6,9):
            for j in range(3):
                if board[i][j] == ".":
                    continue
                if board[i][j] in values_set:
                    return False
                else:
                    values_set.add(board[i][j])
        values_set.clear()

        for i in range(6,9):
            for j in range(3,6):
                if board[i][j] == ".":
                    continue
                if board[i][j] in values_set:
                    return False
                else:
                    values_set.add(board[i][j])
        values_set.clear()

        for i in range(6,9):
            for j in range(6,9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in values_set:
                    return False
                else:
                    values_set.add(board[i][j])
        values_set.clear()

        return True


sol = Solution()

board =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(f" {board[0] = } | {sol.isValidSudoku(board) = }")

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(f" {board[0] = } | {sol.isValidSudoku(board) = }")