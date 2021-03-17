import pygame

from constants import WHITE, BLACK, BOARD_SIZE, BLUE
from hexagon import Hexagon

class Board:
    def __init__(self):
        # 2D array
        self.hexagons = {}
        self.selected_pieces = None
        self.black_left = self.white_left = 14


    def draw_hexagons(self, win):
        win.fill(WHITE)
        center = (win.get_width() / 2, win.get_height() / 2)
        board_range = range(-BOARD_SIZE, BOARD_SIZE + 1)

        for x in board_range:
            for y in board_range:
                for z in board_range:
                    if (x + y + z == 0):
                        self.hexagons[(x, y)] = Hexagon(self, x, y, z)
                        hex_points = self.hexagons[(x, y)].get_vertices()
                        pygame.draw.polygon(win, WHITE, hex_points)
                        pygame.draw.polygon(win, BLUE, hex_points, width=3)
