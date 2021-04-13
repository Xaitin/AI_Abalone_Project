import re

import pygame
import pygame_gui
from pygame_gui.elements import UIPanel, UIButton, UITextEntryLine, UILabel
from pygame_gui.elements.ui_text_box import UITextBox

from config import ConfigMenu
from constants import *
from enums.direction import DirectionEnum
from enums.team_enum import TeamEnum
from game_playing_agent import GamePlayingAgent
from models.board import Board
from models.move import Move
from player_section import PlayerSection
import _thread
import time


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
        self.agent = GamePlayingAgent()

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
        self.font_size_win = 15
        self.board_setup = dict()
        self.setting_result = dict()
        self.board_setup["Standard"] = 0
        self.board_setup["German Daisy"] = 1
        self.board_setup["Belgian Daisy"] = 2
        self.setting_result["selected_layout"] = "Standard"
        self.setting_result["white_type"] = "Human"
        self.setting_result["black_type"] = "Computer"
        self.setting_result["moves"] = 5
        self.player_each_time = [5, 5]
        self.white_state_list = list()
        self.black_state_list = list()
        self.stop_click = True
        self.pause_click = False
        self.black_player_first_move = True
        self.agent_time = 0
        # Texts
        self.draw_text("ABALONE", TITLE_FONT_SIZE, (WINDOW_WIDTH //
                                                   2, TITLE_DISTANCE_TOP + self.button_h // 2))

        # win title
        self.win = UILabel(relative_rect=pygame.Rect((WINDOW_WIDTH // 3.0, WINDOW_HEIGHT - 170), (400, 30)),
                           text=f'', manager=self.manager)
        self.win.hide()

        # Buttons on the top
        self.config_button = self.create_button(WINDOW_WIDTH // 2 - BUTTON_DISTANCE_3 - self.button_w,
                                                TITLE_DISTANCE_TOP,
                                                self.button_w, self.button_h, "config",
                                                self.manager)
        self.start_button = self.create_button(WINDOW_WIDTH // 2 - BUTTON_DISTANCE_2 - self.button_w,
                                               TITLE_DISTANCE_TOP,
                                               self.button_w, self.button_h, "start",
                                               self.manager)
        self.stop_button = self.create_button(WINDOW_WIDTH // 2 - BUTTON_DISTANCE_1 - self.button_w, TITLE_DISTANCE_TOP,
                                              self.button_w, self.button_h, "stop",
                                              self.manager)
        self.pause_button = self.create_button(WINDOW_WIDTH // 2 + BUTTON_DISTANCE_1, TITLE_DISTANCE_TOP, self.button_w,
                                               self.button_h, "pause",
                                               self.manager)
        self.undo_button = self.create_button(WINDOW_WIDTH // 2 + BUTTON_DISTANCE_2, TITLE_DISTANCE_TOP, self.button_w,
                                              self.button_h,
                                              "undo",
                                              self.manager)
        self.reset_button = self.create_button(WINDOW_WIDTH // 2 + BUTTON_DISTANCE_3, TITLE_DISTANCE_TOP, self.button_w,
                                               self.button_h, "reset",
                                               self.manager)
        temp_directions = 60
        temp = 80
        button_w_dir = self.button_w // 2
        button_h_dir = self.button_h // 1.4
        index = 2.8
        sub_h = WINDOW_HEIGHT - 100
        shift_w = 5

        self.NW_button = self.create_button(WINDOW_WIDTH // index + temp_directions * 3 - self.button_w + shift_w,
                                            sub_h - 0.6 * temp_directions,
                                            button_w_dir, button_h_dir, "NW",
                                            self.manager)
        self.NE_button = self.create_button(WINDOW_WIDTH // index + temp_directions * 4 - self.button_w + shift_w,
                                            sub_h - 0.6 * temp_directions,
                                            button_w_dir, button_h_dir, "NE",
                                            self.manager)
        self.W_button = self.create_button(WINDOW_WIDTH // index + temp_directions * 2.5 - self.button_w + shift_w, sub_h,
                                           button_w_dir, button_h_dir, "W",
                                           self.manager)
        self.E_button = self.create_button(WINDOW_WIDTH // index + temp_directions * 4.5 - self.button_w + shift_w, sub_h,
                                           button_w_dir, button_h_dir, "E",
                                           self.manager)
        self.SW_button = self.create_button(WINDOW_WIDTH // index + temp_directions * 3 - self.button_w + shift_w,
                                            sub_h + 0.6 * temp_directions,
                                            button_w_dir, button_h_dir, "SW",
                                            self.manager)
        self.SE_button = self.create_button(WINDOW_WIDTH // index + temp_directions * 4 - self.button_w + shift_w,
                                            sub_h + 0.6 * temp_directions,
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
            WINDOW_WIDTH // 2 + PANEL_DISTANCE_FROM_CENTER -
            PANEL_WIDTH, TITLE_DISTANCE_TOP * 2 + self.button_h
        ]

        self.apply_suggested_move_button = self.create_button(WINDOW_WIDTH // 1.7,
                                                              TITLE_DISTANCE_TOP + temp,
                                                              button_w_dir * 2, button_h_dir * 0.8, "Apply",
                                                              self.manager)

        self.switch_comp_button = self.create_button(WINDOW_WIDTH // index + temp * 2.2 - self.button_w + shift_w,
                                                     sub_h + 0.01 * temp,
                                                     button_w_dir * 4, button_h_dir * 0.8, "Switch Agent",
                                                     self.manager)
        self.switch_comp_button.hide()

        self.apply_suggested_move_button.disable()  # will be enabled when agent suggest the move

        self.suggested_entry = UITextEntryLine(
            pygame.Rect((WINDOW_WIDTH // 2 - 5.7 * shift_w, TITLE_DISTANCE_TOP + temp), (120, -1)), self.manager)

        self.draw_text("Suggested move", self.font_size // 2,
                       (WINDOW_WIDTH // 2 - 1.7 * temp, TITLE_DISTANCE_TOP + 1.2 * temp))

        self.black_player_panel = UIPanel(
            relative_rect=pygame.Rect(
                self.black_panel_position, (PANEL_WIDTH, PANEL_HEIGHT)),
            starting_layer_height=2,
            manager=self.manager
        )
        self.white_player_panel = UIPanel(
            relative_rect=pygame.Rect(
                self.white_panel_position, (PANEL_WIDTH, PANEL_HEIGHT)),
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

        self.black_player = PlayerSection(
            self.manager, self.black_player_panel)
        self.white_player = PlayerSection(
            self.manager, self.white_player_panel)
        # endregion Initialization

    @staticmethod
    def create_button(x, y, w, h, text, manager):
        return UIButton(relative_rect=pygame.Rect((x, y), (w, h)), text=text, manager=manager)

    def draw_text(self, text, size, pose):
        font = pygame.font.SysFont('comicsansms', size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (pose[0], pose[1])
        return self.display.blit(text_surface, text_rect)

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
                    self.on_direction_input(event.key)

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#suggested_move':
                    print(event.text)
                elif event.user_type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == '#next_move':
                    print(event.text)

                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == self.config_button:
                        self.open_config = True
                        self.config_menu = ConfigMenu(pygame.Rect((200, 15), (800, 700)), self.manager, self.display,
                                                      self.window)
                        print('Config!')
                    if event.ui_element == self.start_button:
                        if self.pause_click:
                            self.pause = False
                            self.pause_click = False
                        else:
                            self.resetting_board_player_panel()
                            self.open_config = False
                            self.start_game = True
                            self.stop_click = False
                        print('Start!')
                    if event.ui_element == self.stop_button:
                        self.stop_click = True
                        self.pause = True
                        print('Stop!')
                    if event.ui_element == self.pause_button:
                        self.pause_click = True
                        self.pause = True
                        print('Pause!')
                    if event.ui_element == self.undo_button:
                        self.undo()
                        print('Undo!')
                    if event.ui_element == self.reset_button:
                        self.resetting_board_player_panel()
                        self.start_game = False
                        self.pause_click = False

                    if event.ui_element == self.apply_suggested_move_button:
                        self.apply_suggested_move(self.suggested_entry.text)
                        self.apply_suggested_move_button.disable()

                    if event.ui_element in self.direction_buttons:
                        self.pause = False
                        self.on_direction_input(event.ui_element)
                        if self.is_agent_computer() and self.player_turn == TeamEnum.BLACK:
                            start_time = time.time()
                            self.agent_suggested()
                            end_time = time.time()
                            self.agent_time = end_time - start_time
                        elif self.is_computer_agent() and self.player_turn == TeamEnum.WHITE:
                            start_time = time.time()
                            self.agent_suggested('w')
                            end_time = time.time()
                            self.agent_time = end_time - start_time

                    if event.ui_element == self.switch_comp_button:
                        if self.player_turn == TeamEnum.BLACK:
                            """
                            agent_suggested: give suggestions not play itself
                            agent_play: agent play itself
                            """
                            # self.agent_suggested()
                            self.agent_play()
                        else:
                            # self.agent_suggested('w')
                            self.agent_play('w')

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

    def count_time(self, func):
        start_time = time.time()
        func()
        end_time = time.time()
        self.agent_time = end_time - start_time


    def store_move_hist_in_state(self):
        if self.player_turn == TeamEnum.WHITE:
            print("add state ", ["w", self.board.get_agent_input()])
            self.white_state_list.append(["w", self.board.get_agent_input()])
        else:
            print("add state ", ["b", self.board.get_agent_input()])
            self.black_state_list.append(["b", self.board.get_agent_input()])

    def undo(self):
        score = 14
        print("show list", self.black_state_list, self.white_state_list)
        if self.player_turn == TeamEnum.WHITE and len(self.black_state_list) > 0:
            last_previous_state = self.black_state_list[-1]
            self.black_state_list.pop(-1)
            previous_pose_2d = self.agent.get_ssg_list_position_2d(last_previous_state)
            self.board = Board(
                self.window, self.board_setup[self.setting_result["selected_layout"]], True, previous_pose_2d, TeamEnum.BLACK, self.prev_black_dead_marbles, self.prev_white_dead_marbles)
            prev_time = self.prev_black_time_count
            self.undo_player_info(self.black_player, self.white_player, score, prev_time)
            self.player_turn = TeamEnum.BLACK

        elif self.player_turn == TeamEnum.BLACK and len(self.white_state_list) > 0:
            last_previous_state = self.white_state_list[-1]
            self.white_state_list.pop(-1)
            previous_pose_2d = self.agent.get_ssg_list_position_2d(last_previous_state)
            self.board = Board(
                self.window, self.board_setup[self.setting_result["selected_layout"]], True, previous_pose_2d, TeamEnum.WHITE, self.prev_black_dead_marbles, self.prev_white_dead_marbles)
            prev_time = self.prev_white_time_count
            self.undo_player_info(self.white_player, self.black_player, score, prev_time)
            self.player_turn = TeamEnum.WHITE

        else:
            print("this is empty list")



    def undo_player_info(self, player, opponent, score, prev_time):
        if self.is_agent_computer() and self.player_turn == TeamEnum.WHITE:
            self.apply_suggested_move_button.enable()
        elif self.is_agent_computer() and self.player_turn == TeamEnum.BLACK:
            self.suggested_entry.set_text("")
            self.apply_suggested_move_button.disable()
        elif self.is_computer_agent() and self.player_turn == TeamEnum.BLACK:
            self.apply_suggested_move_button.enable()
        elif self.is_agent_computer() and self.player_turn == TeamEnum.WHITE:
            self.suggested_entry.set_text("")
            self.apply_suggested_move_button.disable()
        player.time_hist_list.pop(-1)
        player.drop_down_time_hist.kill()
        player.drop_move_hist.kill()
        player.total_time_count -= prev_time
        player.total_time_info.set_text(
            f"{self.white_player.total_time_count:.1f} secs")
        player.drop_down_time_hist.set_item_list(
            self.white_player.time_hist_list)
        player.your_turn.set_text("Your Turn!")
        # player.score_count = score - self.board.black_left
        # player.score_info.set_text(
        #     f"{self.white_player.score_count}")
        player.drop_move_hist_list.pop(-1)
        player.drop_move_hist.set_item_list(
            self.white_player.drop_move_hist_list)
        player.move_counts = len(self.white_player.drop_move_hist_list)
        player.total_move_info.set_text(f"{self.white_player.move_counts} moves")
        opponent.your_turn.set_text("")

    def on_direction_input(self, input: UIButton or int):
        self.store_move_hist_in_state()

        if not self.board.is_marble_selected():
            print("Warning: Select marbles, first")
            return

        if isinstance(input, UIButton):
            direction_str = input.text
            direction = DirectionEnum[direction_str]
        else:
            direction = DirectionEnum.get_from_key(input)

        move = self.board.generate_move(direction)
        is_valid_move = self.board.validate_move(move)
        if is_valid_move:
            print("is_valid_move")
            self.move = move
            self.board.apply_move(move)
            self.switch_player()
        else:
            print("Invalid move detected!")

    def agent_suggested(self, agent="b"):
        new_state = self.board.get_agent_input()
        input_list = [agent, new_state]
        self.agent.set_input_list(input_list)
        new_move, new_state_from_agent = self.agent.make_turn()
        self.suggested_entry.set_text(new_move)
        self.apply_suggested_move_button.enable()

    def apply_suggested_move(self, move_str):
        self.store_move_hist_in_state()
        new_move = Move.get_from_move_string(move_str)
        self.move = new_move
        print("move from the agent applied!", move_str)
        self.board.select_marbles_from_move(new_move)
        self.board.apply_move(new_move)
        self.switch_player()

    def agent_play(self, agent="b"):
        self.store_move_hist_in_state()
        new_state = self.board.get_agent_input()
        input_list = [agent, new_state]
        self.agent.set_input_list(input_list)
        if self.black_player_first_move:
            new_move_str, new_state_from_agent = self.agent.make_first_random_move()
            self.black_player_first_move = False
        else:
            new_move_str, new_state_from_agent = self.agent.make_turn()
        new_move = Move.get_from_move_string(new_move_str)
        self.move = new_move
        print("new_move from the agent!", new_move_str)
        self.board.select_marbles_from_move(new_move)
        self.board.apply_move(new_move)
        self.switch_player()

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
        self.board = Board(
            self.window, self.board_setup[self.setting_result["selected_layout"]])
        self.player_each_time = [int(re.search(r'\d+', self.setting_result["black_time"]).group()),
                                 int(re.search(r'\d+', self.setting_result["white_time"]).group())]
        self.setting_result["moves"] = int(
            re.search(r'\d+', self.setting_result["moves"]).group())

        config.SELECTED_INITIAL.set_text(
            self.setting_result["selected_layout"])
        config.WHITE_TIME_INPUT.set_text(self.setting_result["white_time"])
        config.WHITE_TYPE_INPUT.set_text(self.setting_result["white_type"])
        config.BLACK_TIME_INPUT.set_text(self.setting_result["black_time"])
        config.BLACK_TYPE_INPUT.set_text(self.setting_result["black_type"])

    def resetting_board_player_panel(self):
        self.start_count = True
        self.initialize_one_time = True
        self.win.hide()
        self.win.set_text(f"")
        self.suggested_entry.set_text(f"")
        self.white_state_list = list()
        self.black_state_list = list()
        self.black_player.drop_down_time_hist.kill()
        self.white_player.drop_down_time_hist.kill()
        self.black_player.drop_move_hist.kill()
        self.white_player.drop_move_hist.kill()
        self.black_player = PlayerSection(
            self.manager, self.black_player_panel)
        self.white_player = PlayerSection(
            self.manager, self.white_player_panel)
        self.player_turn = TeamEnum.BLACK
        self.board = Board(
            self.window, self.board_setup[self.setting_result["selected_layout"]])
        self.win.rebuild()
        if self.is_computer_computer():
            self.NW_button.hide()
            self.NE_button.hide()
            self.W_button.hide()
            self.E_button.hide()
            self.SW_button.hide()
            self.SE_button.hide()
            self.switch_comp_button.show()
        else:
            self.NW_button.show()
            self.NE_button.show()
            self.W_button.show()
            self.E_button.show()
            self.SW_button.show()
            self.SE_button.show()
            self.switch_comp_button.hide()

    def display_menu(self):
        self.manager.root_container.show()
        pygame.image.load('drawables/game_board.png').convert_alpha()
        clock = pygame.time.Clock()
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, 1000)
        self.time_count = 0
        self.start_count = True
        self.current_time = 0
        self.player_turn = TeamEnum.BLACK
        self.each_time_count = 0
        self.initialize_one_time = True
        self.pause = False
        while self.game_playing:
            time_delta = clock.tick(30) / 1000.0
            self.time_count += time_delta
            self.check_event()
            self.manager.update(time_delta)
            self.window.blit(self.display, (0, 0))
            self.manager.draw_ui(self.window)
            if not self.open_config and self.start_game:
                if not self.pause:
                    if self.is_agent_computer():
                        if self.initialize_one_time:
                            print("pass agent move")
                            self.agent_play()
                            if self.is_computer_computer():
                                self.agent_suggested("w")
                            self.initialize_one_time = False
                    if self.start_count:
                        self.current_time = self.time_count
                        self.start_count = False
                    self.add_timer()
                self.board.update()
                self.finish_game()
            pygame.display.update()
        pygame.quit()

    def add_timer(self):
        start_zero = self.time_count - self.current_time
        self.each_time_count = start_zero
        time_in_secs = self.player_each_time[0] - start_zero
        if self.player_turn == TeamEnum.BLACK:
            self.black_player.time_limit_info.set_text(
                f"{time_in_secs:.1f} secs" if time_in_secs >= 0 else f"{time_in_secs:.1f} secs!")
        else:
            self.white_player.time_limit_info.set_text(
                f"{time_in_secs:.1f} secs" if time_in_secs >= 0 else f"{time_in_secs:.1f} secs!")

    def is_agent_computer(self):
        return self.setting_result["white_type"] == "Human" and self.setting_result["black_type"] == "Computer"

    def is_computer_agent(self):
        return self.setting_result["white_type"] == "Computer" and self.setting_result["black_type"] == "Human"

    def is_computer_computer(self):
        return self.setting_result["white_type"] == "Computer" and self.setting_result["black_type"] == "Computer"

    def switch_player(self):
        # Use this to get the board state
        self.board.__str__()
        if self.player_turn == TeamEnum.BLACK:
            self.prev_black_time_count = self.each_time_count
            if self.is_agent_computer() and self.player_turn == TeamEnum.BLACK:
                self.black_player.time_hist_list.append(
                    f"{self.agent_time:.2f} secs")
                self.black_player.total_time_count += self.agent_time
                self.black_player.total_time_info.set_text(
                    f"{self.black_player.total_time_count:.2f} secs")
                self.black_player.drop_down_time_hist.set_item_list(
                    self.black_player.time_hist_list)
            elif self.is_computer_agent() and self.player_turn == TeamEnum.WHITE:
                self.black_player.time_hist_list.append(
                    f"{self.agent_time:.2f} secs")
                self.black_player.total_time_count += self.agent_time
                self.black_player.total_time_info.set_text(
                    f"{self.black_player.total_time_count:.2f} secs")
                self.black_player.drop_down_time_hist.set_item_list(
                    self.black_player.time_hist_list)
            else:
                self.black_player.time_hist_list.append(
                    f"{self.each_time_count:.1f} secs")
                self.black_player.total_time_count += self.each_time_count
                self.black_player.total_time_info.set_text(
                    f"{self.black_player.total_time_count:.f} secs")
                self.black_player.drop_down_time_hist.set_item_list(
                    self.black_player.time_hist_list)

            self.black_player.your_turn.set_text("")
            self.black_player.score_count = len(self.board.white_dead_marbles)
            self.prev_white_dead_marbles = self.board.white_dead_marbles
            self.black_player.score_info.set_text(
                f"{self.black_player.score_count}")
            self.black_player.drop_move_hist_list.append(f"{self.move}")
            self.black_player.drop_move_hist.set_item_list(
                self.black_player.drop_move_hist_list)
            self.black_player.move_counts = len(self.black_player.drop_move_hist_list)
            self.black_player.total_move_info.set_text(f"{self.black_player.move_counts} moves")
            self.white_player.your_turn.set_text("Your Turn!")
            self.player_turn = TeamEnum.WHITE
            self.start_count = True
        else:
            self.prev_white_time_count = self.each_time_count

            if self.is_agent_computer() and self.player_turn == TeamEnum.BLACK:
                self.white_player.time_hist_list.append(
                    f"{self.agent_time:.1f} secs")
                self.white_player.total_time_count += self.agent_time
                self.white_player.total_time_info.set_text(
                    f"{self.white_player.total_time_count:.1f} secs")
                self.white_player.drop_down_time_hist.set_item_list(
                    self.white_player.time_hist_list)
            elif self.is_computer_agent() and self.player_turn == TeamEnum.WHITE:
                self.white_player.time_hist_list.append(
                    f"{self.agent_time:.1f} secs")
                self.white_player.total_time_count += self.agent_time
                self.white_player.total_time_info.set_text(
                    f"{self.white_player.total_time_count:.1f} secs")
                self.white_player.drop_down_time_hist.set_item_list(
                    self.white_player.time_hist_list)
            else:
                self.white_player.time_hist_list.append(
                    f"{self.each_time_count:.1f} secs")
                self.white_player.total_time_count += self.each_time_count
                self.white_player.total_time_info.set_text(
                    f"{self.white_player.total_time_count:.1f} secs")
                self.white_player.drop_down_time_hist.set_item_list(
                    self.white_player.time_hist_list)

            self.white_player.your_turn.set_text("")
            self.white_player.score_count = len(self.board.black_dead_marbles)
            self.prev_black_dead_marbles = self.board.black_dead_marbles
            self.white_player.score_info.set_text(
                f"{self.white_player.score_count}")
            self.white_player.drop_move_hist_list.append(f"{self.move}")
            self.white_player.drop_move_hist.set_item_list(
                self.white_player.drop_move_hist_list)
            self.white_player.move_counts = len(self.white_player.drop_move_hist_list)
            self.white_player.total_move_info.set_text(f"{self.white_player.move_counts} moves")
            self.black_player.your_turn.set_text("Your Turn!")
            self.player_turn = TeamEnum.BLACK
            self.start_count = True

    def finish_game(self):
        # print("Moves", self.setting_result["moves"])
        if self.white_player.score_count == 6:
            # self.start_game = False
            self.win.show()
            self.win.set_text("Congratulations! White player is winner!")
            # self.win = self.draw_text("Congratulations! White player is winner!", self.font_size_win,
            #                           (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        elif self.black_player.score_count == 6:
            # self.start_game = False
            self.win.show()
            self.win.set_text("Congratulations! Black player is winner!")
            # self.win = self.draw_text("Congratulations! Black player is winner!", self.font_size_win,
            #                           (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        elif self.white_player.move_counts == self.setting_result["moves"] and self.black_player.move_counts == \
                self.setting_result["moves"]:
            self.win.show()
            if self.white_player.score_count > self.black_player.score_count:
                self.win.set_text("White player is winner with the higher score!")
            elif self.white_player.score_count < self.black_player.score_count:
                self.win.set_text("Black player is winner with the higher score!")
            else:
                self.win.set_text("It's Tie!")


def timer(context):
    try:
        count_time = 0
        while True:
            pygame.time.delay(100)

            if context.player_turn == TeamEnum.BLACK:
                count_time += 0.1
                time_in_secs = context.player_each_time[0] - count_time
                context.black_player.time_limit_info.set_text(
                    f"{count_time:.1f} secs" if time_in_secs >= 0 else f"{time_in_secs:.1f} secs!")
            else:
                count_time += 0.1
                time_in_secs = context.player_each_time[1] - count_time
                context.white_player.time_limit_info.set_text(
                    f"{time_in_secs:.1f} secs" if time_in_secs >= 0 else f"{time_in_secs:.1f} secs!")

    except RuntimeError:
        print("RuntimeError from time_oscillator.")


def start_time(context):
    _thread.start_new_thread(timer, (context,))


def main():
    game = GameMenu()
    game.display_menu()


# execute here!
if __name__ == '__main__':
    main()
