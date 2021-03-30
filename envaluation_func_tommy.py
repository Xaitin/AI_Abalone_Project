import copy
from models.state_space import StateSpace
from models.position import Position
from constants import *
from enums.team_enum import *

class Evaluation:
    def __init__(self, player, marble_positions):
        self.state_space = StateSpace()
        self.marble_positions = [Position(TeamEnum.BLACK if position[0] == 'b' else TeamEnum.WHITE, position[1]) for
                                 position in self.state_space.read_position_strings(marble_positions)]
        print(self.marble_positions)
        self.state = self.state_space.to_2d_array(self.marble_positions)

        self.ally = None
        self.enemy = None
        self.enemy_player = None
        self.player = player
        if self.player == TeamEnum.BLACK:
            self.ally = TeamEnum.BLACK.value
            self.enemy = TeamEnum.WHITE.value
            self.enemy_player = TeamEnum.WHITE
        elif self.player == TeamEnum.WHITE:
            self.ally = TeamEnum.WHITE.value
            self.enemy = TeamEnum.BLACK.value
            self.enemy_player = TeamEnum.BLACK
        self.state_space.set_player_value(TeamEnum.BLACK.value)
        self.state_space.set_marble_positions_2d(self.state_space.to_2d_array(self.marble_positions))
        self.state_space.set_player_value(self.ally)
        self.ally_pieces_locations = copy.copy(self.state_space.get_ally_position(self.state))
        self.state_space.set_player_value(self.enemy)
        self.opp_pieces_locations = copy.copy(self.state_space.get_ally_position(self.state))
        self.last_coefficients = None

    def get_evaluation_score(self):
        # Initialize the score.
        score = 0
        weight_coefficients = [500000, 100000, 1000, 10, 1.5, 1, 1, 1, 1]
        weight_coefficients_test1 = [800000, 70000, 5000, 10, 1.5, 1, 1, 1, 1]
        weight_coefficients_test2 = [1000000, 200000, 1500, 10, 1.2, 1.5, 1, 1.5, 1]
        self.last_coefficients = weight_coefficients[5:8]

        score += weight_coefficients[0] * self.terminal_state()
        score += weight_coefficients[1] * self.piece_count()
        score += weight_coefficients[2] * self.in_danger_zone()
        score += weight_coefficients[3] * self.manhattan_distance()
        score += weight_coefficients[4] * self.clumping()
        score += self.sumito_num_pairs_triplets()
        score += weight_coefficients[8] * self.strengthen_group()
        return score

    def terminal_state(self):
        ally_pieces_count = 0
        opponent_pieces_count = 0
        for i in range(BOARD_ARRAY_SIZE):
            for j in range(BOARD_ARRAY_SIZE):
                if self.state[i][j] == self.ally:
                    ally_pieces_count += 1
                if self.state[i][j] == self.enemy:
                    opponent_pieces_count += 1
        if ally_pieces_count < LOSE_MARBLE_NUM:
            return -1
        if opponent_pieces_count < LOSE_MARBLE_NUM:
            return 1
        else:
            return 0

    def piece_count(self):
        pieces_score = 0

        for i in range(BOARD_ARRAY_SIZE):
            for j in range(BOARD_ARRAY_SIZE):
                if self.state[i][j] == self.ally:
                    pieces_score += 1
                if self.state[i][j] == self.enemy:
                    pieces_score -= 1
        return pieces_score

    def in_danger_zone(self):
        score_count = 0
        for i in range(BOARD_ARRAY_SIZE):
            for j in range(BOARD_ARRAY_SIZE):
                if self.state[i][j] == self.ally:
                    score_count += DANGER_ZONE_INDICATOR[i][j]
                if self.state[i][j] == self.enemy:
                    score_count -= DANGER_ZONE_INDICATOR[i][j]
        return score_count

    def manhattan_distance(self):
        score_count = 0
        for i in range(BOARD_ARRAY_SIZE):
            for j in range(BOARD_ARRAY_SIZE):
                if self.state[i][j] == self.ally:
                    score_count += MANHATTAN_WEIGHT[i][j]
                if self.state[i][j] == self.enemy:
                    score_count -= MANHATTAN_WEIGHT[i][j]
        return score_count

    def clumping(self):
        robustness = 0
        for location in self.ally_pieces_locations:
            for nearby_location_with_dir in self.state_space.get_surrounding_dir_positions(location):
                if nearby_location_with_dir[1] in self.ally_pieces_locations and \
                        self.state[nearby_location_with_dir[1][0]][nearby_location_with_dir[1][1]] == self.ally:
                    robustness += 1

        for location in self.opp_pieces_locations:
            for nearby_location_with_dir in self.state_space.get_surrounding_dir_positions(location):
                if nearby_location_with_dir[1] in self.opp_pieces_locations and \
                        self.state[nearby_location_with_dir[1][0]][nearby_location_with_dir[1][1]] == self.enemy:
                    robustness -= 1
        return robustness

    def sumito_num_pairs_triplets(self):
        count_sumito = 0
        count_pairs = 0
        count_triplets = 0
        self.state_space.set_player_value(self.ally)
        self.state_space.get_singular_move_resulting_marble_positions_tommy()
        self.state_space.get_double_marble_move_resulting_marble_positions_tommy()
        self.state_space.get_triple_marble_move_resulting_marble_positions_tommy()
        count_sumito += self.state_space.two_to_one_sumito
        count_sumito += self.state_space.three_to_one_sumito
        count_sumito += self.state_space.three_to_two_sumito
        count_pairs += self.state_space.pairs
        count_triplets += self.state_space.triplets
        self.state_space.reset_count()
        self.state_space.set_player_value(self.enemy)
        self.state_space.get_double_marble_move_resulting_marble_positions_tommy()
        self.state_space.get_triple_marble_move_resulting_marble_positions_tommy()
        count_sumito -= self.state_space.two_to_one_sumito
        count_sumito -= self.state_space.three_to_one_sumito
        count_sumito -= self.state_space.three_to_two_sumito
        count_pairs -= self.state_space.pairs
        count_triplets -= self.state_space.triplets
        summation = self.last_coefficients[0] * count_sumito * 5 + self.last_coefficients[1] * count_pairs + \
                    self.last_coefficients[2] * count_triplets * 3
        return summation

    def strengthen_group(self):
        strength_score = 0
        valid_pose = 1
        upper_bound = (BOARD_ARRAY_SIZE - 1) - valid_pose
        lower_bound = valid_pose
        for location in self.ally_pieces_locations:
            x = location[0]
            y = location[1]
            if upper_bound > x > lower_bound and upper_bound > y > lower_bound:
                if self.state[x + 1][y - 1] == self.enemy and self.state[x - 1][y + 1] == self.ally:
                    strength_score += 1
                if self.state[x + 1][y - 1] == self.ally and self.state[x - 1][y + 1] == self.enemy:
                    strength_score += 1

        return strength_score


