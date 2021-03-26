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
            (1, -1): DirectionEnum.NE,
            (1, 0): DirectionEnum.E,
            (0, 1): DirectionEnum.SE,
            (-1, 1): DirectionEnum.SW,
            (-1, 0): DirectionEnum.W,
            (0, -1): DirectionEnum.NW
        }
        return direction_mapper.get(vector)
