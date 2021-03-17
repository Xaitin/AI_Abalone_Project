import math
from constants import COS30, SIN30, HEXAGON_SIDE_LENGTH, WIDTH, HEIGHT, BOARD_SIZE


class CoordinateHelper:
    @staticmethod
    def fromXYtoCube(self, x, y):
        pass

    @staticmethod
    def fromCubetoXY(position):
        _left = ((2 * COS30) * position[0] + COS30 * position[1]) * HEXAGON_SIDE_LENGTH + WIDTH / 2
        _top = 3 * SIN30 * position[1] * HEXAGON_SIDE_LENGTH + HEIGHT / 2
        return _left, _top

    @staticmethod
    def from2DArraytoCube(position_2d):
        # print("2DArray", position_2d)
        return position_2d[1] - BOARD_SIZE, position_2d[0] - BOARD_SIZE

    @staticmethod
    def from2DArraytoXY(position_2d):
        cubePos = CoordinateHelper.from2DArraytoCube(position_2d)
        # print("Cube Pos", cubePos)
        return CoordinateHelper.fromCubetoXY(cubePos)
