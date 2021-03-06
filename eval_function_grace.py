import math
from itertools import combinations

from constants import LETTER_SHIFT, NUMBER_SHIFT


class EvaluationFunction:

    def __init__(self, board, player):
        self._board_state = board
        self._black_marbles = []
        self._white_marbles = []
        self._center = (5, 5)
        self._player = player

    def evaluate_move(self):
        center_proximity = 0
        cohesion = 0
        marbles_on_board = 0

        marbles = self._board_state.split(',')
        for m in marbles:
            if 'b' in m:
                self._black_marbles.append(m)
            else:
                self._white_marbles.append(m)

        center_proximity = (self.center_proximity(self._player) -
                            self.center_proximity('w' if self._player == 'b' else 'b'))

        # If all the marbles are overall further away from the board,
        # we check cohesion to see if it's not overall a terrible state
        if abs(center_proximity) > 2:
            cohesion = self.cohesion(self._player) - self.cohesion('w' if self._player == 'b' else 'b')
        # Else if the marbles are over all closer, then we can check how many marbles we have on the board.
        # This is multiplied with 100 to give a more favorable score since this is an attacking position.
        if abs(center_proximity) < 2:
            marbles_on_board = (self.marbles_on_board('w' if self._player == 'b' else 'b') * 100 -
                                self.marbles_on_board(self._player) * 100)

        return center_proximity + cohesion + marbles_on_board

    def center_proximity(self, player):
        distance = -math.inf
        if player == 'b':
            for m in self._black_marbles:
                if distance == -math.inf:
                    distance = (abs((LETTER_SHIFT - ord(m[0])) - self._center[0]) + abs(
                        (int(m[1]) - NUMBER_SHIFT) - self._center[1])) / 2
                else:
                    distance += (abs((LETTER_SHIFT - ord(m[0])) - self._center[0]) + abs(
                        (int(m[1]) - NUMBER_SHIFT) - self._center[1])) / 2
            return distance / len(self._black_marbles)
        else:
            for m in self._white_marbles:
                if distance == -math.inf:
                    distance = (abs((LETTER_SHIFT - ord(m[0])) - self._center[0]) + abs(
                        (int(m[1]) - NUMBER_SHIFT) - self._center[1])) / 2
                else:
                    distance += (abs((LETTER_SHIFT - ord(m[0])) - self._center[0]) + abs(
                        (int(m[1]) - NUMBER_SHIFT) - self._center[1])) / 2
            return distance / len(self._white_marbles)

    def cohesion(self, player):
        distance = -math.inf
        if player == 'b':
            all_combinations = list(combinations(self._black_marbles, len(self._black_marbles)))
            for m in all_combinations:
                if distance == -math.inf:
                    distance = (abs((LETTER_SHIFT - ord(m[0])) - (LETTER_SHIFT - ord(m[2]))) + abs(
                        (int(m[1]) - NUMBER_SHIFT) - (int(m[3]) - NUMBER_SHIFT)) / 2)
                else:
                    distance += (abs((LETTER_SHIFT - ord(m[0])) - (LETTER_SHIFT - ord(m[2]))) + abs(
                        (int(m[1]) - NUMBER_SHIFT) - (int(m[3]) - NUMBER_SHIFT)) / 2)
            return distance / len(all_combinations)
        else:
            all_combinations = list(combinations(self._white_marbles, len(self._white_marbles)))
            for m in all_combinations:
                if distance == -math.inf:
                    distance = (abs((LETTER_SHIFT - ord(m[0])) - (LETTER_SHIFT - ord(m[2]))) + abs(
                        (int(m[1]) - NUMBER_SHIFT) - (int(m[3]) - NUMBER_SHIFT)) / 2)
                else:
                    distance += (abs((LETTER_SHIFT - ord(m[0])) - (LETTER_SHIFT - ord(m[2]))) + abs(
                        (int(m[1]) - NUMBER_SHIFT) - (int(m[3]) - NUMBER_SHIFT)) / 2)
            return distance / len(all_combinations)

    def marbles_on_board(self, player):
        if player == 'b':
            return len(self._black_marbles)
        else:
            return len(self._white_marbles)

def main():
    board = 'A1b,A2b,A3b,A4b,A5b,B2b,B3b,B4b,B5b,B6b,C2b,C3b,C5b,C6b,F5w,G5w,G6w,G7w,H4w,H5w,H6w,H7w,H8w,H9w,I6w,I7w,I8w,I9w'
    color = 'b'
    prev = ['b',
            'A1b,A2b,A3b,A4b,A5b,B1b,B2b,B3b,B4b,B5b,B6b,C3b,C5b,C6b,F5w,G5w,G6w,G7w,H4w,H5w,H6w,H7w,H8w,H9w,I6w,I7w,I8w,I9w']
    ef = EvaluationFunction(board, color)
    print("evaluation of the board state -> ", ef.evaluate_move())


if __name__ == "__main__":
    main()
