import math
from typing import Tuple

from constants import COS30, SIN30, HEXAGON_SIDE_LENGTH, WINDOW_WIDTH, WINDOW_HEIGHT, BOARD_SIZE, NUMBER_SHIFT, \
    LETTER_SHIFT


class CoordinateHelper:
    @staticmethod
    def fromXYtoCube(x, y):
        q = round((math.sqrt(3) / 3 * x - 1 / 3 * y) / HEXAGON_SIDE_LENGTH)
        r = round((2 / 3 * y) / HEXAGON_SIDE_LENGTH)
        return q, r

    @staticmethod
    def fromCubetoXY(position):
        _left = ((2 * COS30) * position[0] + COS30 *
                 position[1]) * HEXAGON_SIDE_LENGTH + WINDOW_WIDTH / 2
        _top = 3 * SIN30 * position[1] * \
            HEXAGON_SIDE_LENGTH + WINDOW_HEIGHT / 2
        return _left, _top

    @staticmethod
    def from_2d_array_to_cube(position_2d: Tuple[int, int], with_gutter=True):
        # print("2DArray", position_2d)
        # The "-1" that was originally here for each variable is now used when this function is used in state_space.
        # It was removed because it shifted the marble positions on the game board.
        if with_gutter:
            return position_2d[1] - BOARD_SIZE - 1, position_2d[0] - BOARD_SIZE - 1
        return position_2d[1] - BOARD_SIZE, position_2d[0] - BOARD_SIZE

    @staticmethod
    def from_cube_to_2d_array(cube_position):
        return cube_position[1] + BOARD_SIZE + 1, cube_position[0] + BOARD_SIZE + 1

    @staticmethod
    def from_2d_array_to_xy(position_2d):
        cubePos = CoordinateHelper.from_2d_array_to_cube(position_2d)
        # print("Cube Pos", cubePos)
        return CoordinateHelper.fromCubetoXY(cubePos)

    @staticmethod
    def from_cube_str_to_cube(coord):
        # ex. input: F6 -> output: (1, -1)
        x = int(coord[1]) - NUMBER_SHIFT
        y = LETTER_SHIFT - ord(coord[0])
        return x, y

    @staticmethod
    def from_cube_str_to_2d(coord):
        # ex. input: F6 -> output: (1, -1)
        pos_cube = CoordinateHelper.from_cube_str_to_cube(coord)
        return CoordinateHelper.from_cube_to_2d_array(pos_cube)

    @staticmethod
    def from_cube_to_cube_str(cube):
        # ex. input: (1, -1) -> output: F6
        x = chr(LETTER_SHIFT - cube[1])
        y = NUMBER_SHIFT + cube[0]
        return x + str(y)

    @staticmethod
    def from_2d_to_cube_str(position_2d: Tuple[int, int], with_gutter=True):
        if with_gutter:
            return CoordinateHelper.from_cube_to_cube_str(
                CoordinateHelper.from_2d_array_to_cube(position_2d, with_gutter=with_gutter))
        return CoordinateHelper.from_cube_to_cube_str(
            CoordinateHelper.from_2d_array_to_cube(position_2d, with_gutter=with_gutter))

    @staticmethod
    def get_manhattan_distance(position_a: Tuple[int, int], position_b: Tuple[int, int]) -> int:
        return (abs(position_a[0] - position_b[0])
                + abs(position_a[0] + position_a[1] -
                      position_b[0] - position_b[1])
                + abs(position_a[1] - position_b[1])) / 2
