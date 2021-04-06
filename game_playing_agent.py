import math
import random
from datetime import datetime

from constants import *
from state_space_generator import StateSpaceGenerator as ssg
from eval_func_geoff import EvaluationFunction as ef


class GamePlayingAgent:
    def __init__(self, input_list=DEFAULT_AGENT_LIST):
        self._input_list = input_list
        self._agent_color = input_list[0]
        self._state_space_gen = ssg()
        self.next_move_board_states = list()
        self.next_moves = None
        self.next_moves_values = None
        self.greatest_move_value = 0
        self.next_opponent_moves_values = None
        self.next_opponents_moves = None
        self.next_move_marble_difference = list()

    def search_deeper(self):
        pass

    def get_ssg_list_position_2d(self, input_list):
        self._state_space_gen.read_input_list(input_list)
        return self._state_space_gen.state_space.marble_positions_2d

    def make_turn(self):
        self._state_space_gen.read_input_list(self._input_list)
        board_states = self._state_space_gen.state_space.generate_all_resulting_board_states()
        for line in board_states:
            stri = ""
            for marble in line:
                stri += marble + ","
            self.next_move_board_states.append(stri[:-1])
        self.next_move_marble_difference = self.find_marble_difference_in_states(self._input_list[1], self.next_move_board_states)
        self.next_moves = self._state_space_gen.state_space.get_move_list()
        self.next_moves_values = self.assign_move_values()
        print(self.next_moves)
        print(self.next_move_board_states)
        print(self.next_moves_values)
        self.search_deeper()
        self.next_moves, self.next_move_board_states, self.next_moves_values = self.find_best_next_moves()
        self.next_opponent_moves_values, self.next_opponents_moves = self.find_next_opponent_moves()
        if len(self.next_moves) == 1:
            print(self.next_moves[0])
            print(self.next_move_board_states[0])
            return self.next_moves[0], self.next_move_board_states[0]
        else:
            lowest_opponent_value = math.inf
            for i in range(len(self.next_moves)):
                if self.next_opponent_moves_values[i] < lowest_opponent_value:
                    lowest_opponent_value = self.next_opponent_moves_values[i]
            indexes = list()
            for i in range(len(self.next_moves)):
                if self.next_opponent_moves_values[i] < lowest_opponent_value:
                    indexes.clear()
                    lowest_opponent_value = self.next_opponent_moves_values[i]
                    indexes.append(i)
                elif self.next_opponent_moves_values[i] == lowest_opponent_value:
                    indexes.append(i)
            move_to_choose = indexes[random.randint(0, len(indexes) - 1)]
            print(self.next_moves[move_to_choose])
            print(self.next_move_board_states[move_to_choose])
            print(self.next_moves_values[move_to_choose])
            return self.next_moves[move_to_choose], self.next_move_board_states[move_to_choose]
        # This is our list of best moves and states with a depth of 2

    def assign_move_values(self):
        values = list()
        for i in range(len(self.next_moves)):
            eval_func = ef(self.next_move_board_states[i], self._agent_color, self._input_list)
            value = eval_func.evaluate_move()
            values.append(value)
        return values

    def find_best_next_moves(self):
        best_moves = list()
        best_states = list()
        best_values = list()
        for i in range(len(self.next_moves)):
            if self.next_move_marble_difference[i] != 0:
                self.next_moves_values[i] = self.quiescence_search(self.next_move_board_states[i])
                print("Reassigning value via quiescence search")
                print(self.next_moves_values[i])
                print("Break")
        highest_move_value = -math.inf
        for i in range(len(self.next_moves)):
            if self.next_moves_values[i] > highest_move_value:
                highest_move_value = self.next_moves_values[i]
        for z in range(len(self.next_moves)):
            if self.next_moves_values[z] == highest_move_value:
                best_moves.append(self.next_moves[z])
                best_states.append(self.next_move_board_states[z])
                best_values.append(self.next_moves_values[z])
        return best_moves, best_states, best_values

    def quiescence_search(self, state):
        if self._agent_color == "b":
            color = "w"
            start_color = "b"
        else:
            color = "b"
            start_color = "w"
        my_ssg = ssg()
        initial_list = list()
        initial_list.append(color)
        initial_list.append(state)
        found_non_volatile_move = False
        while found_non_volatile_move is not True:
            my_ssg.read_input_list(initial_list)
            next_move_board_states = list()
            board_states = my_ssg.state_space.generate_all_resulting_board_states()
            for line in board_states:
                stri = ""
                for marble in line:
                    stri += marble + ","
                next_move_board_states.append(stri[:-1])
            next_move_values = self.find_marble_difference_in_states(initial_list[1], next_move_board_states)
            end_state = True
            new_states = list()
            new_values = list()
            highest_value = -math.inf
            for i in range(len(next_move_values)):
                if next_move_values[i] != 0:
                    end_state = False
                    eval_func = ef(next_move_board_states[i], color, self._input_list)
                    value = eval_func.evaluate_move()
                    if value > highest_value:
                        highest_value = value
                    new_states.append(next_move_board_states[i])
                    new_values.append(value)
            if end_state:
                if color == start_color:
                    # Opponent was last to move. Return highest value. Its highest value of next moves
                    if highest_value == -math.inf:
                        eval_func = ef(initial_list[1], start_color, self._input_list)
                        highest_value = eval_func.evaluate_move()
                    return highest_value
                else:
                    # Agent was last to move. Grab value of initial_list[1]
                    eval_func = ef(initial_list[1], start_color, self._input_list)
                    return eval_func.evaluate_move()
            if color == "w":
                color = "b"
            elif color == "b":
                color = "w"
            if not end_state:
                for z in range(len(new_states)):
                    if new_values[z] == highest_value:
                        initial_list = list()
                        initial_list.append(color)
                        initial_list.append(new_states[z])

    def find_next_opponent_moves(self):
        next_opponent_move_values = list()
        next_opponent_moves = list()
        if self._agent_color == "b":
            color = "w"
        else:
            color = "b"
        for state in self.next_move_board_states:
            next_opponent_board_states = list()
            input_list = list()
            input_list.append(color)
            input_list.append(state)
            self._state_space_gen.read_input_list(input_list)
            board_states = self._state_space_gen.state_space.generate_all_resulting_board_states()
            move_list = self._state_space_gen.state_space.get_move_list()
            for line in board_states:
                _str = ""
                for marble in line:
                    _str += marble + ","
                next_opponent_board_states.append(_str[:-1])
            greatest_opponent_move_value = -math.inf
            for opponent_state in next_opponent_board_states:
                eval_func = ef(opponent_state, color, self._input_list)
                current_move_value = eval_func.evaluate_move()
                if current_move_value > greatest_opponent_move_value:
                    greatest_opponent_move_value = current_move_value
            for i in range(len(move_list)):
                eval_func = ef(next_opponent_board_states[i], color, self._input_list)
                value = eval_func.evaluate_move()
                if value == greatest_opponent_move_value:
                    next_opponent_moves.append(move_list[i])
            next_opponent_moves.append("Break")
            next_opponent_move_values.append(greatest_opponent_move_value)
        return next_opponent_move_values, next_opponent_moves

    def set_input_list(self, input_list):
        self._input_list = input_list
        self._agent_color = input_list[0]
        self._state_space_gen = ssg()
        self.next_move_board_states = list()
        self.next_moves = None
        self.next_moves_values = None
        self.greatest_move_value = 0
        self.next_opponent_moves_values = None
        self.next_opponents_moves = None
        self.next_move_marble_difference = list()

    def find_marble_difference_in_states(self, check, next_states):
        check_list = check
        return_list = list()
        for i in range(len(next_states)):
            counter = len(check_list) - len(next_states[i])
            return_list.append(counter)
        return return_list



def main():
    running = True
    running_count = 0
    my_list = ["b",
               "A1b,A2b,A3b,A4b,A5b,B1b,B2b,B3b,B4b,B5b,B6b,C3b,C4b,C5b,G5w,G6w,G7w,H4w,H5w,H6w,H7w,H8w,H9w,I5w,I6w,I7w,I8w,I9w"]
    agent = GamePlayingAgent(my_list)
    start_time = datetime.now()
    print(f"start time: {start_time}\n")
    while running:
        running_count += 1
        print(f"===Move #: {running_count}===")
        print("Black Moving")
        new_move, new_state = agent.make_turn()
        print("White Moving")
        agent.set_input_list(["w",
                              new_state])
        new_move_w, new_state_w = agent.make_turn()
        agent.set_input_list(["b",
                              new_state_w])
        if running_count == 5:
            running = False
    end_time = datetime.now()
    exe_time = end_time - start_time
    print(f"\nend time: {end_time}")
    print(f"execution time (sec): {exe_time.total_seconds()}")


if __name__ == '__main__':
    main()
