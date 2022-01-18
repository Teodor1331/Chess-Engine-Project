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

    game_state  =   GameState()
    valid_moves =   game_state.get_valid_moves()
    made_move   =   False

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
                    print(move.__repr__())
                    if move in valid_moves:
                        game_state.make_move(move)
                        made_move = True

                    square_selected = tuple()
                    player_clicks   = list()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_state.revert_move()
                    made_move = True

        if made_move:
            valid_moves =   game_state.get_valid_moves()
            made_move   =   False

        draw_game_state(screen, game_state)
        clock.tick(15)
        pygame.display.flip()


if __name__ == '__main__':
    main()
