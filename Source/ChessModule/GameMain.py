from GameEngine     import GameState
from GameEngine     import Move

from GameGraphics   import load_pieces
from GameGraphics   import draw_game_state

import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((512, 512))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))

    game_state = GameState()
    load_pieces()
    running = True

    square_selected     = tuple()
    player_clicks       = list()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()

                j = location[0] // 64
                i = location[1] // 64

                if square_selected == (i, j):
                    square_selected = tuple()
                    player_clicks   = list()
                else:
                    square_selected = (i, j)
                    player_clicks.append(square_selected)

                if len(player_clicks) == 2:
                    move = Move(player_clicks[0], player_clicks[1], game_state.board)
                    game_state.make_move(move)

                    square_selected = tuple()
                    player_clicks   = list()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_state.revert_move()

        draw_game_state(screen, game_state)
        clock.tick(15)
        pygame.display.flip()


if __name__ == '__main__':
    main()
