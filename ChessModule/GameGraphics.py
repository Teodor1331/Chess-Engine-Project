from GameEngine import GameState


import pygame


IMAGES          =   dict()


def load_pieces():
    IMAGES['P']     =   pygame.transform.scale(pygame.image.load('../Images/White Pieces/White_Pawn.png'), (64, 64))
    IMAGES['R']     =   pygame.transform.scale(pygame.image.load('../Images/White Pieces/White_Rook.png'), (64, 64))
    IMAGES['N']     =   pygame.transform.scale(pygame.image.load('../Images/White Pieces/White_Knight.png'), (64, 64))
    IMAGES['B']     =   pygame.transform.scale(pygame.image.load('../Images/White Pieces/White_Bishop.png'), (64, 64))
    IMAGES['Q']     =   pygame.transform.scale(pygame.image.load('../Images/White Pieces/White_Queen.png'), (64, 64))
    IMAGES['K']     =   pygame.transform.scale(pygame.image.load('../Images/White Pieces/White_King.png'), (64, 64))

    IMAGES['p']     =   pygame.transform.scale(pygame.image.load('../Images/Black Pieces/Black_Pawn.png'), (64, 64))
    IMAGES['r']     =   pygame.transform.scale(pygame.image.load('../Images/Black Pieces/Black_Rook.png'), (64, 64))
    IMAGES['n']     =   pygame.transform.scale(pygame.image.load('../Images/Black Pieces/Black_Knight.png'), (64, 64))
    IMAGES['b']     =   pygame.transform.scale(pygame.image.load('../Images/Black Pieces/Black_Bishop.png'), (64, 64))
    IMAGES['q']     =   pygame.transform.scale(pygame.image.load('../Images/Black Pieces/Black_Queen.png'), (64, 64))
    IMAGES['k']     =   pygame.transform.scale(pygame.image.load('../Images/Black Pieces/Black_Knight.png'), (64, 64))


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
