import enum


class MoveType(enum.Enum):
    InLine = enum.auto()
    SideStep = enum.auto()

    @staticmethod
    def get_from_str(move_type_str):
        if move_type_str == 'i':
            return MoveType.InLine
        elif move_type_str == 's':
            return MoveType.SideStep
        else:
            return None