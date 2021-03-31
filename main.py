from game_playing_agent import GamePlayingAgent
import re

import pygame
import pygame_gui
from pygame_gui.elements import UIPanel, UIButton, UITextEntryLine
from pygame_gui.elements.ui_text_box import UITextBox

from config import ConfigMenu
from player_section import PlayerSection
from constants import *
from enums.team_enum import TeamEnum
from enums.direction import DirectionEnum
from enums.team_enum import TeamEnum
from models.board import Board
from player_section import PlayerSection

class GameMenu:

    def __init__(self):
        pygame.init()
        self.start_running, self.game_playing = True, True
        self.display = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.manager = pygame_gui.UIManager((WINDOW_WIDTH, WINDOW_HEIGHT))

        # board initialization
        self.board = Board(self.window)
        self.initial_board = 0

        # agent initialization
        # self.agent = GamePlayingAgent()
        
        self.run_display = True
        self.display.fill(BLACK)
        self.config_menu = None
        self.white_human_click = False
        self.black_human_click = False
        self.open_config = False
        self.start_game = False
        self.button_w = 80
        self.button_h = 50
        self.adjust = 30
        self.font_size = 30
        self.board_setup = dict()
        self.setting_result = dict()
        self.board_setup["Standard"] = 0
        self.board_setup["German Daisy"] = 1
        self.board_setup["Belgian Daisy"] = 2
        self.setting_result["selected_layout"] = "Standard"
        self.setting_result["white_type"] = "Human"
        self.setting_result["black_type"] = "Computer"
        self.setting_result["moves"] = 10
        self.player_each_time = [5, 5]
        # Texts
        self.draw_text("Abalone", self.font_size, (WINDOW_WIDTH // 2, TITLE_DISTANCE_TOP + self.button_h // 2))

        # Buttons on the top
        self.config_button = self.button(WINDOW_WIDTH // 2 - BUTTON_DISTANCE_3 - self.button_w, TITLE_DISTANCE_TOP,
                                         self.button_w, self.button_h, "config",
                                         self.manager)
        self.start_button = self.button(WINDOW_WIDTH // 2 - BUTTON_DISTANCE_2 - self.button_w, TITLE_DISTANCE_TOP,
                                        self.button_w, self.button_h, "start",
                                        self.manager)
        self.stop_button = self.button(WINDOW_WIDTH // 2 - BUTTON_DISTANCE_1 - self.button_w, TITLE_DISTANCE_TOP,
                                       self.button_w, self.button_h, "stop",
                                       self.manager)
        self.pause_button = self.button(WINDOW_WIDTH // 2 + BUTTON_DISTANCE_1, TITLE_DISTANCE_TOP, self.button_w,
                                        self.button_h, "pause",
                                        self.manager)
        self.undo_button = self.button(WINDOW_WIDTH // 2 + BUTTON_DISTANCE_2, TITLE_DISTANCE_TOP, self.button_w,
                                       self.button_h,
                                       "undo",
                                       self.manager)
        self.reset_button = self.button(WINDOW_WIDTH // 2 + BUTTON_DISTANCE_3, TITLE_DISTANCE_TOP, self.button_w,
                                        self.button_h, "reset",
                                        self.manager)

        temp = 60
        button_w_dir = self.button_w // 2
        button_h_dir = self.button_h // 1.4
        index = 2.8
        sub_h = WINDOW_HEIGHT - 100
        shift_w = 5

        self.NW_button = self.button(WINDOW_WIDTH // index + temp * 3 - self.button_w + shift_w, sub_h - 0.6 * temp,
                                     button_w_dir, button_h_dir, "NW",
                                     self.manager)
        self.NE_button = self.button(WINDOW_WIDTH // index + temp * 4 - self.button_w + shift_w, sub_h - 0.6 * temp,
                                     button_w_dir, button_h_dir, "NE",
                                     self.manager)
        self.W_button = self.button(WINDOW_WIDTH // index + temp * 2.5 - self.button_w + shift_w, sub_h,
                                    button_w_dir, button_h_dir, "W",
                                    self.manager)
        self.E_button = self.button(WINDOW_WIDTH // index + temp * 4.5 - self.button_w + shift_w, sub_h,
                                    button_w_dir, button_h_dir, "E",
                                    self.manager)
        self.SW_button = self.button(WINDOW_WIDTH // index + temp * 3 - self.button_w + shift_w, sub_h + 0.6 * temp,
                                     button_w_dir, button_h_dir, "SW",
                                     self.manager)
        self.SE_button = self.button(WINDOW_WIDTH // index + temp * 4 - self.button_w + shift_w, sub_h + 0.6 * temp,
                                     button_w_dir, button_h_dir, "SE",
                                     self.manager)

        # Just an additional accessor for direction buttons
        self.direction_buttons = [self.NW_button, self.NE_button, self.W_button, self.E_button, self.SW_button,
                                  self.SE_button]

        # region Player Panels Initialization
        self.black_panel_position = [
            WINDOW_WIDTH // 2 - PANEL_DISTANCE_FROM_CENTER, TITLE_DISTANCE_TOP * 2 + self.button_h
        ]
        self.white_panel_position = [
            WINDOW_WIDTH // 2 + PANEL_DISTANCE_FROM_CENTER - PANEL_WIDTH, TITLE_DISTANCE_TOP * 2 + self.button_h
        ]

        self.suggested_entry = UITextEntryLine(
            pygame.Rect((WINDOW_WIDTH // 2 - 5.7 * shift_w, TITLE_DISTANCE_TOP + temp), (80, -1)), self.manager)

        self.draw_text("Suggested move", self.font_size//2, (WINDOW_WIDTH // 2 - 1.7*temp, TITLE_DISTANCE_TOP + 1.2*temp))

        self.black_player_panel = UIPanel(
            relative_rect=pygame.Rect(self.black_panel_position, (PANEL_WIDTH, PANEL_HEIGHT)),
            starting_layer_height=2,
            manager=self.manager
        )
        self.white_player_panel = UIPanel(
            relative_rect=pygame.Rect(self.white_panel_position, (PANEL_WIDTH, PANEL_HEIGHT)),
            starting_layer_height=2,
            manager=self.manager
        )

        self.black_player_title = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=3><b><i>Black Player</i></b></font></body>",
            object_id="title",
            relative_rect=pygame.Rect(self.black_panel_position, (-1, -1)), manager=self.manager,
            layer_starting_height=2)

        self.white_player_title = UITextBox(
            html_text=f"<body bgcolor={UI_TEXT_BG_COLOR}><font face='verdana' color={UI_TEXT_COLOR} size=3><b><i>White Player</i></b></font></body>",
            object_id="title",
            relative_rect=pygame.Rect(self.white_panel_position, (-1, -1)), manager=self.manager,
            layer_starting_height=2)

        self.black_player = PlayerSection(self.manager, self.black_player_panel)
        self.white_player = PlayerSection(self.manager, self.white_player_panel)
        # endregion Initialization
    @staticmethod
    def button(x, y, w, h, text, manager):
        return UIButton(relative_rect=pygame.Rect((x, y), (w, h)), text=text, manager=manager)

    def draw_text(self, text, size, pose):
        font = pygame.font.SysFont('comicsansms', size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (pose[0], pose[1])
        self.display.blit(text_surface, text_rect)

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
                if DirectionEnum.is_direction_key(event.key):
                    self.on_direction_key_pushed(event.key)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#suggested_move':
                    print(event.text)
                elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#next_move':
                    print(event.text)

                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.config_button:
                        self.open_config = True
                        self.config_menu = ConfigMenu(pygame.Rect((150, 5), (800, 700)), self.manager, self.display,
                                                      self.window)
                        print('Config!')
                    if event.ui_element == self.start_button:
                        self.open_config = False
                        self.resetting_board_player_panel()
                        self.start_game = True
                        print('Start!')
                    if event.ui_element == self.stop_button:
                        self.start_game = False
                        print('Stop!')
                    if event.ui_element == self.pause_button:
                        print('Pause!')
                    if event.ui_element == self.undo_button:
                        print('Undo!')
                    if event.ui_element == self.reset_button:
                        self.resetting_board_player_panel()
                        self.start_game = False

                    if event.ui_element in self.direction_buttons:
                        self.on_direction_button_click(event.ui_element)

                    if self.config_menu != None:
                        if event.ui_element == self.config_menu.START_BUTTON:
                            self.config_menu.WHITE_TYPE_INPUT.html_text = 'Start'
                            self.setting_result[
                                "white_time"] = self.config_menu.time_drop_down_menu_white.selected_option
                            self.setting_result[
                                "black_time"] = self.config_menu.time_drop_down_menu_black.selected_option
                            self.setting_result["moves"] = self.config_menu.move_drop_down_menu.selected_option
                            self.setting_result_func(self.config_menu)
                            self.resetting_board_player_panel()
                            self.start_game = False
                            # move_limit = int(self.MOVE_LIMIT_INPUT.get_text())
                            # Configure sending start data to gameBoard here
                        if event.ui_element == self.config_menu.WHITE_HUMAN_BUTTON:
                            self.config_menu.WHITE_TYPE_INPUT.html_text = 'Human'
                            self.white_human_click = True
                            self.setting_result["white_type"] = 'Human'
                            self.click_func(self.white_human_click, self.config_menu.WHITE_HUMAN_BUTTON,
                                            self.config_menu.WHITE_COMPUTER_BUTTON)
                            print('Human')
                        elif event.ui_element == self.config_menu.WHITE_COMPUTER_BUTTON:
                            self.config_menu.WHITE_TYPE_INPUT.html_text = 'Computer'
                            self.white_human_click = False
                            self.setting_result["white_type"] = 'Computer'
                            self.click_func(self.white_human_click, self.config_menu.WHITE_COMPUTER_BUTTON,
                                            self.config_menu.WHITE_HUMAN_BUTTON)

                            print('Computer')
                        elif event.ui_element == self.config_menu.BLACK_HUMAN_BUTTON:
                            self.config_menu.BLACK_TYPE_INPUT.html_text = 'Human'
                            self.setting_result["black_type"] = 'Human'
                            self.black_human_click = True
                            self.click_func(self.black_human_click, self.config_menu.BLACK_HUMAN_BUTTON,
                                            self.config_menu.BLACK_COMPUTER_BUTTON)

                            print('Human')
                        elif event.ui_element == self.config_menu.BLACK_COMPUTER_BUTTON:
                            self.config_menu.BLACK_TYPE_INPUT.html_text = 'Computer'
                            self.setting_result["black_type"] = 'Computer'
                            self.black_human_click = False
                            self.click_func(self.black_human_click, self.config_menu.BLACK_COMPUTER_BUTTON,
                                            self.config_menu.BLACK_HUMAN_BUTTON)

                            print('Computer')
                        elif event.ui_element == self.config_menu.STANDARD_BUTTON:
                            self.config_menu.SELECTED_INITIAL.html_text = 'Standard'
                            self.setting_result["selected_layout"] = "Standard"
                            self.initial_board = 0
                            self.third_click_func(self.initial_board, self.config_menu.STANDARD_BUTTON,
                                                  self.config_menu.GER_DAISY_BUTTON, self.config_menu.BEL_DAISY_BUTTON)
                            print('Standard')
                        elif event.ui_element == self.config_menu.GER_DAISY_BUTTON:
                            self.config_menu.SELECTED_INITIAL.html_text = 'German Daisy'
                            self.setting_result["selected_layout"] = "German Daisy"
                            self.initial_board = 1
                            self.third_click_func(self.initial_board, self.config_menu.STANDARD_BUTTON,
                                                  self.config_menu.GER_DAISY_BUTTON, self.config_menu.BEL_DAISY_BUTTON)
                            print('German Daisy')
                        elif event.ui_element == self.config_menu.BEL_DAISY_BUTTON:
                            self.config_menu.SELECTED_INITIAL.html_text = 'Belgian Daisy'
                            self.setting_result["selected_layout"] = "Belgian Daisy"
                            self.initial_board = 2
                            self.third_click_func(self.initial_board, self.config_menu.STANDARD_BUTTON,
                                                  self.config_menu.GER_DAISY_BUTTON, self.config_menu.BEL_DAISY_BUTTON)
                            print('Belgian Daisy')


            self.manager.process_events(event)

    def on_direction_button_click(self, ui_element: UIButton):
        if not self.board.is_marble_selected():
            print("Warning: Select marbles, first")
            return
        direction_str = ui_element.text
        direction = DirectionEnum[direction_str]
        move = self.board.generate_move(direction)
        print(move)
        is_valid_move = self.board.validate_move(move)
        # if is_agent
        if is_valid_move:
            if self.is_agent_computer():
                self.move = self.board.apply_move(move)
                self.board.reset_selected_marbles()
                self.board.switch_player()
                self.board.update_state_space()
                # self.switch_player()
                self.switch_player()
            else:
                self.move = self.board.apply_move(move)
                self.switch_player()
        else: 
            print("Invalid move detected!")

    def on_direction_key_pushed(self, key):
        if not self.board.is_marble_selected():
            print("Warning: Select marbles, first")
            return
        direction = DirectionEnum.get_from_key(key)
        move = self.board.generate_move(direction)
        print(move)
        is_valid_move = self.board.validate_move(move)
        if is_valid_move:
            self.board.apply_move(move)
            self.switch_player()
        else: 
            print("Invalid move detected!")

    @staticmethod
    def click_func(check_click, button1, button2):
        if check_click:
            button1.disable()
            button2.enable()
        else:
            button2.enable()
            button1.disable()

    @staticmethod
    def third_click_func(click_index, button1, button2, button3):
        if click_index == 0:
            button1.disable()
            button2.enable()
            button3.enable()
        elif click_index == 1:
            button1.enable()
            button2.disable()
            button3.enable()
        else:
            button1.enable()
            button2.enable()
            button3.disable()

    def setting_result_func(self, config):
        config.SELECTED_INITIAL.enable()
        config.WHITE_TIME_INPUT.enable()
        config.WHITE_TYPE_INPUT.enable()
        config.BLACK_TIME_INPUT.enable()
        config.BLACK_TYPE_INPUT.enable()
        self.board = Board(self.window, self.board_setup[self.setting_result["selected_layout"]])
        self.player_each_time = [int(re.search(r'\d+', self.setting_result["black_time"]).group()), int(re.search(r'\d+', self.setting_result["white_time"]).group())]
        self.player_each_move = int(re.search(r'\d+', self.setting_result["moves"]).group())

        config.SELECTED_INITIAL.set_text(self.setting_result["selected_layout"])
        config.WHITE_TIME_INPUT.set_text(self.setting_result["white_time"])
        config.WHITE_TYPE_INPUT.set_text(self.setting_result["white_type"])
        config.BLACK_TIME_INPUT.set_text(self.setting_result["black_time"])
        config.BLACK_TYPE_INPUT.set_text(self.setting_result["black_type"])

    def resetting_board_player_panel(self):
        self.start_count = True
        self.black_player.drop_down_time_hist.kill()
        self.white_player.drop_down_time_hist.kill()
        self.black_player.drop_move_hist.kill()
        self.white_player.drop_move_hist.kill()
        self.black_player = PlayerSection(self.manager, self.black_player_panel)
        self.white_player = PlayerSection(self.manager, self.white_player_panel)
        self.board = Board(self.window, self.board_setup[self.setting_result["selected_layout"]])

    def display_menu(self):
        self.manager.root_container.show()
        game_board_img = pygame.image.load('drawables/game_board.png').convert_alpha()
        # game_board_img = pygame.transform.scale(game_board_img, (BOARD_IMAGE_SIZE, BOARD_IMAGE_SIZE))

        clock = pygame.time.Clock()
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, 1000)
        self.time_count = 0
        self.start_count = True
        self.current_time = 0
        self.player_turn = TeamEnum.BLACK
        self.each_time_count = 0
        while self.game_playing:
            time_delta = clock.tick(30) / 1000.0
            self.time_count += time_delta
            self.check_event()
            self.manager.update(time_delta)
            self.window.blit(self.display, (0, 0))
            self.manager.draw_ui(self.window)
            start = 1
            if not self.open_config and self.start_game:
                if self.is_agent_computer():
                    if start == 1:
                        start += 1
                        self.player_turn = TeamEnum.WHITE
                        # self.board.reset_selected_marbles()
                        self.board.switch_player()
                        self.board.update_state_space()

                if self.start_count:
                    self.current_time = self.time_count
                    self.start_count = False
                self.add_timer()
                self.board.update()
            pygame.display.update()

        pygame.quit()

    def add_timer(self):
        start_zero = self.time_count - self.current_time
        self.each_time_count = start_zero
        time_in_secs = self.player_each_time[0] - start_zero
        if self.player_turn == TeamEnum.BLACK:
            self.black_player.time_limit_info.set_text(f"{time_in_secs:.1f} secs" if time_in_secs>=0 else f"{time_in_secs:.1f} secs!")
        else:
            self.white_player.time_limit_info.set_text(f"{time_in_secs:.1f} secs" if time_in_secs>=0 else f"{time_in_secs:.1f} secs!")

    def is_agent_computer(self):
        return self.setting_result["white_type"] == "Human" and self.setting_result["black_type"] == "Computer"

    def switch_player(self):
        score = 14
        # Use this to get the board state
        self.board.__str__()
        if self.player_turn == TeamEnum.BLACK:
            if self.is_agent_computer():
                self.player_turn = TeamEnum.WHITE
                self.start_count = True
            else:
                self.black_player.time_hist_list.append(f"{self.each_time_count:.1f} secs")
                self.black_player.total_time_count += self.each_time_count
                self.black_player.total_time_info.set_text(f"{self.black_player.total_time_count:.1f} secs")
                self.black_player.drop_down_time_hist.set_item_list(self.black_player.time_hist_list)
                self.black_player.your_turn.set_text("")
                self.black_player.score_count = score - len(self.board.white_marble_list)
                self.black_player.score_info.set_text(f"{self.black_player.score_count}")
                self.black_player.drop_move_hist_list.append(f"{self.move}")
                self.black_player.drop_move_hist.set_item_list(self.black_player.drop_move_hist_list)
                self.white_player.your_turn.set_text("Your Turn!")
                self.player_turn = TeamEnum.WHITE
                self.start_count = True
        else:
            self.white_player.time_hist_list.append(f"{self.each_time_count:.1f} secs")
            self.white_player.total_time_count += self.each_time_count
            self.white_player.total_time_info.set_text(f"{self.white_player.total_time_count:.1f} secs")
            self.white_player.drop_down_time_hist.set_item_list(self.white_player.time_hist_list)
            self.white_player.your_turn.set_text("")
            self.white_player.score_count = score - len(self.board.black_marble_list)
            self.white_player.score_info.set_text(f"{self.black_player.score_count}")
            self.white_player.drop_move_hist_list.append(f"{self.move}")
            self.white_player.drop_move_hist.set_item_list(self.white_player.drop_move_hist_list)
            self.black_player.your_turn.set_text("Your Turn!")
            self.player_turn = TeamEnum.BLACK
            self.start_count = True

    def is_agent_computer(self):
        return self.setting_result["white_type"] == "Human" and self.setting_result["black_type"] == "Computer"


    def finish(self):

        self.start_game = False


def main():
    game = GameMenu()
    game.display_menu()


# execute here!
if __name__ == '__main__':
    main()
