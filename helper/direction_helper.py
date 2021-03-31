from typing import Tuple
from constants import DIRECTION_VECTORS_2D


class DirectionHelper:
    @staticmethod
    def are_directions_on_the_same_axis(dir_a: Tuple[int, int], dir_b: Tuple[int, int]):
        return dir_a == dir_b or dir_a == DirectionHelper.get_opposite_direction(dir_b)

    @staticmethod
    def get_opposite_direction(direction_vector: Tuple[int, int]):
        return -direction_vector[0], -direction_vector[1]

    @staticmethod
    def get_perpendicular_directions(direction_vector: Tuple[int, int]):
        opposite_direction = DirectionHelper.get_opposite_direction(
            direction_vector)
        directions = DIRECTION_VECTORS_2D.copy()
        directions.remove(direction_vector)
        directions.remove(opposite_direction)
        return directions

    @staticmethod
    def get_left_directions(direction_vector: Tuple[int, int]):
        # Reference https://www.redblobgames.com/grids/hexagons/#rotation
        q = direction_vector[0]
        r = direction_vector[1]
        s = -q - r

        return [(-r, -s), (s, q)]
