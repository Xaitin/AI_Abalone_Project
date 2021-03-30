from _operator import add

import pygame
from pygame.sprite import AbstractGroup, Sprite

from constants import MARBLE_SIZE, RED
from enums.direction import DirectionEnum
from helper.coordinate_helper import CoordinateHelper
from enums.team_enum import TeamEnum


class Marble(Sprite):
    def __init__(self, position_2d, team, *groups: AbstractGroup):
        super().__init__(*groups)
        self.image = self.get_team_marble_img(team)
        self.team = team
        self.position_2d = tuple(position_2d)
        self.position_cube = CoordinateHelper.from2DArraytoCube(position_2d)
        self.xy_pos = None
        self.xy_center = None
        self.rect = None
        self.recalc_position()

    def draw(self, window):
        window.blit(self.image, dest=self.xy_pos)

    def move_by_position_cube(self, new_position_cube):
        print(
            f"Moving Marble from {self.position_cube} to {new_position_cube}")
        self.position_2d = CoordinateHelper.fromCubeto2DArray(
            new_position_cube)
        self.recalc_position()

    def move_by_direction(self, direction: DirectionEnum):
        prev_position_cube = tuple(self.position_cube)
        new_position_2d = tuple(
            map(add, self.position_2d, DirectionEnum.get_direction_vector_2d(direction)))
        self.move_position_2d(new_position_2d)
        self.recalc_position()

        print(
            f"Moving Marble from {prev_position_cube} to {self.position_cube}")

    def get_team_marble_img(self, team):
        marble_img_path = TeamEnum.get_image_path(team)
        img = pygame.image.load(marble_img_path).convert_alpha()
        image_scaled = pygame.transform.scale(img, (MARBLE_SIZE, MARBLE_SIZE))
        return image_scaled

    def draw_selection_circle(self, win):
        # pygame.Rect(self.xy_pos, (MARBLE_SIZE, MARBLE_SIZE))
        pygame.draw.circle(win, color=RED, center=self.xy_center,
                           radius=MARBLE_SIZE/2, width=2)

    def recalc_position(self):
        self.xy_pos = [val - MARBLE_SIZE /
                       2 for val in CoordinateHelper.from2DArraytoXY(position_2d=self.position_2d)]
        self.xy_center = [val for val in CoordinateHelper.from2DArraytoXY(
            position_2d=self.position_2d)]
        self.rect = pygame.Rect(
            self.xy_pos[0], self.xy_pos[1], MARBLE_SIZE, MARBLE_SIZE)

    def move_position_2d(self, new_position_2d):
        self.position_2d = new_position_2d
        self.position_cube = CoordinateHelper.from2DArraytoCube(
            new_position_2d)
        self.recalc_position()

    def get_position_cube(self):
        return self.position_cube

    def __str__(self) -> str:
        team_str = "b" if self.team == TeamEnum.BLACK.value else "w"
        return f"{CoordinateHelper.from_2d_to_cube_str(self.position_2d)}{team_str}"
