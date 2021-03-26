from direction import DirectionEnum
from move_type import MoveType


class Move:
    def __init__(self, move_type: MoveType, spots: [(int, int)], direction: (int, int)) -> None:
        self.move_type = move_type
        self.spots = spots
        self.direction = direction

    def get_spots(self):
        return self.spots

    def get_direction(self):
        return self.direction

    def get_move_type(self):
        return self.move_type
