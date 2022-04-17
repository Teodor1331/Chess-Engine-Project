"""Tests on the module with the engine logic of the project."""

from inspect import ismethod

import pytest

from game_engine import GameState
from game_engine import Move

from game_helpers import build_ranks_to_rows_notation
from game_helpers import build_files_to_columns_notation


@pytest.fixture(name='game_state')
def fixture_game_state():
    """Return a GameState fixture."""
    return GameState()


@pytest.fixture(name="game_board")
def fixture_game_board():
    """Return a game board fixture."""
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


@pytest.fixture(name='move1')
def fixture_move1(game_board):
    """Return an example Move fixtiure."""
    return Move([0, 1], [1, 0], game_board)


@pytest.fixture(name='move2')
def fixture_move2(game_board):
    """Return an example Move fixture."""
    return Move([3, 4], [4, 3], game_board)


@pytest.fixture(name='move3')
def fixture_move3(game_board):
    """Return an example Move fixture."""
    return Move([6, 7], [7, 6], game_board)


def test_game_state_initializer(game_state):
    """Test the GameState class initializer."""
    assert isinstance(game_state, GameState)
    assert 'game_state' in locals()
    assert locals()['game_state'] is game_state


def test_game_state_properties(game_state, game_board):
    """Test the GameState class properties."""
    assert isinstance(game_state, GameState)

    assert hasattr(game_state, 'board')
    assert hasattr(game_state, 'player_turn')
    assert hasattr(game_state, 'game_moves')

    # assert isinstance(game_state.board, List[List[str]])
    assert isinstance(game_state.player_turn, bool)
    assert isinstance(game_state.game_moves, list)

    assert game_state.board == game_board
    assert game_state.player_turn is True
    assert game_state.game_moves == []


def test_game_state_deleters(game_state):
    """Test the GameState class deleters."""
    assert isinstance(game_state, GameState)

    del game_state.board
    del game_state.player_turn
    del game_state.game_moves

    assert not hasattr(game_state, 'board')
    assert not hasattr(game_state, 'player_turn')
    assert not hasattr(game_state, 'game_moves')


def test_game_state_methods(game_state):
    """Test the existence of the GameState class methods."""
    assert isinstance(game_state, GameState)

    assert hasattr(game_state, 'change_board_place')
    assert hasattr(game_state, 'add_game_move')
    assert hasattr(game_state, 'make_move')

    assert hasattr(game_state, 'generate_pawn_moves')
    assert hasattr(game_state, 'generate_rook_moves')
    assert hasattr(game_state, 'generate_bishop_moves')
    assert hasattr(game_state, 'generate_knight_moves')
    assert hasattr(game_state, 'generate_queen_moves')

    assert ismethod(game_state.change_board_place)
    assert ismethod(game_state.add_game_move)
    assert ismethod(game_state.make_move)
    assert ismethod(game_state.revert_move)

    assert ismethod(game_state.generate_pawn_moves)
    assert ismethod(game_state.generate_rook_moves)
    assert ismethod(game_state.generate_bishop_moves)
    assert ismethod(game_state.generate_knight_moves)
    assert ismethod(game_state.generate_queen_moves)


def test_game_state_change_board_place_method(game_state):
    """Test change board place method in the GameState class."""
    assert isinstance(game_state, GameState)

    for i in range(8):
        for j in range(8):
            game_state.change_board_place(i, j, '.')

    for i in range(8):
        for j in range(8):
            assert isinstance(game_state.board[i][j], str)
            assert game_state.board[i][j] == '.'


def test_move_constants():
    """Test the move class constants."""
    assert Move.RANKS_TO_ROWS == build_ranks_to_rows_notation()
    assert Move.FILES_TO_COLUMNS == build_files_to_columns_notation()

    assert Move.ROWS_TO_RANKS == {
        7: '1', 6: '2', 5: '3', 4: '4',
        3: '5', 2: '6', 1: '7', 0: '8'
    }

    assert Move.COLUMNS_TO_FILES == {
        0: 'a', 1: 'b', 2: 'c', 3: 'd',
        4: 'e', 5: 'f', 6: 'g', 7: 'h',
    }


