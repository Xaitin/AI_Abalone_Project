import pygame
from board import Board
from constants import *
from marble import Marble

FPS = 60
SETUP_CONSTANT = 0

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Abalone")


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    teams = [None, pygame.sprite.Group(), pygame.sprite.Group()]
    marbles = pygame.sprite.Group()
    selected_marbles = []
    setup = SETUP_CONSTANT
    initialize_marbles(teams, marbles, setup)
    game_board_img = pygame.image.load('drawables/game_board.png')

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print("Mouse button down", x, y)
                for marble in marbles:
                    if marble.rect.collidepoint(x, y):
                        if marble not in selected_marbles:
                            selected_marbles.append(marble)
                        else:
                            selected_marbles.remove(marble)
                        # print(marble.rect, marble.groups())
                        print(selected_marbles)

        WIN.blit(game_board_img, dest=(300, 300), area=pygame.Rect(300,300, 300, 300))
        board.draw_hexagons(WIN)
        for team in teams[1:]:
            team.draw(WIN)
        pygame.display.update()

    pygame.quit()


def initialize_marbles(teams, marbles, setup=0):
    for row, row_value in enumerate(INITIAL_GAME_BOARD_SETUPS[setup][1: -1]):
        for col, value in enumerate(row_value[1: -1]):
            try:
                if value > 0:
                    position_2d = [row, col]
                    Marble(position_2d, value, teams[value], marbles)

                    # print(position_2d, value)

            except ValueError:
                pass


if __name__ == '__main__':
    main()
