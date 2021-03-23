import enum

DIRECTION_VECTORS = [(1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1)]


class DirectionEnum(enum.Enum):
    NE = 1
    E = 3
    SE = 5
    SW = 7
    W = 9
    NW = 11

    def get_direction_vector(self, direction_enum):
        dir = direction_enum.value()
        if dir == 1:
            return (1, -1)
        elif dir == 3:
            return (1, 0)
        elif dir == 5:
            return (0, 1)
        elif dir == 7:
            return (-1, 1)
        elif dir == 9:
            return (-1, 0)
        elif dir == 11:
            return (0, -1)
        else:
            return None
