from typing import List, Tuple
from helper.coordinate_helper import CoordinateHelper
from enums.direction import DirectionEnum
from enums.move_type import MoveType


class Move:
    def __init__(self, move_type: MoveType, spots: List[Tuple[int, int]], direction: Tuple[int, int]) -> None:
        self.move_type = move_type
        self.spots = spots
        self.direction = direction

    def get_spots(self):
        return self.spots

    def get_direction(self):
        return self.direction

    def get_move_type(self):
        return self.move_type

    def __str__(self):
        _str_move_type = 'i' if self.move_type == MoveType.InLine else 's'
        first_spot_str = CoordinateHelper.from_2d_to_cube_str(self.spots[0])
        second_spot_str = CoordinateHelper.from_2d_to_cube_str(self.spots[-1])
        _str_direction = DirectionEnum.get_from_2d(self.direction).name

        if _str_move_type == 'i':
            return f"{_str_move_type}-{first_spot_str}-{_str_direction}"
        else:
            return f"{_str_move_type}-{first_spot_str}-{second_spot_str}-{_str_direction}"
