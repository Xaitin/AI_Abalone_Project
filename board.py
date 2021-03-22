import pygame

from constants import WHITE, BOARD_SIZE, INITIAL_GAME_BOARD_SETUPS, WIDTH, HEIGHT
from coordinate_helper import CoordinateHelper
from hexagon import Hexagon
from marble import Marble

SETUP_CONSTANT = 0


class Board:

    def __init__(self, win):
        # 2D array
        self.hexagons = {}
        self.selected_hexagon = None
        self.selected_marbles = []
        self.black_left = self.white_left = 14
        self.win = win
        self.teams = [None, pygame.sprite.Group(), pygame.sprite.Group()]
        self.init_hexagons(win)
        self.marbles = pygame.sprite.Group()
        self.black_marble_list = list()
        self.white_marble_list = list()
        win.fill(WHITE)
        self.initialize_marbles(self.teams, SETUP_CONSTANT)

    def init_hexagons(self, win):
        board_range = range(-BOARD_SIZE, BOARD_SIZE + 1)
        for x in board_range:
            for y in board_range:
                for z in board_range:
                    if (x + y + z == 0):
                        self.hexagons[(x, y)] = Hexagon(self, x, y, z, win)

    def initialize_marbles(self, teams, setup=0):
        for row, row_value in enumerate(INITIAL_GAME_BOARD_SETUPS[setup][1: -1]):
            for col, value in enumerate(row_value[1: -1]):
                try:
                    if value > 0:
                        position_2d = [row, col]
                        Marble(position_2d, value, teams[value], self.marbles)
                        if value == 2:
                            self.white_marble_list.append(CoordinateHelper.from2DArraytoCube(position_2d))
                        if value == 1:
                            self.black_marble_list.append(CoordinateHelper.from2DArraytoCube(position_2d))


                except ValueError:
                    pass
        print(self.black_marble_list)

    def update(self):
        self.draw_hexagons()

        for team in self.teams[1:]:
            team.draw(self.win)

        for marble in self.selected_marbles:
            marble.draw_selection_circle(self.win)

    def on_click(self, click_position):
        x, y = click_position
        x_cent, y_cent = x - WIDTH / 2, y - HEIGHT / 2
        print(x_cent, y_cent)
        q, r = CoordinateHelper.fromXYtoCube(x_cent, y_cent)

        print("Mouse button down", x, y)
        print("Mouse button down", q, r)

        if not self.isInsideGameBoard(q, r):
            print("outside of the gameboard")
            return

        self.select_marble(x, y)
        if len(self.selected_marbles) > 0:
            position_cube = self.select_hexagon(q, r)
            if self.selected_hexagon is not None:
                self.selected_marbles.pop().move(position_cube)
                self.reset_selected_hexagon()

    def isInsideGameBoard(self, x, y):
        z = -x - y
        return abs(x) <= BOARD_SIZE and abs(y) <= BOARD_SIZE and abs(z) <= BOARD_SIZE

    def reset_selected_marbles(self):
        self.selected_marbles = []

    def reset_selected_hexagon(self):
        self.selected_hexagon = None

    def select_marble(self, x, y):
        for marble in self.marbles:
            if marble.rect.collidepoint(x, y):
                if marble not in self.selected_marbles:
                    self.selected_marbles.append(marble)
                    print(self.selected_marbles)
                    return True
                else:
                    self.selected_marbles.remove(marble)
                    print(self.selected_marbles)
                    return True

        return False

    def draw_hexagons(self):
        for position, hexagon in self.hexagons.items():
            hexagon.draw()

        if self.selected_hexagon is not None:
            self.selected_hexagon.draw_selected()
            # print(self.selected_hexagons)

    def select_hexagon(self, x, y):
        selected = self.hexagons[(x, y)]
        marble_positions = [marble.get_position_cube() for marble in self.selected_marbles]

        if self.selected_hexagon is None:
            if (x, y) not in marble_positions:
                self.selected_hexagon = selected
                return (x, y)
        elif selected in self.selected_hexagon:
            self.selected_hexagon = None
            return (x, y)
        else:
            pass
