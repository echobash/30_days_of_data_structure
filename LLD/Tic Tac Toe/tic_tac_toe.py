class Player:
    sign = ""
    winner = ""

    def __init__(self, name):
        self.name = name


class Board:
    def __init__(self):
        self.board = [[-1, -1, -1],
                 [-1, -1, -1],
                 [-1, -1, -1]]

        self.size = 3

    def print_board(self):
        for i in range(3):
            for j in range(3):
                print(f"| {self.board[i][j]} |", end=" ")
            print()


    def update_board(self, x, y, sign):
        self.board[x][y] = sign

    def is_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == -1:
                    return False
        return True


class Game:
    current_turn = ""

    def __init__(self, player1, player2, board):
        self.player1 = player1
        self.player2 = player2
        self.board = board

    def assign_sign_to_player(self):
        self.player1.sign = "X"
        self.player2.sign = "O"

    def marks_sign_on_board(self, x, y, sign):
        self.board.update_board(x, y, sign)

    def start(self):
        self.assign_sign_to_player()
        self.current_turn = self.player1
        self.board.print_board()
        while not self.is_won() and not self.is_tie():
            self.print_current_turn_player()
            coordinates = input('Enter coordinate of cells (space separated)')
            x = int(coordinates.split()[0])
            y = int(coordinates.split()[1])
            self.marks_sign_on_board(x, y, self.current_turn.sign)
            self.switch_turn()
            self.board.print_board()
        if self.is_tie():
            print("Game is Draw")
            return
        else:
            self.switch_turn()
            self.current_turn.winner = self.current_turn.name
        print(f"Winner is {self.current_turn.winner }")

    def get_current_turn(self):
        return self.current_turn

    def print_current_turn_player(self):
        print( self.current_turn.name)

    def switch_turn(self):
        if self.current_turn == self.player1:
            self.current_turn = self.player2
        else:
            self.current_turn = self.player1

    def is_won(self):
        # Check for rows
        for i in range(3):
            if self.board.board[i][0] == self.board.board[i][1] == self.board.board[i][2] != -1:
                return True

        # Check for columns
        for i in range(3):
            if self.board.board[0][i] == self.board.board[1][i] == self.board.board[2][i] != -1:
                return True

        # Check for diagonal
        if self.board.board[0][0] == self.board.board[1][1] == self.board.board[2][2] != -1:
            return True
        # Check for reverse diagonal
        if self.board.board[0][2] == self.board.board[1][1] == self.board.board[2][0] != -1:
            return True

    def is_tie(self):
        return self.board.is_board_full()


board = Board()

player1 = Player("Ali")
player2 = Player("Mohit")

game = Game(player1, player2, board)
game.start()