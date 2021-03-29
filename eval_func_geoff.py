from constants import FRIENDLY_SQUARE_VALUES, ENEMY_SQUARE_VALUES


class EvaluationFunction:

    def __init__(self, board, friendly_color):
        self._board_state = board
        self._friendly_color = friendly_color

    def evaluate_move(self):
        marbles = self._board_state.split(',')
        square_control_value = 0
        friendly_marble_value = 0
        enemy_marble_value = 0
        for marble in marbles:
            pos = marble[0] + marbles[1]
            if marble[2] == self._friendly_color:
                square_control_value += FRIENDLY_SQUARE_VALUES.get(pos)
                friendly_marble_value += 10
            else:
                square_control_value += ENEMY_SQUARE_VALUES.get(pos)
                enemy_marble_value += 10
        marble_count_value = friendly_marble_value - enemy_marble_value
        return square_control_value + marble_count_value
