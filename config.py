import pygame
from pygame_gui.elements import UIWindow, UIPanel, UIButton, UISelectionList, UITextEntryLine, UIDropDownMenu
from pygame_gui.elements.ui_text_box import UITextBox

from constants import *

class ConfigMenu(UIWindow):
    def __init__(self, rect, ui_manager, display, window):
        super().__init__(rect, ui_manager, window_display_title='Config',
                         object_id='#config_window',
                         resizable=True)
        self.run_display = True
        self.manager = ui_manager
        self.display = display
        self.window = window
        pose_x = 90
        pose_y = 70
        gap = 160

        self.INITIAL_BOARD_LAYOUT = UIPanel(relative_rect=pygame.Rect((pose_x, pose_y), (600, 100)),
                                            starting_layer_height=2, manager=self.manager,
                                            container=self)
        self.PLAYER_OPTIONS_LAYOUT = UIPanel(
            relative_rect=pygame.Rect((pose_x, pose_y + gap), (210, 110)),
            starting_layer_height=2, manager=self.manager, container=self)
        self.GAME_OPTIONS_LAYOUT = UIPanel(
            relative_rect=pygame.Rect((pose_x + 2.5 * gap // 1, pose_y + gap), (168, 125)),
            starting_layer_height=2, manager=self.manager, container=self)
        self.SELECTED_CONFIGURATIONS = UIPanel(
            relative_rect=pygame.Rect((pose_x, pose_y + 2 * gap), (600, 125)),
            starting_layer_height=2, manager=self.manager, container=self)
        # labels below here
        self.MAIN_TITLE = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=6><b>Abalone</b></font></body>",
            relative_rect=pygame.Rect((self.rect.width / 2 - 35, 40), (-1, -1)), manager=self.manager,
            layer_starting_height=2,
            object_id="mTitle", container=self)
        self.CONFIG_TITLE_PLAYER = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=3><b><i>Player "
                      "Configurations</i></b></font></body>", object_id="title",
            relative_rect=pygame.Rect((pose_x, 180), (-1, -1)), manager=self.manager, layer_starting_height=2,
            container=self)
        self.CONFIG_TITLE_GAME = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=3><b><i>Game "
                      "Configurations</i></b></font></body>", object_id="title",
            relative_rect=pygame.Rect((pose_x + 2.5 * gap, 180), (-1, -1)), manager=self.manager,
            layer_starting_height=2, container=self)
        self.CONFIG_TITLE_OPTIONS = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=3><b><i>Selected "
                      "Options</i></b></font></body>", object_id="title",
            relative_rect=pygame.Rect((pose_x, 360), (-1, -1)), manager=self.manager, layer_starting_height=2,
            container=self)
        self.TIME_LIMIT_PLAYER_LABEL = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "Time Limit per player:</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((10, 15), (-1, -1)), manager=self.manager, container=self.PLAYER_OPTIONS_LAYOUT
        )
        self.INITIAL_PLACEMENT_LABEL = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "Starting board layout:</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((10, 0), (-1, -1)), manager=self.manager, container=self.INITIAL_BOARD_LAYOUT
        )
        self.INITIAL_PLACEMENT_INPUT_LABEL = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "Selected layout:</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((8, 8), (-1, -1)), manager=self.manager, container=self.SELECTED_CONFIGURATIONS
        )
        self.WHITE_OPTIONS_LABEL = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "Whites Settings:</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((200, 8), (-1, -1)), manager=self.manager, container=self.SELECTED_CONFIGURATIONS
        )
        self.BLACK_OPTIONS_LABEL = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "Blacks Settings:</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((400, 8), (-1, -1)), manager=self.manager, container=self.SELECTED_CONFIGURATIONS
        )
        self.SELECTED_INITIAL = UIButton(
            relative_rect=pygame.Rect((8, 60), (120, 35)), manager=self.manager, container=self.SELECTED_CONFIGURATIONS,
            text=f'Standard'
        )
        self.WHITE_TIME_LABEL = UITextBox(
            relative_rect=pygame.Rect((200, 40), (-1, -1)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            html_text=f'Time:'
        )
        self.WHITE_TYPE_LABEL = UITextBox(
            relative_rect=pygame.Rect((200, 80), (-1, -1)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            html_text=f'Type:'
        )
        self.BLACK_TIME_LABEL = UITextBox(
            relative_rect=pygame.Rect((400, 40), (-1, -1)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            html_text=f'Time:'
        )
        self.BLACK_TYPE_LABEL = UITextBox(
            relative_rect=pygame.Rect((400, 80), (-1, -1)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            html_text=f'Type:'
        )
        self.WHITE_TIME_INPUT = UIButton(
            relative_rect=pygame.Rect((270, 40), (80, 35)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            text=f'5 secs'
        )
        self.WHITE_TYPE_INPUT = UIButton(
            relative_rect=pygame.Rect((270, 80), (80, 35)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            text=f'Human'
        )
        self.BLACK_TIME_INPUT = UIButton(
            relative_rect=pygame.Rect((470, 40), (80, 35)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            text=f'5 secs'
        )
        self.BLACK_TYPE_INPUT = UIButton(
            relative_rect=pygame.Rect((470, 80), (80, 35)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            text=f'Computer'
        )
        self.SELECTED_INITIAL.disable()
        self.WHITE_TIME_INPUT.disable()
        self.WHITE_TYPE_INPUT.disable()
        self.BLACK_TIME_INPUT.disable()
        self.BLACK_TYPE_INPUT.disable()
        self.MOVE_LIMIT_LABEL = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "Move limit per player:</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((10, 60), (-1, -1)), manager=self.manager, container=self.PLAYER_OPTIONS_LAYOUT
        )

        self.PLAYER1_LABEL_2 = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "White</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((5, 0), (-1, -1)), manager=self.manager, container=self.GAME_OPTIONS_LAYOUT
        )
        self.PLAYER2_LABEL_2 = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "Black</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((85, 0), (-1, -1)), manager=self.manager, container=self.GAME_OPTIONS_LAYOUT
        )
        # Buttons below here
        self.START_BUTTON = UIButton(
            relative_rect=pygame.Rect(((self.rect.width - gap) // 2, self.rect.height - gap), (100, 50)),
            text='Apply',
            manager=self.manager, container=self)
        self.STANDARD_BUTTON = UIButton(relative_rect=pygame.Rect((80, 35), (120, 50)),
                                        text='Standard', manager=self.manager,
                                        container=self.INITIAL_BOARD_LAYOUT)
        self.GER_DAISY_BUTTON = UIButton(relative_rect=pygame.Rect((250, 35), (120, 50)),
                                         text='German Daisy', manager=self.manager,
                                         container=self.INITIAL_BOARD_LAYOUT)
        self.BEL_DAISY_BUTTON = UIButton(relative_rect=pygame.Rect((430, 35), (120, 50)),
                                         text='Belgian Daisy', manager=self.manager,
                                         container=self.INITIAL_BOARD_LAYOUT)
        self.WHITE_HUMAN_BUTTON = UIButton(relative_rect=pygame.Rect((5, 40), (74, 30)),
                                           text='Human', manager=self.manager,
                                           container=self.GAME_OPTIONS_LAYOUT)
        self.BLACK_HUMAN_BUTTON = UIButton(relative_rect=pygame.Rect((84, 40), (74, 30)),
                                           text='Human', manager=self.manager,
                                           container=self.GAME_OPTIONS_LAYOUT)
        self.WHITE_COMPUTER_BUTTON = UIButton(relative_rect=pygame.Rect((5, 70), (74, 30)),
                                              text='Computer', manager=self.manager,
                                              container=self.GAME_OPTIONS_LAYOUT)
        self.BLACK_COMPUTER_BUTTON = UIButton(relative_rect=pygame.Rect((84, 70), (74, 30)),
                                              text='Computer', manager=self.manager,
                                              container=self.GAME_OPTIONS_LAYOUT)

        drop_down_h = 240
        gap = 40
        black_white_h = 260 - 2*gap
        time_list = list()
        move_list = list()
        for i in range(1, 11):
            time_list.append(f"{i * 5} secs")
            move_list.append(f"{i * 5} moves")

        self.PLAYER1_LABEL = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "White</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((330, black_white_h), (-1, -1)), manager=self.manager, container=self
        )
        self.PLAYER2_LABEL = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=1><b><i>"
                      "Black</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((330 + 70, black_white_h), (-1, -1)), manager=self.manager, container=self
        )
        current_time_string = '5 secs'
        self.time_drop_down_menu_white = UIDropDownMenu(time_list,
                                                        current_time_string,
                                                        pygame.Rect((300, drop_down_h), (90, 40)),
                                                        manager=self.manager,
                                                        container=self)
        self.time_drop_down_menu_black = UIDropDownMenu(time_list,
                                                        current_time_string,
                                                        pygame.Rect((380, drop_down_h), (90, 40)),
                                                        manager=self.manager,
                                                        container=self)
        current_move_string = '5 moves'
        self.move_drop_down_menu = UIDropDownMenu(move_list,
                                                        current_move_string,
                                                        pygame.Rect((320, drop_down_h + 1.3*gap), (130, 40)),
                                                        manager=self.manager,
                                                        container=self)


        self.WHITE_TIME_INPUT.rebuild_from_changed_theme_data()