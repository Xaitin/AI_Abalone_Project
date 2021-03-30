import math

from state_space_generator import StateSpaceGenerator as ssg
from eval_func_geoff import EvaluationFunction as ef


class GamePlayingAgent:

    def __init__(self, input_list):
        self._input_list = input_list
        self._agent_color = input_list[0]
        self._state_space_gen = ssg()
        self.next_move_board_states = list()
        self.next_moves = None
        self.next_moves_values = None
        self.greatest_move_value = 0
        self.next_opponent_moves_values = None
        self.next_opponents_moves = None

    def make_turn(self):
        self._state_space_gen.read_input_list(self._input_list)
        board_states = self._state_space_gen.state_space.generate_all_resulting_board_states()
        for line in board_states:
            _str = ""
            for marble in line:
                _str += marble + ","
            self.next_move_board_states.append(_str[:-1])
        self.next_moves = self._state_space_gen.state_space.get_move_list()
        self.next_moves_values = self.assign_move_values()
        self.next_moves, self.next_move_board_states, self.next_moves_values = self.find_best_next_moves()
        self.next_opponent_moves_values, self.next_opponents_moves = self.find_next_opponent_moves()
        print(self.next_moves)
        print(self.next_moves_values)
        print(self.next_opponent_moves_values)
        print(self.next_opponents_moves)
        # This is our list of best moves and states with a depth of 2

    def assign_move_values(self):
        values = list()
        for i in range(len(self.next_moves)):
            eval_func = ef(self.next_move_board_states[i], self._agent_color)
            value = eval_func.evaluate_move()
            values.append(value)
        return values

    def find_best_next_moves(self):
        best_moves = list()
        best_states = list()
        best_values = list()
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

    def find_next_opponent_moves(self):
        next_opponent_move_values = list()
        next_opponent_moves = list()
        if self._agent_color == "b":
            color = "w"
        else:
            color = "b"
            print(self.next_move_board_states)
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
                eval_func = ef(opponent_state, color)
                current_move_value = eval_func.evaluate_move()
                if current_move_value > greatest_opponent_move_value:
                    greatest_opponent_move_value = current_move_value
            for i in range(len(move_list)):
                eval_func = ef(next_opponent_board_states[i], color)
                value = eval_func.evaluate_move()
                if value == greatest_opponent_move_value:
                    next_opponent_moves.append(move_list[i])
            next_opponent_moves.append("Break")
            next_opponent_move_values.append(greatest_opponent_move_value)
        return next_opponent_move_values, next_opponent_moves


def main():
    my_list = list()
    my_list.append("b")
    my_list.append("C3b,C4b,C5b,D4b,D5b,E5b,F5w,F6w,G5w,G7w,H5w,H6w,H7w,H8w")
    agent = GamePlayingAgent(my_list)
    agent.make_turn()


if __name__ == '__main__':
    main()
