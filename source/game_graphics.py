"""Module with the methods for building the chess board."""

import pygame

from game_engine import GameState


IMAGES = {}
PIECES = {
    'P': 'Pawn',
    'R': 'Rook',
    'N': 'Knight',
    'B': 'Bishop',
    'Q': 'Queen',
    'K': 'King',
}
ELEMENTS = [
    ['../images/White Pieces/White_', 'PRNBQK'],
    ['../images/Black Pieces/Black_', 'prnbqk'],
]


def load_pieces() -> None:
    """Load pieces from the corresponding images."""
    for element in ELEMENTS:
        for literal in element[1]:
            path = element[0] + PIECES[literal.upper()]

            IMAGES[literal] = pygame.transform.scale(
                pygame.image.load(path + '.png'), (64, 64))


def draw_board(screen) -> None:
    """Draw the board (without the pieces on it)."""
    colors = [pygame.Color("white"), pygame.Color("gray")]

    for i in range(8):
        for j in range(8):
            sum_index = i + j
            remainder = sum_index % 2
            color = colors[remainder]
            pygame.draw.rect(
                screen, color, pygame.Rect(j * 64, i * 64, 64, 64)
            )


def draw_pieces(screen, game_state) -> None:
    """Draw the pieces (without the board under them)."""
    assert isinstance(screen, pygame.Surface)
    assert isinstance(game_state, GameState)

    for i in range(8):
        for j in range(8):
            piece = game_state.board[i][j]

            if piece != '.':
                screen.blit(IMAGES[piece], pygame.Rect(j * 64, i * 64, 64, 64))


def draw_game_state(screen, game_state) -> None:
    """Draw the game state (with both board and pieces)."""
    assert isinstance(screen, pygame.Surface)
    assert isinstance(game_state, GameState)

    draw_board(screen)
    draw_pieces(screen, game_state)
