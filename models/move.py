from operator import add, sub
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

    @staticmethod
    def get_from_move_string(move_str):
        move_info = move_str.split('-')
        move_type = MoveType.get_from_str(move_info[0])
        first_spot = CoordinateHelper.from_cube_str_to_2d(move_info[1])
        second_spot = CoordinateHelper.from_cube_str_to_2d(move_info[2])
        direction = DirectionEnum[move_info[3]]
        direction_2d = DirectionEnum.get_direction_vector_2d(direction)

        spots = list()
        spots.append(first_spot)

        distance = CoordinateHelper.get_manhattan_distance(first_spot, second_spot)
        if distance == 0:
            pass
        elif distance == 1:
            spots.append(second_spot)
        elif distance == 2:
            direction_from_first_to_second = tuple(map(lambda x, y: (x - y) / 2, second_spot, first_spot))
            middle_spot = tuple(map(add, first_spot, direction_from_first_to_second))
            spots.append(middle_spot)
            spots.append(second_spot)
        else:
            print("something went wrong at get_from_move_string")
            return None

        return Move(move_type=move_type, spots=spots, direction=direction_2d)

    def __str__(self):
        _str_move_type = 'i' if self.move_type == MoveType.InLine else 's'

        if isinstance(self.spots, Tuple):
            self.move_type = MoveType.InLine
            first_spot_str = CoordinateHelper.from_2d_to_cube_str(self.spots)
            second_spot_str = CoordinateHelper.from_2d_to_cube_str(self.spots)

        elif self.move_type == MoveType.SideStep:
            first_spot_str = CoordinateHelper.from_2d_to_cube_str(self.spots[0])
            second_spot_str = CoordinateHelper.from_2d_to_cube_str(self.spots[-1])
            spot_str_arr = sorted([first_spot_str, second_spot_str])
            first_spot_str = spot_str_arr[0]
            second_spot_str = spot_str_arr[1]

        else:
            first_spot_str = CoordinateHelper.from_2d_to_cube_str(self.spots[0])
            second_spot_str = CoordinateHelper.from_2d_to_cube_str(self.spots[-1])

        _str_direction = DirectionEnum.get_from_2d(self.direction).name

        return f"{_str_move_type}-{first_spot_str}-{second_spot_str}-{_str_direction}"
