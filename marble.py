import pygame
from pygame.sprite import AbstractGroup

from constants import MARBLE_SIZE
from coordinate_helper import CoordinateHelper
from team_enum import TeamEnum


class Marble(pygame.sprite.Sprite):
    def __init__(self, position_2d, team, *groups: AbstractGroup):
        super().__init__(*groups)
        xy_pos = [val - MARBLE_SIZE/2  for val in CoordinateHelper.from2DArraytoXY(position_2d=position_2d)]
        marble_img_path = TeamEnum.get_image_path(team)
        img = pygame.image.load(marble_img_path)
        image_scaled = pygame.transform.scale(img, (MARBLE_SIZE, MARBLE_SIZE))

        self.image = image_scaled
        self.rect = pygame.Rect(xy_pos[0], xy_pos[1], MARBLE_SIZE, MARBLE_SIZE)
