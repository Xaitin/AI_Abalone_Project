from constants import FRIENDLY_SQUARE_VALUES, ENEMY_SQUARE_VALUES


class EvaluationFunction:

    def __init__(self, board, friendly_color, previous_board):
        self._board_state = board
        self._friendly_color = friendly_color
        self._previous_board = previous_board

    def evaluate_move(self):
        marbles = self._board_state.split(',')
        prev_marbles = self._previous_board[1].split(',')
        square_control_value = 0
        friendly_marble_value = 0
        enemy_marble_value = 0
        prev_friendly_val = 0
        prev_enemy_val = 0
        for marble in marbles:
            pos = marble[0] + marble[1]
            if marble[2] == self._friendly_color:
                value_at_square = FRIENDLY_SQUARE_VALUES.get(pos)
                if value_at_square is not None:
                    square_control_value += value_at_square
                friendly_marble_value += 1000000
            else:
                value_at_square = ENEMY_SQUARE_VALUES.get(pos)
                if value_at_square is not None:
                    square_control_value += value_at_square
                enemy_marble_value += 1000000
        for m in prev_marbles:
            if m[2] == self._friendly_color:
                prev_friendly_val += 1000000
            else:
                prev_enemy_val += 1000000
        prev_marble_value = prev_friendly_val - prev_enemy_val
        marble_count_value = friendly_marble_value - enemy_marble_value
        return square_control_value + (marble_count_value - prev_marble_value)
