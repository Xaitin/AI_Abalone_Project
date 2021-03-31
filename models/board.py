import copy
from models.state_space import StateSpace
from helper.direction_helper import DirectionHelper
from operator import add, sub

import pygame

from constants import WHITE, BOARD_SIZE, INITIAL_GAME_BOARD_SETUPS, WINDOW_WIDTH, WINDOW_HEIGHT, EMPTY_GAME_BOARD_ARRAY, BOARD_ARRAY_SIZE, OUTSIDE_OF_THE_BOARD_VALUE
from enums.direction import DirectionEnum
from enums.move_type import MoveType
from enums.team_enum import TeamEnum
from helper.coordinate_helper import CoordinateHelper
from models import marble
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
        self.team_of_turn = TeamEnum.BLACK
        self.black_marble_list = list()
        self.white_marble_list = list()
        win.fill(WHITE)
        self.initialize_marbles(self.teams, setup)
        self.state_space = StateSpace(marble_positions=self.__str__(
        ), player=TeamEnum.get_team_str(self.team_of_turn))

    def __str__(self) -> str:
        marble_str_arr = []
        marble_str_arr += sorted([str(marble) for marble in self.marbles.sprites()
                                  if marble.team == TeamEnum.BLACK.value])
        marble_str_arr += sorted([str(marble) for marble in self.marbles.sprites()
                                  if marble.team == TeamEnum.WHITE.value])
        for marble_str in marble_str_arr:
            print(marble_str, end=', ')
        print()

        return marble_str_arr

    def switch_player(self):
        self.team_of_turn = TeamEnum.WHITE if self.team_of_turn == TeamEnum.BLACK else TeamEnum.BLACK

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
                            self.white_marble_list.append(
                                CoordinateHelper.from2DArraytoCube(position_2d))
                        if value == 1:
                            self.black_marble_list.append(
                                CoordinateHelper.from2DArraytoCube(position_2d))
                except ValueError:
                    pass

    def update(self):
        self.draw_hexagons()
        # self.check_position_2d()
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
        # try:
        #     selected_team = self.selected_marbles[0].team
        # except IndexError:
        #     selected_team = None
        #
        try:
            clicked_marble = next(
                filter(lambda marble: marble.rect.collidepoint(x, y), self.marbles))
        except StopIteration:
            print("no clicked marble?")
            return

        # only ally can be added unless no marble is selected yet
        if clicked_marble.team == self.team_of_turn.value:
            n_selected = len(self.selected_marbles)

            if n_selected == 0:
                self.add_selected_marble(clicked_marble)
            else:
                first_marble = self.selected_marbles[0]

                # Marble De-selection
                # Only allowing de-selection of the last selected marble.
                if clicked_marble == self.selected_marbles[-1]:
                    self.selected_marbles.remove(clicked_marble)
                    print("marble removed")
                    return

                # Marble Selection
                # when one marble is selected, only a neighbor ally marble can be added.
                if n_selected == 1 and CoordinateHelper.manhattan_distance(first_marble.position_2d,
                                                                           clicked_marble.position_2d) == 1:
                    self.add_selected_marble(clicked_marble)
                elif n_selected == 2:
                    second_marble = self.selected_marbles[1]
                    direction = tuple(
                        map(sub, second_marble.position_2d, first_marble.position_2d))
                    second_marble_next_spot = tuple(
                        map(add, second_marble.position_2d, direction))
                    if clicked_marble.position_2d == second_marble_next_spot:
                        self.add_selected_marble(clicked_marble)
        print(self.selected_marbles)
        print([marble.position_2d for marble in self.selected_marbles])
        return False

    def check_position_2d(self):
        print(self.black_marble_list)
        for index in self.black_marble_list:
            if index in self.boundary():
                print("black", index)
                self.black_marble_list.remove(index)
        for index in self.white_marble_list:
            if index in self.boundary():
                print("white", index)
                self.white_marble_list.remove(index)

    def boundary(self):
        boundaries = list()
        for i in range(BOARD_ARRAY_SIZE):
            for j in range(BOARD_ARRAY_SIZE):
                if EMPTY_GAME_BOARD_ARRAY[i][j] == OUTSIDE_OF_THE_BOARD_VALUE:
                    boundaries.append((i, j))
        return boundaries


    def add_selected_marble(self, marble):
        if marble not in self.selected_marbles:
            self.selected_marbles.append(marble)
            print("Marble added", marble)
            print(self.selected_marbles)

    def is_marble_selected(self):
        return len(self.selected_marbles) > 0

    def generate_move(self, move_direction: DirectionEnum):
        n_selected = len(self.selected_marbles)
        direction_vector_2d = DirectionEnum.get_direction_vector_2d(
            move_direction)

        if n_selected == 1:
            marble = self.selected_marbles[0]
            return Move(MoveType.InLine, marble.position_2d, direction_vector_2d)
        else:
            first_marble, second_marble = self.selected_marbles[0], self.selected_marbles[1]
            marble_alignment_direction = tuple(
                map(sub, second_marble.position_2d, first_marble.position_2d))

            if DirectionHelper.are_directions_on_the_same_axis(direction_vector_2d, marble_alignment_direction):
                move_type = MoveType.InLine

                # When you selected marbles in reversed-direction compared to the direction you wanna move
                if DirectionHelper.get_opposite_direction(direction_vector_2d) == marble_alignment_direction:
                    self.selected_marbles = list(reversed(self.selected_marbles))

            else:
                move_type = MoveType.SideStep

            move_spots = [
                marble.position_2d for marble in self.selected_marbles]

            return Move(move_type=move_type, spots=move_spots, direction=direction_vector_2d)

    def validate_move(self, move: Move):
        self.state_space.generate_all_resulting_board_states()
        valid_moves = self.state_space.get_move_list()
        print("state_space.marble_positions_2d", self.state_space.marble_positions_2d)
        print("state_space self.__str__()", self.__str__())
        print(valid_moves)
        return str(move) in self.state_space.get_move_list()

    def apply_move(self, move: Move):
        marbles = self.marbles.sprites()
        # marbles_for_move = list(filter(lambda marble: marble.position_2d in
        #                       move.spots, marbles))
        marbles_to_move = self.selected_marbles
        move_direction_enum = DirectionEnum.get_from_2d(move.direction)

        # SideStep move doesn't push other marbles
        if move.move_type == MoveType.SideStep:
            for marble in marbles_to_move:
                marble.move_by_direction(
                    move_direction_enum)

        # In-line move needs to push marbles in front of them
        else:
            last_marble = marbles_to_move[-1]
            next_spot = tuple(
                map(add, last_marble.position_2d, move.direction))
            next_marble = next(
                filter(lambda m: m.position_2d == next_spot, marbles), None)

            while next_marble is not None:
                marbles_to_move.append(next_marble)
                last_marble = marbles_to_move[-1]
                next_spot = tuple(
                    map(add, last_marble.position_2d, move.direction))
                next_marble = next(
                    filter(lambda m: m.position_2d == next_spot, marbles), None)


            for marble in reversed(marbles_to_move):
                marble.move_by_direction(move_direction_enum)

            # next_spot = tuple(
            #     map(add, last_marble.position_2d, move.direction))
            # next_marble = next(
            #     filter(lambda m: m.position_2d == next_spot, marbles), None)

            # len(marbles_to_move) == 2
            # # next_spot is empty
            # if next_marble is None:
            # else:
            #     marbles_to_move.append(next_marble)
            #     for marble in reversed(marbles_to_move):
            #         marble.move_by_direction(
            #             move_direction_enum)

            # len(marbles_to_move) == 3
            # # next_spot is empty
            # if next_marble is None:
            #     for marble in reversed(marbles_to_move):
            #         marble.move_by_direction(
            #             move_direction_enum)
            # else:
            #     marbles_to_move.append(next_marble)
            #     for marble in reversed(marbles_to_move):
            #         marble.move_by_direction(
            #             move_direction_enum)

        self.reset_selected_marbles()
        self.switch_player()
        self.update_state_space()

        return move



    def update_state_space(self):
        self.state_space = StateSpace(marble_positions=copy.copy(self.__str__()),
                                      player=TeamEnum.get_team_str(self.team_of_turn))

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
        marble_positions = [marble.get_position_cube()
                            for marble in self.selected_marbles]

        if self.selected_hexagon is None:
            if (x, y) not in marble_positions:
                self.selected_hexagon = selected
                return (x, y)
        elif selected in self.selected_hexagon:
            self.selected_hexagon = None
            return (x, y)
        else:
            pass
