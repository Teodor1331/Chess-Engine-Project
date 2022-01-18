from GameEngine import GameState


import pygame


IMAGES          =   dict()
PIECES          =   {
    'P'     :   'Pawn',
    'R'     :   'Rook',
    'N'     :   'Knight',
    'B'     :   'Bishop',
    'Q'     :   'Queen',
    'K'     :   'King',
}


def load_pieces():
    elements = [
        ['../../Images/White Pieces/White_', 'PRNBQK'],
        ['../../Images/Black Pieces/Black_', 'prnbqk'],
    ]

    for element in elements:
        for literal in element[1]:
            IMAGES[literal] = pygame.transform.scale(
                pygame.image.load(element[0] + PIECES[literal.upper()] + '.png'),
                (64, 64))
                

def draw_board(screen):
    colors = [pygame.Color("white"), pygame.Color("gray")]

    for i in range(8):
        for j in range(8):
            sum_index = i + j
            remainder = sum_index % 2
            color = colors[remainder]
            pygame.draw.rect(screen, color, pygame.Rect(j * 64, i * 64, 64, 64))


def draw_pieces(screen, game_state):
    assert isinstance(screen, pygame.Surface)
    assert isinstance(game_state, GameState)

    for i in range(8):
        for j in range(8):
            piece = game_state.board[i][j]

            if piece != '.':
                screen.blit(IMAGES[piece], pygame.Rect(j * 64, i * 64, 64, 64))


def draw_game_state(screen, game_state):
    assert isinstance(screen, pygame.Surface)
    assert isinstance(game_state, GameState)

    draw_board(screen)
    draw_pieces(screen, game_state)
