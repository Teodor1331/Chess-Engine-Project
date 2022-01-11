from GameEngine     import GameState
from GameGraphics   import *

import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((512, 512))
    clock = pygame.time.Clock()
    screen.fill(pygame.Color("white"))

    game_state = GameState()
    load_pieces()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        draw_game_state(screen, game_state)
        clock.tick(15)
        pygame.display.flip()


if __name__ == '__main__':
    main()
