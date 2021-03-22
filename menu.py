import pygame
import pygame_gui
from pygame_gui.elements import *
from board import Board
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
        pose_x = 130
        pose_y = 70
        gap = 160

        self.INITIAL_BOARD_LAYOUT = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((pose_x, pose_y), (600, 100)),
                                                                starting_layer_height=2, manager=self.manager,
                                                                container=self)
        self.PLAYER_OPTIONS_LAYOUT = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((pose_x, pose_y + gap), (345, 125)),
            starting_layer_height=2, manager=self.manager, container=self)
        self.GAME_OPTIONS_LAYOUT = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((pose_x + 2.5 * gap // 1, pose_y + gap), (168, 125)),
            starting_layer_height=2, manager=self.manager, container=self)
        self.SELECTED_CONFIGURATIONS = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect((pose_x, pose_y + 2 * gap), (600, 125)),
            starting_layer_height=2, manager=self.manager, container=self)
        # labels below here
        self.MAIN_TITLE = pygame_gui.elements.ui_text_box.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=6><b>Abalone</b></font></body>",
            relative_rect=pygame.Rect((self.rect.width / 2 - 35, 40), (-1, -1)), manager=self.manager,
            layer_starting_height=2,
            object_id="mTitle", container=self)
        self.CONFIG_TITLE_PLAYER = pygame_gui.elements.ui_text_box.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=3><b><i>Player "
                      "Configurations</i></b></font></body>", object_id="title",
            relative_rect=pygame.Rect((pose_x, 180), (-1, -1)), manager=self.manager, layer_starting_height=2,
            container=self)
        self.CONFIG_TITLE_GAME = pygame_gui.elements.ui_text_box.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=3><b><i>Game "
                      "Configurations</i></b></font></body>", object_id="title",
            relative_rect=pygame.Rect((pose_x + 2.5 * gap, 180), (-1, -1)), manager=self.manager,
            layer_starting_height=2, container=self)
        self.CONFIG_TITLE_OPTIONS = pygame_gui.elements.ui_text_box.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=3><b><i>Selected "
                      "Options</i></b></font></body>", object_id="title",
            relative_rect=pygame.Rect((pose_x, 360), (-1, -1)), manager=self.manager, layer_starting_height=2,
            container=self)
        self.TIME_LIMIT_PLAYER_LABEL = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "Time Limit per player:</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((10, 35), (-1, -1)), manager=self.manager, container=self.PLAYER_OPTIONS_LAYOUT
        )
        self.INITIAL_PLACEMENT_LABEL = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "Starting board layout:</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((10, 0), (-1, -1)), manager=self.manager, container=self.INITIAL_BOARD_LAYOUT
        )
        self.INITIAL_PLACEMENT_INPUT_LABEL = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "Selected layout:</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((8, 8), (-1, -1)), manager=self.manager, container=self.SELECTED_CONFIGURATIONS
        )
        self.WHITE_OPTIONS_LABEL = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "Whites Settings:</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((200, 8), (-1, -1)), manager=self.manager, container=self.SELECTED_CONFIGURATIONS
        )
        self.BLACK_OPTIONS_LABEL = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "Blacks Settings:</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((400, 8), (-1, -1)), manager=self.manager, container=self.SELECTED_CONFIGURATIONS
        )
        self.SELECTED_INITIAL = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((8, 60), (-1, -1)), manager=self.manager, container=self.SELECTED_CONFIGURATIONS,
            html_text='Standard'
        )
        self.WHITE_TIME_LABEL = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((200, 40), (-1, -1)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            html_text='Time:'
        )
        self.WHITE_TYPE_LABEL = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((200, 80), (-1, -1)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            html_text='Type:'
        )
        self.BLACK_TIME_LABEL = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((400, 40), (-1, -1)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            html_text='Time:'
        )
        self.BLACK_TYPE_LABEL = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((400, 80), (-1, -1)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            html_text='Type:'
        )
        self.WHITE_TIME_INPUT = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((270, 40), (-1, -1)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            html_text='10 mins'
        )
        self.WHITE_TYPE_INPUT = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((270, 80), (-1, -1)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            html_text='Human'
        )
        self.BLACK_TIME_INPUT = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((470, 40), (-1, -1)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            html_text='10 mins'
        )
        self.BLACK_TYPE_INPUT = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((470, 80), (-1, -1)), manager=self.manager,
            container=self.SELECTED_CONFIGURATIONS,
            html_text='Computer'
        )
        self.MOVE_LIMIT_LABEL = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "Move limit per player:</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((10, 80), (-1, -1)), manager=self.manager, container=self.PLAYER_OPTIONS_LAYOUT
        )
        self.PLAYER1_LABEL = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "White</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((215, 0), (-1, -1)), manager=self.manager, container=self.PLAYER_OPTIONS_LAYOUT
        )
        self.PLAYER2_LABEL = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "Black</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((275, 0), (-1, -1)), manager=self.manager, container=self.PLAYER_OPTIONS_LAYOUT
        )
        self.PLAYER1_LABEL_2 = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "White</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((5, 0), (-1, -1)), manager=self.manager, container=self.GAME_OPTIONS_LAYOUT
        )
        self.PLAYER2_LABEL_2 = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "Black</i></b></font></body>", object_id="label",
            relative_rect=pygame.Rect((85, 0), (-1, -1)), manager=self.manager, container=self.GAME_OPTIONS_LAYOUT
        )
        # Buttons below here
        self.START_BUTTON = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(((self.rect.width - gap) // 2, self.rect.height - gap), (100, 50)),
            text='Start',
            manager=self.manager, container=self)
        self.STANDARD_BUTTON = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((80, 35), (120, 50)),
                                                            text='Standard', manager=self.manager,
                                                            container=self.INITIAL_BOARD_LAYOUT)
        self.GER_DAISY_BUTTON = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 35), (120, 50)),
                                                             text='German Daisy', manager=self.manager,
                                                             container=self.INITIAL_BOARD_LAYOUT)
        self.BEL_DAISY_BUTTON = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((430, 35), (120, 50)),
                                                             text='Belgian Daisy', manager=self.manager,
                                                             container=self.INITIAL_BOARD_LAYOUT)
        self.WHITE_HUMAN_BUTTON = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 40), (74, 30)),
                                                               text='Human', manager=self.manager,
                                                               container=self.GAME_OPTIONS_LAYOUT)
        self.BLACK_HUMAN_BUTTON = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((84, 40), (74, 30)),
                                                               text='Human', manager=self.manager,
                                                               container=self.GAME_OPTIONS_LAYOUT)
        self.WHITE_COMPUTER_BUTTON = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((5, 70), (74, 30)),
                                                                  text='Computer', manager=self.manager,
                                                                  container=self.GAME_OPTIONS_LAYOUT)
        self.BLACK_COMPUTER_BUTTON = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((84, 70), (74, 30)),
                                                                  text='Computer', manager=self.manager,
                                                                  container=self.GAME_OPTIONS_LAYOUT)
        # Text input elements
        self.TIME_LIMIT_INPUT_P1 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((220, 38), (50, 50)),
                                                                       manager=self.manager,
                                                                       container=self.PLAYER_OPTIONS_LAYOUT)
        self.TIME_LIMIT_INPUT_P2 = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((280, 38), (50, 50)),
                                                                       manager=self.manager,
                                                                       container=self.PLAYER_OPTIONS_LAYOUT)
        self.MOVE_LIMIT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((220, 83), (50, 50)),
                                                                    manager=self.manager,
                                                                    container=self.PLAYER_OPTIONS_LAYOUT)


