import pygame
from pygame import Union, Sprite, Sequence


class Player(pygame.sprite.Group):
    def __init__(self, player_number, *sprites: Union[Sprite, Sequence[Sprite]]):
        super().__init__(*sprites)
        self._player_number = player_number

