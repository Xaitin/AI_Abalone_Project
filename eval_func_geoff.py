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

def main():
    board = 'A1b,A2b,A3b,A4b,A5b,B2b,B3b,B4b,B5b,B6b,C2b,C3b,C5b,C6b,F5w,G5w,G6w,G7w,H4w,H5w,H6w,H7w,H8w,H9w,I6w,I7w,I8w,I9w'
    color = 'b'
    prev = ['b',
            'A1b,A2b,A3b,A4b,A5b,B1b,B2b,B3b,B4b,B5b,B6b,C3b,C5b,C6b,F5w,G5w,G6w,G7w,H4w,H5w,H6w,H7w,H8w,H9w,I6w,I7w,I8w,I9w']
    ef = EvaluationFunction(board, color, prev)
    print("evaluation of the board state -> ", ef.evaluate_move())


if __name__ == "__main__":
    main()
