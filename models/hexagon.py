from operator import sub

import pygame
from pygame.sprite import Sprite

from constants import BLUE, RED, HEXAGON_SIDE_LENGTH, COS60, SIN60, HEXAGON_OUTLINE_COLOR, SELECTED_HEXAGON_COLOR, \
    BOARD_COLOR, TEXT_ON_HEXAGON_COLOR
from helper.coordinate_helper import CoordinateHelper


class Hexagon(Sprite):
    def __init__(self, board, x, y, z, win):
        if not self.validate(x, y, z):
            raise ValueError('coordinate value is wrong')

        Sprite.__init__(self)

        self._board = board
        self._x = x
        self._y = y
        self._z = -x - y
        self.position_2d = (0, 0)
        self.win = win
        self._occupied = False
        self._occupied_by = None
        self._side_length = HEXAGON_SIDE_LENGTH
        self._color = BLUE if self._occupied else RED
        self.hex_points = None

        self.recalc_position_2d()

        self.image = pygame.Surface((2 * HEXAGON_SIDE_LENGTH, 2 * HEXAGON_SIDE_LENGTH), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.position_2d
        self.recalc_vertices()

        # Text label part
        self.font = pygame.font.SysFont('arial', 15)
        self.text = CoordinateHelper.from_cube_to_cube_str((x, y))
        self.position_text = self.font.render(self.text, True, TEXT_ON_HEXAGON_COLOR)
        self.offset = (self.position_text.get_width() / 2, self.position_text.get_height() / 2)

        self.draw()

    def draw(self):
        pygame.draw.polygon(self.image, BOARD_COLOR, self.hex_points)
        pygame.draw.polygon(self.image, HEXAGON_OUTLINE_COLOR, self.hex_points, width=1)

        self.win.blit(self.image, dest=tuple(pos - self._side_length for pos in self.position_2d))
        self.win.blit(self.position_text, dest=tuple(map(sub, self.position_2d, self.offset)))

    def draw_selected(self):
        pygame.draw.polygon(self.image, SELECTED_HEXAGON_COLOR, self.hex_points)
        self.win.blit(self.image, dest=tuple(pos - self._side_length for pos in self.position_2d))

    def occupy(self):
        self._occupied = True

    def unoccupy(self):
        self._occupied = False

    def recalc_position_2d(self):
        self.position_2d = CoordinateHelper.fromCubetoXY((self._x, self._y))

    def recalc_vertices(self):
        # points should be a list of tuples
        # [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6)]
        width, height = self.image.get_width(), self.image.get_height()
        left = width / 2
        top = height / 2
        points = []
        points.append((left, top + self._side_length))
        points.append((left + SIN60 * self._side_length, top + COS60 * self._side_length))
        points.append((left + SIN60 * self._side_length, top - COS60 * self._side_length))
        points.append((left, top - self._side_length))
        points.append((left - SIN60 * self._side_length, top - COS60 * self._side_length))
        points.append((left - SIN60 * self._side_length, top + COS60 * self._side_length))
        self.hex_points = points

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
