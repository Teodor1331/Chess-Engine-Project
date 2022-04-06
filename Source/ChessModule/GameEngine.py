from GameHelpers import build_ranks_to_rows_notation
from GameHelpers import build_files_to_columns_notation


class GameState:
    def __init__(self):
        self.__board            =   self.generate_board()
        self.__move_functions   =   self.generate_functions()
        self.__whites_turn      =   True
        self.__blacks_turn      =   False
        self.__game_moves       =   list()


    @property
    def board(self):
        return self.__board


    @property
    def move_functions(self):
        return self.__move_functions


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


    @move_functions.setter
    def move_functions(self, move_functions):
        self.__move_functions = move_functions


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


    @move_functions.deleter
    def move_functions(self):
        del self.__move_functions


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
        del self.__move_functions
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


    def generate_functions(self):
        return {
            'P'     :   self.get_pawn_moves,
            'R'     :   self.get_rook_moves,
            'N'     :   self.get_knight_moves,
            'B'     :   self.get_bishop_moves,
            'Q'     :   self.get_queen_moves,
            'K'     :   self.get_king_moves,
        }

    
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


    def revert_move(self):
        if len(self.game_moves) != 0:
            move = self.__game_moves.pop()
            assert isinstance(move, Move)
            self.change_board_place(move.start_row, move.start_col, move.moved_piece)
            self.change_board_place(move.end_row, move.end_col, move.taken_piece)
            self.whites_turn = not self.whites_turn
            self.blacks_turn = not self.blacks_turn

    '''
        Decide all valid moves which consider checks.
        That are the moves that need the possible moves.
    '''
    def get_valid_moves(self):
        return self.get_possible_moves()


    '''
        Decide all moves which do not consider checks.
        That are the moves that are regular in the game.
    '''
    def get_possible_moves(self):
        moves = list()

        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                turn = self.board[i][j]

                condition1 = (turn >= 'A' and turn <= 'Z') and self.whites_turn
                condition2 = (turn >= 'a' and turn <= 'z') and self.blacks_turn

                if condition1 or condition2:
                    piece = self.board[i][j]
                    self.move_functions[piece.upper()](i, j, moves)

        return moves       


    def get_pawn_moves(self, i, j, moves):
        assert isinstance(moves, list)

        if self.whites_turn:
            if self.board[i - 1][j] == '.':
                moves.append(Move((i, j), (i - 1, j), self.board))

                if i == 6 and self.board[i - 2][j] == '.' and self.board[i - 1][j]:
                    moves.append(Move((i, j), (i - 2, j), self.board))

                if j - 1 >= 0:
                    if 'a' <= self.board[i - 1][j - 1] <= 'z':
                        moves.append(Move((i, j), (i - 1, j - 1), self.board))
                if j + 1 < 7:
                    if 'a' <= self.board[i - 1][j + 1] <= 'z':
                        moves.append(Move((i, j), (i - 1, j + 1), self.board))
        else:
            pass


    def get_rook_moves(self, i, j, moves):
        assert isinstance(moves, list)


    def get_knight_moves(self, i, j, moves):
        assert isinstance(moves, list)


    def get_bishop_moves(self, i, j, moves):
        assert isinstance(moves, list)


    def get_queen_moves(self, i, j, moves):
        assert isinstance(moves, list)


    def get_king_moves(self, i, j, moves):
        assert isinstance(moves, list)


    
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

        self.__move_id      =   self.generate_move_id()


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


    @property
    def move_id(self):
        return self.__move_id


    def __eq__(self, move):
        assert isinstance(move, Move)
        return self.move_id == move.move_id


    def __del__(self):
        del self.__start_row
        del self.__start_col

        del self.__end_row
        del self.__end_col

        del self.__moved_piece
        del self.__taken_piece

        del self.__move_id


    def __repr__(self):
        return  self.get_rank_file(self.start_row, self.start_col) + \
                self.get_rank_file(self.end_row, self.end_col)
 

    def get_rank_file(self, row, column):
        return self.COLUMNS_TO_FILES[column] + self.ROWS_TO_RANKS[row]


    def generate_move_id(self):
        return  self.start_row  * 1000   + \
                self.start_col  * 100    + \
                self.end_row    * 10     + \
                self.end_col    * 1
