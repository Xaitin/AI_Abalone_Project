import enum

from coordinate_helper import CoordinateHelper

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
            (1, -1):DirectionEnum.SW,
            (-1, 1):DirectionEnum.NE,
            (1, 0): DirectionEnum.SE,
            (0, 1): DirectionEnum.E,
            (-1, 0): DirectionEnum.NW,
            (0, -1): DirectionEnum.W
        }
        return direction_vector_2d_mapper.get(vector_2d)
