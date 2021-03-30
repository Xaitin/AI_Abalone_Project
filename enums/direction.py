import enum

import pygame


class DirectionEnum(enum.Enum):
    NE = 1
    E = 3
    SE = 5
    SW = 7
    W = 9
    NW = 11

    @staticmethod
    def get_direction_vector(direction_enum):
        direction_vector_mapper = {
            DirectionEnum.NE: (1, -1),
            DirectionEnum.E: (1, 0),
            DirectionEnum.SE: (0, 1),
            DirectionEnum.SW: (-1, 1),
            DirectionEnum.W: (-1, 0),
            DirectionEnum.NW: (0, -1)
        }

        return direction_vector_mapper.get(direction_enum)

    @staticmethod
    def get_from_tuple(vector):
        direction_mapper = {
        }
        return direction_mapper.get(vector)

    @staticmethod
    def get_from_2d(vector_2d):
        direction_vector_2d_mapper = {
            (1, -1): DirectionEnum.SW,
            (-1, 1): DirectionEnum.NE,
            (1, 0): DirectionEnum.SE,
            (0, 1): DirectionEnum.E,
            (-1, 0): DirectionEnum.NW,
            (0, -1): DirectionEnum.W
        }
        return direction_vector_2d_mapper.get(vector_2d)

    @staticmethod
    def get_from_key(keyboard_input):
        key_direction_mapper = {
            pygame.K_u: DirectionEnum.NW,
            pygame.K_i: DirectionEnum.NE,
            pygame.K_h: DirectionEnum.W,
            pygame.K_k: DirectionEnum.E,
            pygame.K_n: DirectionEnum.SW,
            pygame.K_m: DirectionEnum.SE
        }
        return key_direction_mapper.get(keyboard_input)

    @staticmethod
    def is_direction_key(keyboard_input):
        return keyboard_input in [pygame.K_u, pygame.K_i, pygame.K_h, pygame.K_k, pygame.K_n, pygame.K_m]