def test_move_initializer(move1, move2, move3):
    """Test the Move class initializer."""
    assert isinstance(move1, Move)
    assert isinstance(move2, Move)
    assert isinstance(move3, Move)

    assert 'move1' in locals()
    assert 'move2' in locals()
    assert 'move3' in locals()

    assert locals()['move1'] is move1
    assert locals()['move2'] is move2
    assert locals()['move3'] is move3


def test_move_properties(move1, move2, move3):
    """Test the Move class properties."""
    assert isinstance(move1, Move)
    assert isinstance(move2, Move)
    assert isinstance(move3, Move)

    assert hasattr(move1, 'start_row')
    assert hasattr(move2, 'start_row')
    assert hasattr(move3, 'start_row')

    assert hasattr(move1, 'start_col')
    assert hasattr(move2, 'start_col')
    assert hasattr(move3, 'start_col')

    assert hasattr(move1, 'end_row')
    assert hasattr(move2, 'end_row')
    assert hasattr(move3, 'end_row')

    assert hasattr(move1, 'end_col')
    assert hasattr(move2, 'end_col')
    assert hasattr(move3, 'end_col')

    assert hasattr(move1, 'moved_piece')
    assert hasattr(move2, 'moved_piece')
    assert hasattr(move3, 'moved_piece')

    assert hasattr(move1, 'taken_piece')
    assert hasattr(move2, 'taken_piece')
    assert hasattr(move3, 'taken_piece')

    assert isinstance(move1.start_row, int)
    assert isinstance(move2.start_row, int)
    assert isinstance(move3.start_row, int)

    assert isinstance(move1.start_col, int)
    assert isinstance(move2.start_col, int)
    assert isinstance(move3.start_col, int)

    assert isinstance(move1.end_row, int)
    assert isinstance(move2.end_row, int)
    assert isinstance(move3.end_row, int)

    assert isinstance(move1.end_col, int)
    assert isinstance(move2.end_col, int)
    assert isinstance(move3.end_col, int)

    assert isinstance(move1.moved_piece, str)
    assert isinstance(move2.moved_piece, str)
    assert isinstance(move3.moved_piece, str)

    assert isinstance(move1.taken_piece, str)
    assert isinstance(move2.taken_piece, str)
    assert isinstance(move3.taken_piece, str)

    assert move1.start_row == move1.end_col == 0
    assert move2.start_row == move2.end_col == 3
    assert move3.start_row == move3.end_col == 6

    assert move1.start_col == move1.end_row == 1
    assert move2.start_col == move2.end_row == 4
    assert move3.start_col == move3.end_row

    assert move1.moved_piece == move3.taken_piece.lower() == 'n'
    assert move2.moved_piece == move2.taken_piece == '.'
    assert move3.moved_piece == move1.taken_piece.upper() == 'P'


def test_move_methods(move1, move2, move3):
    """Test for the existence of the Move class methods."""
    assert isinstance(move1, Move)
    assert isinstance(move2, Move)
    assert isinstance(move3, Move)

    assert hasattr(move1, 'get_rank_file')
    assert hasattr(move2, 'get_rank_file')
    assert hasattr(move3, 'get_rank_file')

    assert ismethod(move1.get_rank_file)
    assert ismethod(move2.get_rank_file)
    assert ismethod(move3.get_rank_file)


def test_move_get_rank_file_method(move1, move2, move3):
    """Test the get rak file method in the Move class."""
    assert isinstance(move1, Move)
    assert isinstance(move2, Move)
    assert isinstance(move3, Move)

    assert isinstance(move1.get_rank_file(0, 0), str)
    assert isinstance(move2.get_rank_file(3, 3), str)
    assert isinstance(move3.get_rank_file(6, 6), str)

    assert move1.get_rank_file(0, 0) == 'a8'
    assert move2.get_rank_file(3, 3) == 'd5'
    assert move3.get_rank_file(6, 6) == 'g2'


def test_move_representation_method(move1, move2, move3):
    """Test the representation of the Move class."""
    assert isinstance(move1, Move)
    assert isinstance(move2, Move)
    assert isinstance(move3, Move)

    assert str(move1) == 'b8a7'
    assert str(move2) == 'e5d4'
    assert str(move3) == 'h2g1'
