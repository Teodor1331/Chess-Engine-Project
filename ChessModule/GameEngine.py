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
