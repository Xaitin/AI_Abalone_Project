from operator import add

from constants import EMPTY_GAME_BOARD_ARRAY
from coordinate_helper import CoordinateHelper
from direction import DIRECTION_VECTORS
from position import Position
from team_enum import TeamEnum


class StateSpace:
    def __init__(self, marble_positions, player=None):
        self.marble_positions = [Position(TeamEnum.BLACK if position[0] == 'b' else TeamEnum.WHITE, position[1]) for
                                 position in
                                 self.read_position_strings(marble_positions)]
        self.player_of_turn = player
        self.marble_positions_2d = self.to2DArray(self.marble_positions)

    def read_position_strings(self, position_strings):
        translate_movements = list()
        # format example: [('b', (0, 2)), ('b', (0, 1)), ('b', (1, 0)), ('b', (0, 0))]
        for position_string in position_strings:
            player = position_string[-1]
            coord = position_string[:-1]
            translate_movements.append((player, CoordinateHelper.from_cube_str_to_cube(coord)))
        return translate_movements

    def to2DArray(self, marble_positions):
        result_array = EMPTY_GAME_BOARD_ARRAY
        for position in marble_positions:
            array_position_row, array_position_col = CoordinateHelper.fromCubeto2DArray(position.get_position(),
                                                                                        with_gutter=True)
            result_array[array_position_row][array_position_col] = position.get_team().value

        # print(result_array)
        # print(TEST_1_INPUT)
        # print(result_array == TEST_1_INPUT)
        return result_array

    def get_singular_move_resulting_marble_positions(self):
        resulting_marble_positions = []

        for index, position in enumerate(self.marble_positions):
            surroundings = self.get_surrounding_positions(position)
            valid_spots = [value for value in [spot if self.is_empty_spot(spot) else None for spot in surroundings] if
                           value is not None]
            for spot in valid_spots:
                new_state = self.marble_positions.copy()
                new_state[index] = Position(position.team, spot)
                resulting_marble_positions.append(new_state)

        return resulting_marble_positions

    def is_empty_spot(self, position_cube):
        position_2d = CoordinateHelper.fromCubeto2DArray(position_cube, with_gutter=True)

        if self.marble_positions_2d[position_2d[0]][position_2d[1]] == -1:
            return True
        else:
            return False

    def get_surrounding_positions(self, position_cube):
        surrounding_positions = []
        for direction in DIRECTION_VECTORS:
            surrounding_positions.append(tuple(map(add, position_cube.get_position(), direction)))

        # print(surrounding_positions)
        return surrounding_positions

    def __str__(self):
        return f"\nPlayer of the turn : {self.player_of_turn}\n" \
               f"Marble Positions: {self.marble_positions}\n"
