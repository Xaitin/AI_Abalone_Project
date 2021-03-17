from constants import BLUE, RED, HEXAGON_SIDE_LENGTH, COS60, SIN60, WIDTH, HEIGHT
import math
from coordinate_helper import CoordinateHelper

class Hexagon:
    def __init__(self, board, x, y, z):
        if not self.validate(x, y, z):
            raise ValueError('coordinate value is wrong')

        self._board = board
        self._x = x
        self._y = y
        self._z =  -x - y
        self._occupied = False
        self._side_length = HEXAGON_SIDE_LENGTH
        self._color = BLUE if self._occupied else RED

    def occupy(self):
        self._occupied = True

    def unoccupy(self):
        self._occupied = False

    def get_vertices(self):
        # points should be a list of tuples
        # [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6)]
        left, top = CoordinateHelper.fromCubetoXY((self._x, self._y))
        points = []
        points.append((left, top + self._side_length))
        points.append((left + SIN60 * self._side_length, top + COS60 * self._side_length))
        points.append((left + SIN60 * self._side_length, top - COS60 * self._side_length))
        points.append((left, top - self._side_length))
        points.append((left - SIN60 * self._side_length, top - COS60 * self._side_length))
        points.append((left - SIN60 * self._side_length, top + COS60 * self._side_length))
        return points


    def validate(self, x, y, z):
        """
        Validate the Hexagon's cube coordinate. The sum should be zero.
        :return: a boolean
        """
        return (x + y + z) == 0