import pygame

from board import Board
from constants import *

FPS = 60

WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Abalone")


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board(WIN)
    game_board_img = pygame.image.load('drawables/game_board.png').convert_alpha()
    game_board_img = pygame.transform.scale(game_board_img, (BOARD_IMAGE_SIZE, BOARD_IMAGE_SIZE))
    game_board_img_dest = (WINDOW_WIDTH / 2 - game_board_img.get_width() / 2, WINDOW_HEIGHT / 2 - game_board_img.get_height() / 2)

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Mouse Handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.on_click(event.pos)

            # Keyboard handling
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    board.reset_selected_marbles()

        WIN.blit(game_board_img, dest=game_board_img_dest)
        board.update()
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
