from constants import DIRECTION_VECTORS_2D


class DirectionHelper:
    @staticmethod
    def get_opposite_direction(direction_vector: (int, int)):
        return direction_vector[1], direction_vector[0]

    @staticmethod
    def get_perpendicular_directions(direction_vector: (int, int)):
        opposite_direction = DirectionHelper.get_opposite_direction(direction_vector)
        directions = DIRECTION_VECTORS_2D.copy()
        directions.remove(direction_vector)
        directions.remove(opposite_direction)
        return directions

    @staticmethod
    def get_left_directions(direction_vector: (int, int)):
        # Reference https://www.redblobgames.com/grids/hexagons/#rotation
        q = direction_vector[0]
        r = direction_vector[1]
        s = -q - r

        return [(-r, -s), (s, q)]
