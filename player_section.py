import pygame
from pygame_gui.elements import UISelectionList, UILabel
from pygame_gui.elements.ui_text_box import UITextBox

from constants import *


class PlayerSection:
    def __init__(self, manager, player):
        gap = 40
        pose_x = 10
        pose_y = 35
        self.manager = manager
        self.player = player
        self.time_hist_list = list()
        self.drop_move_hist_list = list()
        self.score_count = 0
        self.total_time_count = 0
        self.move_counts = 0
        self.score = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "Score:</i></b></font></body>", object_id="score",
            relative_rect=pygame.Rect((pose_x, pose_y), (-1, -1)), manager=self.manager, container=self.player
        )
        self.time_limit = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "Time Limit:</i></b></font></body>", object_id="time_limit",
            relative_rect=pygame.Rect((pose_x, pose_y + gap), (-1, -1)), manager=self.manager,
            container=self.player
        )
        self.time_hist = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "Time History:</i></b></font></body>", object_id="time_hist",
            relative_rect=pygame.Rect((pose_x, pose_y + 2 * gap), (-1, -1)), manager=self.manager,
            container=self.player
        )
        self.total_time = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "Total Time:</i></b></font></body>", object_id="total_time",
            relative_rect=pygame.Rect((pose_x, pose_y + 5 * gap), (-1, -1)), manager=self.manager,
            container=self.player
        )
        self.move_hist = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "Move History:</i></b></font></body>", object_id="move_hist",
            relative_rect=pygame.Rect((pose_x, pose_y + 6 * gap), (-1, -1)), manager=self.manager,
            container=self.player
        )
        label_len = 120
        self.score_info = UILabel(
            relative_rect=pygame.Rect((pose_x + 3 * gap // 1, pose_y), (label_len, 30)),
            text='0', manager=manager, container=player)
        self.time_limit_info = UILabel(
            relative_rect=pygame.Rect((pose_x + 3 * gap // 1, pose_y + gap), (label_len, 30)),
            text='0 secs', manager=self.manager, container=self.player)
        self.total_time_info = UILabel(
            relative_rect=pygame.Rect((pose_x + 3 * gap // 1, pose_y + 5 * gap), (label_len, 30)),
            text=f'0 secs', manager=self.manager, container=self.player)
        self.drop_down_time_hist = UISelectionList(pygame.Rect(pose_x, pose_y + 3 * gap, 120, 80),
                                                   item_list=self.time_hist_list,
                                                   manager=self.manager,
                                                   container=self.player,
                                                   allow_multi_select=True)

        self.drop_move_hist = UISelectionList(pygame.Rect(pose_x, pose_y + 7 * gap, 120, 80),
                                              item_list=self.drop_move_hist_list,
                                              manager=self.manager,
                                              container=self.player,
                                              allow_multi_select=True)

        self.total_move = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "Total Moves:</i></b></font></body>", object_id="time_limit",
            relative_rect=pygame.Rect((pose_x, pose_y + 9 *gap), (-1, -1)), manager=self.manager,
            container=self.player
        )
        self.total_move_info = UILabel(
            relative_rect=pygame.Rect((pose_x + 3 * gap // 1, pose_y + 9 *gap), (label_len, 30)),
            text=f'0 moves', manager=self.manager, container=self.player)

        self.your_turn = UILabel(relative_rect=pygame.Rect((pose_x + 2.5 * gap, pose_y - 0.8 * gap), (120, 30)),
                                 text='', manager=self.manager, container=self.player)
