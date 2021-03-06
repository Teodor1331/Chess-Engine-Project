# pylint: disable=E1101

"""Main module of the Chess Engine Project."""


import pygame

from game_engine import GameState
from game_engine import Move

from game_graphics import load_pieces
from game_graphics import draw_game_state


def main():
    """Run the whole logic of the project."""
    pygame.init()

    screen = pygame.display.set_mode((512, 512))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))

    game_state = GameState()
    load_pieces()
    running = True

    square_selected = ()
    player_clicks = []

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()

                j = location[0] // 64
                i = location[1] // 64

                if square_selected == (i, j):
                    square_selected = ()
                    player_clicks = []
                else:
                    square_selected = (i, j)
                    player_clicks.append(square_selected)

                if len(player_clicks) == 2:
                    coordinate1 = player_clicks[0][0]
                    coordinate2 = player_clicks[0][1]
                    figure = game_state.board[coordinate1][coordinate2]

                    if game_state.player_turn and 'A' <= figure <= 'Z':
                        move = Move(
                            player_clicks[0], player_clicks[1],
                            game_state.board
                        )
                        game_state.make_move(move)
                    elif not game_state.player_turn and 'a' <= figure <= 'z':
                        move = Move(
                            player_clicks[0], player_clicks[1],
                            game_state.board
                        )
                        game_state.make_move(move)

                    square_selected = ()
                    player_clicks = []
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_state.revert_move()

        draw_game_state(screen, game_state)
        clock.tick(15)
        pygame.display.flip()


if __name__ == '__main__':
    main()
