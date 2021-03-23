from coordinate_helper import CoordinateHelper
from team_enum import TeamEnum


class Position:
    def __init__(self, team, position):
        self.team = team
        self.position = position

    def get_team(self):
        return self.team

    def get_position(self):
        return self.position

    def __str__(self):
        return f"\nTeam: {self.team}, Position: {self.position}\n"

    def __repr__(self):
        team_str = 'w' if self.team == TeamEnum.WHITE else 'b'
        position_str = CoordinateHelper.from_cube_to_cube_str(self.position)
        return position_str + team_str
