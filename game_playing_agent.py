from state_space_generator import StateSpaceGenerator as ssg
from eval_func_geoff import EvaluationFunction as ef


class GamePlayingAgent:

    def __init__(self, input_list):
        self._input_list = input_list
        self._state_space_gen = ssg()
        self.next_move_board_states = None
        self.next_moves = None
        self.next_moves_values = None
        self.greatest_move_value = 0

    def make_turn(self):
        self._state_space_gen.read_input_list(self._input_list)
        self.next_move_board_states = self._state_space_gen.state_space.generate_all_resulting_board_states()
        self.next_moves = self._state_space_gen.state_space.get_move_list()
        self.next_moves_values = self.assign_values(self.next_moves, self.next_move_board_states)
        # next moves and next move board states are now the best next moves below this
        self.next_moves, self.next_move_board_states = self.find_best_next_moves()

        # Assuming next_moves and next_move_board_states are in the right order
        """Assigns values to the next moves"""
    def assign_values(self, next_moves, next_move_states):
        values = list()
        for i in range(len(next_moves)):
            eval_func = ef(next_move_states[i], self._input_list[0])
            current_move_value = eval_func.evaluate_move()
            if current_move_value > self.greatest_move_value:
                self.greatest_move_value = current_move_value
            values.append(current_move_value)
        return values

    def find_best_next_moves(self):
        best_moves = list()
        best_states = list()
        for i in range(len(self.next_moves)):
            if self.next_moves_values[i] == self.greatest_move_value:
                best_moves.append(self.next_moves[i])
                best_states.append(self.next_move_board_states[i])
        return best_moves, best_states
