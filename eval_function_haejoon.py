from helper.coordinate_helper import CoordinateHelper


class EvaluationFunction:
    # board ex: 'A1b,A2b,A3b,A4b,A5b,B2b,B3b,B4b,B5b,B6b,C2b,C3b,C5b,C6b,F5w,G5w,G6w,G7w,H4w,H5w,H6w,H7w,H8w,H9w,I6w,I7w,I8w,I9w'
    # color ex: 'b'
    # Previous board ex.
    # ['b',
    #  'A1b,A2b,A3b,A4b,A5b,B1b,B2b,B3b,B4b,B5b,B6b,C3b,C5b,C6b,F5w,G5w,G6w,G7w,H4w,H5w,H6w,H7w,H8w,H9w,I6w,I7w,I8w,I9w']
    def __init__(self, board, friendly_color, previous_board):
        self._board_state = board
        self._friendly_color = friendly_color
        self._previous_board = previous_board

    def evaluate_move(self):
        center_proximity = 0
        cohesion = 0
        marbles_on_board = 0
        dead_marble_constant = 10

        _black_marbles = list()
        _white_marbles = list()

        n_black_alive = len(_black_marbles)
        n_black_dead = 14 - n_black_alive
        n_white_alive = len(_white_marbles)
        n_white_dead = 14 - n_white_alive

        result_value = 0

        marble_str_array = self._board_state.split(',')
        for marble_str in marble_str_array:
            if 'b' == marble_str[2]:
                _black_marbles.append(CoordinateHelper.from_cube_str_to_2d(marble_str))
            else:
                _white_marbles.append(CoordinateHelper.from_cube_str_to_2d(marble_str))

        self.com_black_2d = (round(sum([marble[0] for marble in _black_marbles]) / len(_black_marbles)),
                             round(sum([marble[1] for marble in _black_marbles]) / len(_black_marbles)))
        self.com_white_2d = (round(sum([marble[0] for marble in _white_marbles]) / len(_white_marbles)),
                             round(sum([marble[1] for marble in _white_marbles]) / len(_white_marbles)))
        center = (5, 5)

        modified_center = (round(center[0] + self.com_black_2d[0] + self.com_white_2d[0] / 3),
                           round(center[1] + self.com_black_2d[1] + self.com_white_2d[1] / 3))

        manhattan_distances_black = [CoordinateHelper.get_manhattan_distance(modified_center, marble_2d) for marble_2d in _black_marbles]
        manhattan_distances_white = [CoordinateHelper.get_manhattan_distance(modified_center, marble_2d) for marble_2d in _white_marbles]

        black_value = sum(manhattan_distances_black) + dead_marble_constant * n_black_dead
        white_value = sum(manhattan_distances_white) + dead_marble_constant * n_white_dead

        return abs(black_value - white_value)


def main():
    board = 'A1b,A2b,A3b,A4b,A5b,B2b,B3b,B4b,B5b,B6b,C2b,C3b,C5b,C6b,F5w,G5w,G6w,G7w,H4w,H5w,H6w,H7w,H8w,H9w,I6w,I7w,I8w,I9w'
    color = 'b'
    prev = ['b',
            'A1b,A2b,A3b,A4b,A5b,B1b,B2b,B3b,B4b,B5b,B6b,C3b,C5b,C6b,F5w,G5w,G6w,G7w,H4w,H5w,H6w,H7w,H8w,H9w,I6w,I7w,I8w,I9w']
    ef = EvaluationFunction(board, color, prev)
    print("evaluation of the board state -> ", ef.evaluate_move())


if __name__ == "__main__":
    main()