if __name__ == '__main__':
    # state1 = INITIAL_GAME_BOARD_SETUPS[2]

    # initial_state = INITIAL_GAME_BOARD_SETUPS[0]
    #
    # state_white_win_one = [
    #     [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
    #     [-2, -2, -2, -2, -2, 2, 2, 2, 2, 2, -2],
    #     [-2, -2, -2, -2, 2, 2, 2, 2, 2, -1, -2],
    #     [-2, -2, -2, -1, -1, 2, 2, 2, -1, -1, -2],
    #     [-2, -2, -1, -1, -1, -1, -1, -1, -1, -1, -2],
    #     [-2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2],
    #     [-2, -1, -1, -1, 1, 1, -1, -1, -1, -2, -2],
    #     [-2, -1, -1, 1, -1, -1, -1, -1, -2, -2, -2],
    #     [-2, 1, 1, 1, 1, 1, 1, -2, -2, -2, -2],
    #     [-2, 1, 1, 1, 1, 1, -2, -2, -2, -2, -2],
    #     [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]
    # ]
    #
    # test_list = list()
    # test_list += INITIAL_GAME_BOARD_SETUPS
    # test_list.append(state_white_win_one)
    #
    # for test_index in test_list:
    #     tommy_AI_Evaluation_white = Evaluation(TeamEnum.WHITE, test_index)
    #     print(f" white:  {tommy_AI_Evaluation_white.get_evaluation_score()}")
    #     tommy_AI_Evaluation_black = Evaluation(TeamEnum.BLACK, test_index)
    #     print(f" black:  {tommy_AI_Evaluation_black.get_evaluation_score()}")



    # DEFAULT_MARBLE_POSITION = ['C5b', 'D5b', 'E4b', 'E5b', 'E6b', 'F5b', 'F6b', 'F7b', 'F8b', 'G6b', 'H6b', 'C3w', 'C4w', 'D3w', 'D4w', 'D6w', 'E7w', 'F4w', 'G5w', 'G7w', 'G8w', 'G9w', 'H7w', 'H8w', 'H9w']
    tommy_AI_Evaluation_white = Evaluation(TeamEnum.WHITE, DEFAULT_MARBLE_POSITION)
    print(f" white:  {tommy_AI_Evaluation_white.get_evaluation_score()}")
    tommy_AI_Evaluation_black = Evaluation(TeamEnum.BLACK, DEFAULT_MARBLE_POSITION)
    print(f" black:  {tommy_AI_Evaluation_black.get_evaluation_score()}")