from enum import Enum
from constants import WHITE_MARBLE_PATH, BLACK_MARBLE_PATH

class TeamEnum(Enum):
    WHITE = 1
    BLACK = 2
    BLUE  = 3

    @staticmethod
    def get_image_path(val):
        if val == TeamEnum.BLACK.value:
            return WHITE_MARBLE_PATH
        elif val == TeamEnum.WHITE.value:
            return BLACK_MARBLE_PATH
        else:
            raise ValueError('no such team')