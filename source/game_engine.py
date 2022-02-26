"""Module with the engine logic of the project."""

from typing import List

from game_helpers import build_ranks_to_rows_notation
from game_helpers import build_files_to_columns_notation


class GameState:
    """Class for managing the state of a game."""

    def __init__(self) -> None:
        self.__board        =   [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        self.__whites_turn  =   True
        self.__blacks_turn  =   False
        self.__game_moves   =   []


    @property
    def board(self) -> List[List[str]]:
        """Return the board property of the class."""
        return self.__board


    @property
    def whites_turn(self) -> bool:
        """Return the whites turn property of the class."""
        return self.__whites_turn


    @property
    def blacks_turn(self) -> bool:
        """Return the blacks turn property of the class."""
        return self.__blacks_turn


    @property
    def game_moves(self) -> list:
        """Return the game moves property of the class."""
        return self.__game_moves


    @board.deleter
    def board(self) -> None:
        del self.__board

    @whites_turn.deleter
    def whites_turn(self) -> None:
        del self.__whites_turn


    @blacks_turn.deleter
    def blacks_turn(self) -> None:
        del self.__blacks_turn


    @game_moves.deleter
    def game_moves(self) -> None:
        del self.__game_moves


    def change_board_place(self, row, col, value) -> None:
        """Change the piece place on the board."""
        self.__board[row][col] = value


    def add_game_move(self, move) -> None:
        """Add a new game move to the game state moves."""
        assert isinstance(move, Move)
        self.__game_moves.append(move)


    def make_move(self, move) -> None:
        """Make a move in the current game state."""
        assert isinstance(move, Move)

        if self.board[move.start_row][move.start_col] != '.':
            self.change_board_place(move.start_row, move.start_col, '.')
            self.change_board_place(move.end_row, move.end_col, move.moved_piece)
            self.add_game_move(move)
            self.__whites_turn = not self.whites_turn
            self.__blacks_turn = not self.blacks_turn


    def revert_move(self) -> None:
        """Revert a move from the current game state."""
        if len(self.game_moves) != 0:
            move = self.__game_moves.pop()
            assert isinstance(move, Move)
            self.change_board_place(move.start_row, move.start_col, move.moved_piece)
            self.change_board_place(move.end_row, move.end_col, move.taken_piece)
            self.__whites_turn = not self.whites_turn
            self.__blacks_turn = not self.blacks_turn


    def generate_pawn_moves(self, row, column):
        """Generate all possible pawn moves."""

        #white pawns start on row 6 and they move upwards
        if self.whites_turn:
            if self.board[row - 1][column] == ".":

                single_square_advance = Move([row, column], [row - 1, column], self.board)
                self.add_game_move(single_square_advance)

                if self.board[row - 2][column] == "." and row == 6:

                    double_square_advance = Move([row, column], [row - 2, column], self.board)
                    self.add_game_move(double_square_advance)

            elif column - 1 >= 0 and self.board[row - 1][column - 1] in "rnbqp":
                attack_left = Move([row, column], [row - 1, column - 1], self.board)
                self.add_game_move(attack_left)

            elif column + 1 <= 7 and self.board[row - 1][column + 1] in "rnbqp":
                attack_right = Move([row, column], [row - 1, column + 1], self.board)
                self.add_game_move(attack_right)

        # and black pawns start on row 2 and move downwards.
        # Their column nomeration is also inverted and start from 8
        else:
            if self.board[row + 1][column] == ".":

                single_square_advance = Move([row, column], [row + 1, column], self.board)
                self.add_game_move(single_square_advance)

                if self.board[row + 2][column] == "." and row == 1:

                    double_square_advance = Move([row, column], [row + 2, column], self.board)
                    self.add_game_move(double_square_advance)

            elif column - 1 >= 0 and self.board[row + 1][column - 1] in "RNBQP":
                attack_right = Move([row, column], [row + 1, column - 1], self.board)
                self.add_game_move(attack_right)

            elif column + 1 <= 7 and self.board[row + 1][column + 1] in "RNBQP":
                attack_left = Move([row, column], [row + 1, column + 1], self.board)
                self.add_game_move(attack_left)


    def generate_rook_moves(self, row, column):
        """Generate all possible rook moves."""

        #expressing up, down, left and right directions with pairs of coefficients
        #the first coefficient resembles row direction, the second one - column
        moving_directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for direction in moving_directions:

            for i in range(1, 7):

                next_row_square = row + direction[0] * i
                next_column_square = column + direction[1] * i

                if 0 <= next_row_square < 8 and 0 <= next_column_square < 8:
                    if self.board[next_row_square][next_column_square] == '.':
                        start = [row, column]
                        end = [next_row_square, next_column_square]
                        advance = Move(start, end, self.board)
                        self.add_game_move(advance)

                    elif self.whites_turn and self.board[next_row_square][next_column_square] in "rnbqp":
                        attack = Move([row, column], [next_row_square, next_column_square], self.board)
                        self.add_game_move(attack)

                    elif self.whites_turn is False and self.board[next_row_square][next_column_square] in "RNBQP":
                        attack = Move([row, column], [next_row_square, next_column_square], self.board)
                        self.add_game_move(attack)
                    else:
                        break

                else:
                    break


    def generate_bishop_moves(self, row, column):
        """Generate all possible bishop moves."""

        # pretty similar to how a rook would move, just diagonally
        # the first coefficient resembles row direction, the second one - column
        moving_directions = [[1, 1], [1, -1], [-1, 1], [-1, -1]]

        for direction in moving_directions:

            for i in range(1, 7):

                next_row_square = row + direction[0] * i
                next_column_square = column + direction[1] * i

                if 0 <= next_row_square < 8 and 0 <= next_column_square < 8:

                    if self.board[next_row_square][next_column_square] == '.':

                        advance = Move([row, column], [next_row_square, next_column_square], self.board)
                        self.add_game_move(advance)

                    elif self.whites_turn and self.board[next_row_square][next_column_square] in "rnbqp":

                        attack = Move([row, column], [next_row_square, next_column_square], self.board)
                        self.add_game_move(attack)

                    elif self.whites_turn is False and self.board[next_row_square][next_column_square] in "RNBQP":

                        attack = Move([row, column], [next_row_square, next_column_square], self.board)
                        self.add_game_move(attack)

                    else:
                        break

                else:
                    break


    def generate_knight_moves(self, row, column):
        """Generate all possible knigh moves."""

        #knights move in Г formation, which can be expressed as doube square moves in any
        # direction and one additional in a direction perpendicular to it
        #thus, we have 8 possible possitions for a knight
        possible_possitions = [[2, 1], [2, -1], [-2, 1], [-2, -1],
                               [1, 2], [1, -2], [-1, 2], [-1, -2]]

        for position in possible_possitions:

            next_row_square = row + position[0]
            next_column_square = column + position[1]

            if 0 <= next_row_square < 8 and 0 <= next_column_square < 8:

                if self.board[next_row_square][next_column_square] == '.':

                    advance = Move([row, column], [next_row_square, next_column_square], self.board)
                    self.add_game_move(advance)

                elif self.whites_turn and self.board[next_row_square][next_column_square] in "rnbqp":

                    attack = Move([row, column], [next_row_square, next_column_square], self.board)
                    self.add_game_move(attack)

                elif self.whites_turn is False and self.board[next_row_square][next_column_square] in "RNBQP":

                    attack = Move([row, column], [next_row_square, next_column_square], self.board)
                    self.add_game_move(attack)

            else:
                break


    def generate_queen_moves(self, row, column):
        """Generate all possible queen moves."""

        #queens literally move like rooks and bishops combined
        self.generate_rook_moves(row, column)
        self.generate_bishop_moves(row, column)


class Move:
    """Class for managing the move logic in the game."""

    RANKS_TO_ROWS       = build_ranks_to_rows_notation()
    FILES_TO_COLUMNS    = build_files_to_columns_notation()
    ROWS_TO_RANKS       = {value: key for key, value in RANKS_TO_ROWS.items()}
    COLUMNS_TO_FILES    = {value: key for key, value in FILES_TO_COLUMNS.items()}

    def __init__(self, start, end, board) -> None:
        self.__start_row    =   start[0]
        self.__start_col    =   start[1]

        self.__end_row      =   end[0]
        self.__end_col      =   end[1]

        self.__moved_piece  =   board[start[0]][start[1]]
        self.__taken_piece  =   board[end[0]][end[1]]


    @property
    def start_row(self) -> int:
        """Return the start row property of the class."""
        return self.__start_row


    @property
    def start_col(self) -> int:
        """Return the start col property of the class."""
        return self.__start_col


    @property
    def end_row(self) -> int:
        """Return the end row property of the class."""
        return self.__end_row


    @property
    def end_col(self) -> int:
        """Return the end col property of the class."""
        return self.__end_col


    @property
    def moved_piece(self) -> str:
        """Return the moved piece property of the class."""
        return self.__moved_piece


    @property
    def taken_piece(self) -> str:
        """Return the taken piece property of the class."""
        return self.__taken_piece


    def __repr__(self) -> str:
        return  self.get_rank_file(self.start_row, self.start_col) + \
                self.get_rank_file(self.end_row, self.end_col)


    def get_rank_file(self, row, column) -> str:
        """Return move notation according to the chess game conditions."""
        return self.COLUMNS_TO_FILES[column] + self.ROWS_TO_RANKS[row]