class GameMenu:

    def __init__(self):
        pygame.init()
        self.start_running, self.game_playing = True, True
        self._width, self._height = 1080, 700
        self.display = pygame.Surface((self._width, self._height))
        self.window = pygame.display.set_mode((self._width, self._height))
        self.manager = pygame_gui.UIManager((self._width, self._height))

        # board initialization
        self.board = Board(self.window)

        self.run_display = True
        self.display.fill(pygame.Color('#000000'))
        self.pose_y = 60
        self.config_menu = None
        self.white_human_click = False
        self.black_human_click = False
        self.open_config = False
        self.start_game = False
        self.button_w = 80
        self.button_h = 50
        self.adjust = 30
        self.font_size = 30
        self.draw_text("Abalone", self.font_size, (self._width // 2 + self.adjust * 1.5 // 1, self.pose_y + 30))
        self.draw_text("Next Move Suggested", self.font_size // 2,
                       (self._width // 2 + self.adjust * 2, self.pose_y + 80))
        self.draw_text("Next Move", self.font_size // 2, (self._width // 2 + self.adjust * 1.5 // 1, self.pose_y + 580))
        self.black_pose = [self._width // 2 - 500, self.pose_y * 3]
        self.white_pose = [self._width // 2 + 250, self.pose_y * 3]
        self.black_player = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(self.black_pose, (self._width // 5, self._height // 1.7)), starting_layer_height=2,
            manager=self.manager)
        self.white_player = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(self.white_pose, (self._width // 5, self._height // 1.7)), starting_layer_height=2,
            manager=self.manager)
        self.black_player_title = pygame_gui.elements.ui_text_box.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=3><b><i>Black Player</i></b></font></body>",
            object_id="title",
            relative_rect=pygame.Rect(self.black_pose, (-1, -1)), manager=self.manager, layer_starting_height=2)
        self.white_player_title = pygame_gui.elements.ui_text_box.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=3><b><i>White Player</i></b></font></body>",
            object_id="title",
            relative_rect=pygame.Rect(self.white_pose, (-1, -1)), manager=self.manager, layer_starting_height=2)
        self.player_info(self.black_player)
        self.player_info(self.white_player)
        self.config_button = self.button(self._width // 2 - 350, self.pose_y, self.button_w, self.button_h, "config",
                                         self.manager)
        self.start_button = self.button(self._width // 2 - 250, self.pose_y, self.button_w, self.button_h, "start",
                                        self.manager)
        self.stop_button = self.button(self._width // 2 - 150, self.pose_y, self.button_w, self.button_h, "stop",
                                       self.manager)
        self.pause_button = self.button(self._width // 2 + 150, self.pose_y, self.button_w, self.button_h, "pause",
                                        self.manager)
        self.undo_button = self.button(self._width // 2 + 250, self.pose_y, self.button_w, self.button_h, "undo",
                                       self.manager)
        self.reset_button = self.button(self._width // 2 + 350, self.pose_y, self.button_w, self.button_h, "reset",
                                        self.manager)
        UITextEntryLine(pygame.Rect((self._width // 2, self.pose_y + 100), (100, -1)), self.manager,
                        object_id='#suggested_move')
        UITextEntryLine(pygame.Rect((self._width // 2, self.pose_y + 600), (100, -1)), self.manager,
                        object_id='#next_move')

    @staticmethod
    def button(x, y, w, h, text, manager):
        return pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y), (w, h)), text=text, manager=manager)

    def draw_text(self, text, size, pose):
        font = pygame.font.SysFont('comicsansms', size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (pose[0], pose[1])
        self.display.blit(text_surface, text_rect)

    def player_info(self, container):
        gap = 40
        pose_x = 10
        pose_y = 35
        self.score = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "Score:</i></b></font></body>", object_id="score",
            relative_rect=pygame.Rect((pose_x, pose_y), (-1, -1)), manager=self.manager, container=container
        )
        self.time_limit = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "Time Limit:</i></b></font></body>", object_id="time_limit",
            relative_rect=pygame.Rect((pose_x, pose_y + gap), (-1, -1)), manager=self.manager, container=container
        )
        self.time_hist = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "Time History:</i></b></font></body>", object_id="time_hist",
            relative_rect=pygame.Rect((pose_x, pose_y + 2 * gap), (-1, -1)), manager=self.manager, container=container
        )
        self.total_time = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "Total Time:</i></b></font></body>", object_id="total_time",
            relative_rect=pygame.Rect((pose_x, pose_y + 5 * gap), (-1, -1)), manager=self.manager, container=container
        )
        self.move_hist = pygame_gui.elements.UITextBox(
            html_text="<body bgcolor='#000000'><font face='verdana' color='#FFFFFF' size=1><b><i>"
                      "Move History:</i></b></font></body>", object_id="move_hist",
            relative_rect=pygame.Rect((pose_x, pose_y + 6 * gap), (-1, -1)), manager=self.manager, container=container
        )

        self.score_info = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((pose_x + 3*gap//1, pose_y), (70, 30)),
                                                        text='0', manager=self.manager, container=container)
        self.score_info.disable()
        self.time_limit_info = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((pose_x + 3*gap//1, pose_y + gap), (70, 30)),
                                                        text='0 secs', manager=self.manager, container=container)
        self.time_limit_info.disable()
        self.total_time_info = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((pose_x + 3*gap//1, pose_y + 5 * gap), (70, 30)),
                                                        text='0 secs', manager=self.manager, container=container)
        self.total_time_info.disable()
        self.drop_down_time_hist = UISelectionList(pygame.Rect(pose_x, pose_y + 3 * gap, 120, 80),
                        item_list=['1. 5 secs',
                                   '2. 5 secs',
                                   '3. 5 secs',
                                   '4. 5 secs',
                                   '5. 5 secs',
                                   ],
                        manager=self.manager,
                        container=container,
                        allow_multi_select=True)

        self.drop_move_hist = UISelectionList(pygame.Rect(pose_x, pose_y + 7 * gap, 120, 80),
                        item_list=['1. F5',
                                   '2. A3',
                                   '3. G4',
                                   '4. C1',
                                   ],
                        manager=self.manager,
                        container=container,
                        allow_multi_select=True)

    def check_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_playing = False

            # Mouse Handling
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.board.on_click(event.pos)

            # Keyboard handling
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.board.reset_selected_marbles()


            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#suggested_move':
                    print(event.text)
                elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#next_move':
                    print(event.text)

                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.config_button:
                        self.open_config = True
                        self.config_menu = ConfigMenu(pygame.Rect((10, 10), (800, 700)), self.manager, self.display,
                                                      self.window)
                        print('Config!')
                    if event.ui_element == self.start_button:
                        self.open_config = False
                        self.start_game = True
                        print('Start!')
                    if event.ui_element == self.stop_button:
                        self.start_game = False
                        print('Start!')
                    if event.ui_element == self.pause_button:
                        print('Pause!')
                    if event.ui_element == self.pause_button:
                        print('Pause!')
                    if event.ui_element == self.undo_button:
                        print('Undo!')
                    if event.ui_element == self.reset_button:
                        print('Reset!')

                    if self.config_menu != None:
                        if event.ui_element == self.config_menu.START_BUTTON:
                            self.config_menu.WHITE_TYPE_INPUT.html_text = 'Start'
                            print('Start')
                            # move_limit = int(self.MOVE_LIMIT_INPUT.get_text())
                            # Configure sending start data to gameBoard here
                        if event.ui_element == self.config_menu.WHITE_HUMAN_BUTTON:
                            self.config_menu.WHITE_TYPE_INPUT.html_text = 'Human'
                            self.white_human_click = True
                            self.click_func(self.white_human_click, self.config_menu.WHITE_HUMAN_BUTTON, self.config_menu.WHITE_COMPUTER_BUTTON)
                            print('Human')
                        elif event.ui_element == self.config_menu.WHITE_COMPUTER_BUTTON:
                            self.config_menu.WHITE_TYPE_INPUT.html_text = 'Computer'
                            self.white_human_click = False
                            self.click_func(self.white_human_click, self.config_menu.WHITE_COMPUTER_BUTTON, self.config_menu.WHITE_HUMAN_BUTTON)

                            print('Computer')
                        elif event.ui_element == self.config_menu.BLACK_HUMAN_BUTTON:
                            self.config_menu.BLACK_TYPE_INPUT.html_text = 'Human'
                            self.black_human_click = True
                            self.click_func(self.black_human_click, self.config_menu.BLACK_HUMAN_BUTTON, self.config_menu.BLACK_COMPUTER_BUTTON)

                            print('Human')
                        elif event.ui_element == self.config_menu.BLACK_COMPUTER_BUTTON:
                            self.config_menu.BLACK_TYPE_INPUT.html_text = 'Computer'
                            self.black_human_click = False
                            self.click_func(self.black_human_click, self.config_menu.BLACK_COMPUTER_BUTTON, self.config_menu.BLACK_HUMAN_BUTTON)

                            print('Computer')
                        elif event.ui_element == self.config_menu.STANDARD_BUTTON:
                            self.config_menu.SELECTED_INITIAL.html_text = 'Standard'
                            print('Standard')
                        elif event.ui_element == self.config_menu.GER_DAISY_BUTTON:
                            self.config_menu.SELECTED_INITIAL.html_text = 'German Daisy'
                            print('German Daisy')
                        elif event.ui_element == self.config_menu.BEL_DAISY_BUTTON:
                            self.config_menu.SELECTED_INITIAL.html_text = 'Belgian Daisy'
                            print('Belgian Daisy')
                    if event.user_type == pygame_gui.UI_TEXT_ENTRY_CHANGED:
                        if event.ui_element == self.config_menu.TIME_LIMIT_INPUT_P1:
                            pass
                            # take p1 input
                        elif event.ui_element == self.config_menu.TIME_LIMIT_INPUT_P2:
                            pass
                            # take p2 input
                        elif event.ui_element == self.config_menu.MOVE_LIMIT_INPUT:
                            pass
            self.manager.process_events(event)

    @staticmethod
    def click_func(check_click, button1, button2):
        if check_click:
            button1.disable()
            button2.enable()
        else:
            button2.enable()
            button1.disable()


    def display_menu(self):
        self.manager.root_container.show()
        game_board_img = pygame.image.load('drawables/game_board.png').convert_alpha()
        game_board_img = pygame.transform.scale(game_board_img, (BOARD_IMAGE_SIZE, BOARD_IMAGE_SIZE))

        clock = pygame.time.Clock()
        while self.game_playing:
            time_delta = clock.tick(30) / 1000.0
            self.check_event()
            self.manager.update(time_delta)
            self.window.blit(self.display, (0, 0))
            self.manager.draw_ui(self.window)
            if not self.open_config and self.start_game:
                self.board.update()
            pygame.display.update()

        pygame.quit()


def main():
    game = GameMenu()
    game.display_menu()


# execute here!
if __name__ == '__main__':
    main()
