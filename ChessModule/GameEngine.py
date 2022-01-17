from GameHelpers import build_ranks_to_rows_notation
from GameHelpers import build_files_to_columns_notation


class GameState:
    def __init__(self):
        self.__board        =   self.generate_board()
        self.__whites_turn  =   True
        self.__blacks_turn  =   False
        self.__game_moves   =   list()


    @property
    def board(self):
        return self.__board


    @property
    def whites_turn(self):
        return self.__whites_turn


    @property
    def blacks_turn(self):
        return self.__blacks_turn


    @property
    def game_moves(self):
        return self.__game_moves


    @board.setter
    def board(self, board):
        self.__board = board


    @whites_turn.setter
    def whites_turn(self, whites_turn):
        self.__whites_turn = whites_turn


    @blacks_turn.setter
    def blacks_turn(self, blacks_turn):
        self.__blacks_turn = blacks_turn


    @game_moves.setter
    def game_moves(self, game_moves):
        self.__game_moves = game_moves


    @board.deleter
    def board(self):
        del self.__board

    @whites_turn.deleter
    def whites_turn(self):
        del self.__whites_turn


    @blacks_turn.deleter
    def blacks_turn(self):
        del self.__blacks_turn


    @game_moves.deleter
    def game_moves(self):
        del self.__game_moves


    def __del__(self):
        del self.__board
        del self.__whites_turn
        del self.__blacks_turn
        del self.__game_moves


    def generate_board(self):
        return [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

    
    def change_board_place(self, row, col, value):
        self.__board[row][col] = value


    def add_game_move(self, move):
        assert isinstance(move, Move)
        self.__game_moves.append(move)


    def make_move(self, move):
        assert isinstance(move, Move)

        if self.board[move.start_row][move.start_col] != '.':
            self.change_board_place(move.start_row, move.start_col, '.')
            self.change_board_place(move.end_row, move.end_col, move.moved_piece)
            self.add_game_move(move)
            self.whites_turn = not self.whites_turn
            self.blacks_turn = not self.blacks_turn


    def generate_pawn_moves(self, row, column):

        #white pawns start on row 6 and they move upwards
        if self.whites_turn:
            if self.board[row - 1][column] == ".":

                single_square_advance = Move([row, column], [row - 1, column], self.board)
                self.add_game_move(single_square_advance)

                if self.board[row - 2][column] == "." and row == 6:

                    double_square_advance = Move([row, column], [row - 2, column], self.board)
                    self.add_game_move(double_square_advance)

            elif column - 1 >= 0 and self.board[row - 1][column - 1] in "rnbqkp":
                attack_left = Move([row, column], [row - 1, column - 1], self.board)
                self.add_game_move(attack_left)

            elif column + 1 <= 7 and self.board[row - 1][column + 1] in "rnbqkp":
                attack_right = Move([row, column], [row - 1, column + 1], self.board)
                self.add_game_move(attack_right)

        #and black pawns start on row 2 and move downwards. Their column nomeration is also inverted and start from 8
        else:
            if self.board[row + 1][column] == ".":

                single_square_advance = Move([row, column], [row + 1, column], self.board)
                self.add_game_move(single_square_advance)

                if self.board[row + 2][column] == "." and row == 1:

                    double_square_advance = Move([row, column], [row + 2, column], self.board)
                    self.add_game_move(double_square_advance)

            elif column - 1 >= 0 and self.board[row + 1][column - 1] in "RNBQKP":
                attack_right = Move([row, column], [row + 1, column - 1], self.board)
                self.add_game_move(attack_right)

            elif column + 1 <= 7 and self.board[row + 1][column + 1] in "RNBQKP":
                attack_left = Move([row, column], [row + 1, column + 1], self.board)
                self.add_game_move(attack_left)


    def revert_move(self):
        if len(self.game_moves) != 0:
            move = self.__game_moves.pop()
            assert isinstance(move, Move)
            self.change_board_place(move.start_row, move.start_col, move.moved_piece)
            self.change_board_place(move.end_row, move.end_col, move.taken_piece)
            self.whites_turn = not self.whites_turn
            self.blacks_turn = not self.blacks_turn

    
class Move:
    RANKS_TO_ROWS       = build_ranks_to_rows_notation()
    FILES_TO_COLUMNS    = build_files_to_columns_notation()
    ROWS_TO_RANKS       = {value: key for key, value in RANKS_TO_ROWS.items()}
    COLUMNS_TO_FILES    = {value: key for key, value in FILES_TO_COLUMNS.items()}

    def __init__(self, start, end, board):
        self.__start_row    =   start[0]
        self.__start_col    =   start[1]

        self.__end_row      =   end[0]
        self.__end_col      =   end[1]

        self.__moved_piece  =   board[start[0]][start[1]]
        self.__taken_piece  =   board[end[0]][end[1]]


    @property
    def start_row(self):
        return self.__start_row


    @property
    def start_col(self):
        return self.__start_col


    @property
    def end_row(self):
        return self.__end_row


    @property
    def end_col(self):
        return self.__end_col


    @property
    def moved_piece(self):
        return self.__moved_piece


    @property
    def taken_piece(self):
        return self.__taken_piece


    def __del__(self):
        del self.__start_row
        del self.__start_col

        del self.__end_row
        del self.__end_col

        del self.__moved_piece
        del self.__taken_piece


    def __repr__(self):
        return  self.get_rank_file(self.start_row, self.start_col) + \
                self.get_rank_file(self.end_row, self.end_col)
 

    def get_rank_file(self, row, column):
        return self.COLUMNS_TO_FILES[column] + self.ROWS_TO_RANKS[row]
