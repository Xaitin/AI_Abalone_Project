from operator import sub

import pygame

from constants import WHITE, BOARD_SIZE, INITIAL_GAME_BOARD_SETUPS, WINDOW_WIDTH, WINDOW_HEIGHT
from enums.direction import DirectionEnum
from enums.move_type import MoveType
from helper.coordinate_helper import CoordinateHelper
from models.hexagon import Hexagon
from models.marble import Marble
from models.move import Move

SETUP_CONSTANT = 0


class Board:
    def __init__(self, win, setup=0):
        # 2D array
        self.hexagons = {}
        self.selected_hexagon = None
        self.selected_marbles = []
        self.black_left = self.white_left = 14
        self.win = win
        self.init_hexagons(win)

        self.teams = [None, pygame.sprite.Group(), pygame.sprite.Group()]
        self.marbles = pygame.sprite.Group()
        self.black_marble_list = list()
        self.white_marble_list = list()
        win.fill(WHITE)
        self.initialize_marbles(self.teams, setup)

    def generate_move(self, direction: DirectionEnum):
        if len(self.selected_marbles) == 1:
            marble = self.selected_marbles.pop()

            return Move(MoveType.InLine, marble.position_2d, DirectionEnum.get_direction_vector(direction))
        else:
            return None

    def init_hexagons(self, win):
        board_range = range(-BOARD_SIZE, BOARD_SIZE + 1)
        for x in board_range:
            for y in board_range:
                for z in board_range:
                    if (x + y + z == 0):
                        self.hexagons[(x, y)] = Hexagon(self, x, y, z, win)

    def initialize_marbles(self, teams, setup=0):
        for row, row_value in enumerate(INITIAL_GAME_BOARD_SETUPS[setup]):
            for col, value in enumerate(row_value):
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

        self.marbles.draw(self.win)

        for marble in self.selected_marbles:
            marble.draw_selection_circle(self.win)

    def on_click(self, click_position):
        x, y = click_position
        x_cent, y_cent = x - WINDOW_WIDTH / 2, y - WINDOW_HEIGHT / 2
        print(x_cent, y_cent)
        q, r = CoordinateHelper.fromXYtoCube(x_cent, y_cent)

        print("Mouse button down", x, y)
        print("Mouse button down", q, r)

        if not self.is_inside_game_board(q, r):
            print("outside of the gameboard")
            return

        self.select_marble(x, y)

        """
        Moving by clicking.. 
        We decided to just use select marbles by click and then keyboard input or button to move marbles. 
        """
        # if len(self.selected_marbles) > 0:
        #     position_cube = self.select_hexagon(q, r)
        #     if self.selected_hexagon is not None:
        #         self.selected_marbles.pop().move(position_cube)
        #         self.reset_selected_hexagon()

    def select_marble(self, x, y):
        # TODO change selected_team -> team of the turn
        try:
            selected_team = self.selected_marbles[0].team
        except IndexError:
            selected_team = None

        try:
            clicked_marble = next(filter(lambda marble: marble.rect.collidepoint(x, y), self.marbles))
        except StopIteration:
            return

        # only ally can be added unless no marble is selected yet
        if selected_team is None or clicked_marble.team == selected_team:
            n_selected = len(self.selected_marbles)

            if n_selected == 0:
                self.add_remove_selected_marble(clicked_marble)
            else:
                first_marble = self.selected_marbles[0]
                # when one marble is selected, only a neighbor ally marble can be added.
                if n_selected == 1 and CoordinateHelper.manhattan_distance(first_marble, clicked_marble) == 1:
                    self.add_remove_selected_marble(clicked_marble)
                elif n_selected == 2:
                    second_marble = self.selected_marbles[1]
                    direction = tuple(map(sub, second_marble.position_2d, first_marble.position_2d))

        return False

    def add_remove_selected_marble(self, marble):
        if marble not in self.selected_marbles:
            self.selected_marbles.append(marble)
            print("Marble added", marble)
            print(self.selected_marbles)

        else:
            self.selected_marbles.remove(marble)
            print("Marble removed", marble)
            print(self.selected_marbles)

    def is_marble_selected(self):
        return len(self.selected_marbles) > 0

    def apply_move(self, move: Move):
        marbles = filter(lambda marble: marble.position_2d == move.spots, self.marbles.sprites())
        for marble in marbles:
            marble.move_by_direction(DirectionEnum.get_from_2d(move.direction))

    def is_inside_game_board(self, x, y):
        z = -x - y
        return abs(x) <= BOARD_SIZE and abs(y) <= BOARD_SIZE and abs(z) <= BOARD_SIZE

    def reset_selected_marbles(self):
        self.selected_marbles = []

    def reset_selected_hexagon(self):
        self.selected_hexagon = None

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
