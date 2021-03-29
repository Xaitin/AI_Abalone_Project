import copy
import itertools
from operator import add

from constants import EMPTY_GAME_BOARD_ARRAY, EMPTY_SPOT_VALUE, OUTSIDE_OF_THE_BOARD_VALUE, DIRECTION_VECTORS_2D, \
    BOARD_ARRAY_SIZE, DEFAULT_MARBLE_POSITION
from coordinate_helper import CoordinateHelper
from direction_helper import DirectionHelper
from move import Move
from move_type import MoveType
from position import Position
from team_enum import TeamEnum


class StateSpace:
    def __init__(self, marble_positions=DEFAULT_MARBLE_POSITION, player='b'):
        self.moves_list = []
        self.marble_positions = [Position(TeamEnum.BLACK if position[0] == 'b' else TeamEnum.WHITE, position[1]) for
                                 position in
                                 self.read_position_strings(marble_positions)]
        self.player_of_turn = TeamEnum.BLACK if player == 'b' else TeamEnum.WHITE
        self.marble_positions_2d = self.to_2d_array(self.marble_positions)
        self.two_to_one_sumito = 0
        self.three_to_one_sumito = 0
        self.three_to_two_sumito = 0
        self.pairs = 0
        self.triplets = 0
        self.player_value = None



    def reset_count(self):
        self.two_to_one_sumito = 0
        self.three_to_one_sumito = 0
        self.three_to_two_sumito = 0
        self.pairs = 0
        self.triplets = 0

    def set_marble_positions_2d(self, marble_positions_2d):
        self.marble_positions_2d = marble_positions_2d

    def set_player_value(self, player_value):
        self.player_value = player_value

    def get_ally_position(self, state):
        ally_pieces_locations = []
        for j in range(BOARD_ARRAY_SIZE):
            for i in range(BOARD_ARRAY_SIZE):
                if state[i][j] == self.player_value:
                    ally_pieces_locations.append((i, j))

        return ally_pieces_locations

    def get_singular_move_resulting_marble_positions_tommy(self):
        resulting_marble_positions = []
        self.ally_positions = self.get_ally_position(self.marble_positions_2d)
        for position_2d in self.ally_positions:
            surroundings = copy.deepcopy(self.get_surrounding_dir_positions(position_2d=position_2d))
            for dir, spot in surroundings:
                spot_val = self.marble_positions_2d[spot[0]][spot[1]]
                if spot_val == EMPTY_SPOT_VALUE:
                    move, new_state, new_marble_positions = None, None, None
                    move = Move(move_type=MoveType.InLine, spots=[position_2d], direction=dir)
                    self.moves_list.append(move.__str__())
                    # new_state = after move, new self.marble_positions_2d
                    new_state = copy.deepcopy(self.generate_new_state_after_move(move))
                    resulting_marble_positions.append(new_state)
                else:
                    pass
        return resulting_marble_positions

    def get_double_marble_move_resulting_marble_positions_tommy(self):
        resulting_marble_positions = []
        self.ally_positions = self.get_ally_position(self.marble_positions_2d)
        for position_2d in self.ally_positions:
            first_marble_pos_2d = position_2d
            surroundings = copy.deepcopy(self.get_surrounding_dir_positions(first_marble_pos_2d))

            for dir, second_marble_pos_2d in surroundings:
                second_x, second_y = second_marble_pos_2d

                # Pair matched between first_marble <-> pos
                if self.marble_positions_2d[second_x][second_y] == self.player_value:
                    self.pairs += 1
                    in_line_result_state, side_step_result_states = None, None
                    in_line_result_state = copy.deepcopy(
                        self.generate_double_in_line_moves_result_states(first_marble_pos_2d,
                                                                         second_marble_pos_2d,
                                                                         dir))
                    if in_line_result_state is not None:
                        resulting_marble_positions.append(in_line_result_state)
                    side_step_result_states = copy.deepcopy(self.generate_side_step_moves_result_states(
                        marble_positions=[first_marble_pos_2d, second_marble_pos_2d],
                        direction_vector=dir))
                    if side_step_result_states is not None:
                        resulting_marble_positions += side_step_result_states
        return resulting_marble_positions

    def get_triple_marble_move_resulting_marble_positions_tommy(self):
        resulting_marble_positions = []
        self.ally_positions = self.get_ally_position(self.marble_positions_2d)
        for position in self.ally_positions:
            first_marble_pos_2d = position
            surroundings = copy.deepcopy(self.get_surrounding_dir_positions(first_marble_pos_2d))
            for dir, second_marble_pos_2d in surroundings:
                second_x, second_y = second_marble_pos_2d
                third_marble_pos_2d = third_x, third_y = tuple(map(add, second_marble_pos_2d, dir))
                # Pair matched between first_marble <-> pos
                if self.marble_positions_2d[second_x][second_y] == self.player_value \
                        and self.marble_positions_2d[third_x][third_y] == self.player_value:
                    self.triplets += 1
                    in_line_result_state, side_step_result_states = None, None
                    in_line_result_state = copy.deepcopy(
                        self.generate_triple_in_line_moves_result_states(first_marble_pos_2d, second_marble_pos_2d,
                                                                         third_marble_pos_2d, dir))
                    if in_line_result_state is not None:
                        resulting_marble_positions.append(in_line_result_state)
                    side_step_result_states = copy.deepcopy(self.generate_side_step_moves_result_states(
                        marble_positions=[first_marble_pos_2d, second_marble_pos_2d, third_marble_pos_2d],
                        direction_vector=dir))
                    if side_step_result_states is not None:
                        resulting_marble_positions += side_step_result_states
        return resulting_marble_positions

    def generate_all_possible_move_2d(self):
        result = self.get_singular_move_resulting_marble_positions_tommy()
        result += self.get_double_marble_move_resulting_marble_positions_tommy()
        result += self.get_triple_marble_move_resulting_marble_positions_tommy()
        return result

    def get_singular_move_resulting_marble_positions(self):
        resulting_marble_positions = []

        for index, position in enumerate(self.marble_positions):
            if position.team != self.player_of_turn:
                continue
            position_cube = position.get_position()
            position_2d = CoordinateHelper.fromCubeto2DArray(position_cube, with_gutter=True)
            surroundings = copy.deepcopy(self.get_surrounding_dir_positions(position_2d=position_2d))
            for dir, spot in surroundings:
                spot_val = self.marble_positions_2d[spot[0]][spot[1]]
                if spot_val == EMPTY_SPOT_VALUE:
                    move, new_state, new_marble_positions = None, None, None
                    move = Move(move_type=MoveType.InLine, spots=[position_2d], direction=dir)
                    self.moves_list.append(move.__str__())
                    # new_state = after move, new self.marble_positions_2d
                    new_state = copy.deepcopy(self.generate_new_state_after_move(move))
                    new_marble_positions = copy.deepcopy(self.to_marble_position_list(new_state))
                    resulting_marble_positions.append(new_marble_positions)
                else:
                    pass

        resulting_marble_positions.sort()
        return list(k for k, _ in itertools.groupby(resulting_marble_positions))

    def get_double_marble_move_resulting_marble_positions(self):
        resulting_marble_positions = []

        for first_marble in self.marble_positions:
            if first_marble.team != self.player_of_turn:
                continue

            first_marble_pos = first_marble.position
            first_marble_pos_2d = CoordinateHelper.fromCubeto2DArray(first_marble_pos, with_gutter=True)
            print("fromCubeto2DArray", first_marble_pos_2d)
            surroundings = copy.deepcopy(self.get_surrounding_dir_positions(first_marble_pos_2d))

            for dir, second_marble_pos_2d in surroundings:
                second_x, second_y = second_marble_pos_2d
                # Pair matched between first_marble <-> pos
                if self.marble_positions_2d[second_x][second_y] == self.player_of_turn.value:
                    in_line_result_state, side_step_result_states = None, None
                    in_line_result_state = copy.deepcopy(
                        self.generate_double_in_line_moves_result_states(first_marble_pos_2d,
                                                                         second_marble_pos_2d,
                                                                         dir))

                    side_step_result_states = copy.deepcopy(self.generate_side_step_moves_result_states(
                        marble_positions=[first_marble_pos_2d, second_marble_pos_2d],
                        direction_vector=dir))
                    print("side_step_result_states", side_step_result_states)
                    if in_line_result_state is not None:
                        resulting_marble_positions.append(self.to_marble_position_list(in_line_result_state))
                    if side_step_result_states is not None:
                        resulting_marble_positions += [self.to_marble_position_list(state) for state in
                                                       side_step_result_states]

        return resulting_marble_positions

    def get_triple_marble_move_resulting_marble_positions(self):
        resulting_marble_positions = []

        for first_marble in self.marble_positions:
            if first_marble.team != self.player_of_turn:
                continue

            first_marble_pos = first_marble.position
            first_marble_pos_2d = CoordinateHelper.fromCubeto2DArray(first_marble_pos, with_gutter=True)
            surroundings = copy.deepcopy(self.get_surrounding_dir_positions(first_marble_pos_2d))

            for dir, second_marble_pos_2d in surroundings:
                second_x, second_y = second_marble_pos_2d
                third_marble_pos_2d = third_x, third_y = tuple(map(add, second_marble_pos_2d, dir))
                # Pair matched between first_marble <-> pos
                if self.marble_positions_2d[second_x][second_y] == self.player_of_turn.value \
                        and self.marble_positions_2d[third_x][third_y] == self.player_of_turn.value:
                    in_line_result_state, side_step_result_states = None, None
                    in_line_result_state = copy.deepcopy(
                        self.generate_triple_in_line_moves_result_states(first_marble_pos_2d, second_marble_pos_2d,
                                                                         third_marble_pos_2d, dir))
                    if in_line_result_state is not None:
                        resulting_marble_positions.append(self.to_marble_position_list(in_line_result_state))

                    side_step_result_states = copy.deepcopy(self.generate_side_step_moves_result_states(
                        marble_positions=[first_marble_pos_2d, second_marble_pos_2d, third_marble_pos_2d],
                        direction_vector=dir))
                    if side_step_result_states is not None:
                        resulting_marble_positions += [self.to_marble_position_list(state) for state in
                                                       side_step_result_states]

        return resulting_marble_positions

    def generate_double_in_line_moves_result_states(self, first_marble_pos: (int, int), second_marble_pos: (int, int),
                                                    direction_vector: (int, int)):
        """
        In-line moves with double-marble.
        :param second_marble_pos:
        :param first_marble_pos:
        :param direction_vector:
        :return:
        """
        ally_value = int(self.marble_positions_2d[first_marble_pos[0]][first_marble_pos[1]])
        next_spot = tuple(map(add, second_marble_pos, direction_vector))
        next_spot_val = int(self.marble_positions_2d[next_spot[0]][next_spot[1]])
        move = None

        if next_spot_val == ally_value:
            # This becomes triple-marble movement
            pass

        elif next_spot_val == EMPTY_GAME_BOARD_ARRAY:
            move = Move(move_type=MoveType.InLine, spots=[first_marble_pos, second_marble_pos],
                        direction=direction_vector)
            self.moves_list.append(move.__str__())
            return copy.deepcopy(self.generate_new_state_after_move(move))

        elif next_spot_val == OUTSIDE_OF_THE_BOARD_VALUE:
            # You can't move outside of the game board
            pass

        else:
            # This means enemy marble is on the next spot
            next_next_spot = tuple(map(add, next_spot, direction_vector))
            next_next_spot_val = int(self.marble_positions_2d[next_next_spot[0]][next_next_spot[1]])

            if next_next_spot_val == ally_value:
                # When enemy marble is sandwiched by ally marbles.
                # You can't push them all together
                pass

            elif next_next_spot_val == EMPTY_SPOT_VALUE:
                # We can push the enemy marble a spot
                self.two_to_one_sumito += 1

                move = Move(move_type=MoveType.InLine, spots=[first_marble_pos, second_marble_pos, next_spot],
                            direction=direction_vector)
                self.moves_list.append(move.__str__())
                return copy.deepcopy(self.generate_new_state_after_move(move))

            elif next_next_spot_val == OUTSIDE_OF_THE_BOARD_VALUE:
                # We're kicking you out, you enemy
                self.two_to_one_sumito += 1
                # We're not putting the enemy marble's spot in the move as it's going to be kicked out of the board.
                move = Move(move_type=MoveType.InLine, spots=[first_marble_pos, second_marble_pos],
                            direction=direction_vector)
                self.moves_list.append(move.__str__())
                return copy.deepcopy(self.generate_new_state_after_move(move))

            else:
                # You can't move 2 enemy marbles with double marbles.
                pass

    def generate_triple_in_line_moves_result_states(self, first_marble_pos, second_marble_pos,
                                                    third_marble_pos, direction_vector):
        """
        In-line moves with triple-marble.
        :param second_marble_pos:
        :param first_marble_pos:
        :param direction_vector:
        :return:
        """
        ally_value = int(self.marble_positions_2d[first_marble_pos[0]][first_marble_pos[1]])
        next_spot = tuple(map(add, third_marble_pos, direction_vector))
        next_spot_val = int(self.marble_positions_2d[next_spot[0]][next_spot[1]])
        move = None

        if next_spot_val == ally_value:
            # No move possible for 4 marbles.
            pass

        elif next_spot_val == EMPTY_GAME_BOARD_ARRAY:
            move = Move(move_type=MoveType.InLine, spots=[first_marble_pos, second_marble_pos, third_marble_pos],
                        direction=direction_vector)
            self.moves_list.append(move.__str__())
            return copy.deepcopy(self.generate_new_state_after_move(move))

        elif next_spot_val == OUTSIDE_OF_THE_BOARD_VALUE:
            # You can't move outside of the game board
            pass

        else:
            # This means one enemy marble is on the next spot
            next_next_spot = tuple(map(add, next_spot, direction_vector))
            next_next_spot_val = int(self.marble_positions_2d[next_next_spot[0]][next_next_spot[1]])

            if next_next_spot_val == ally_value:
                # When enemy marble is sandwiched by ally marbles.
                # You can't push them all together
                pass

            elif next_next_spot_val == EMPTY_SPOT_VALUE:
                # We can push the enemy marble a spot
                self.three_to_one_sumito += 1

                move = Move(move_type=MoveType.InLine,
                            spots=[first_marble_pos, second_marble_pos, third_marble_pos, next_spot],
                            direction=direction_vector)
                self.moves_list.append(move.__str__())
                return copy.deepcopy(self.generate_new_state_after_move(move))

            elif next_next_spot_val == OUTSIDE_OF_THE_BOARD_VALUE:
                # We're kicking you out, you enemy
                self.three_to_one_sumito += 1

                # We're not putting the enemy marble's spot in the move as it's going to be kicked out of the board.
                move = Move(move_type=MoveType.InLine, spots=[first_marble_pos, second_marble_pos, third_marble_pos],
                            direction=direction_vector)
                self.moves_list.append(move.__str__())
                return copy.deepcopy(self.generate_new_state_after_move(move))

            else:
                # This means two enemy marbles are on the next and next_next spots
                # For Three player, this has to be elaborated more.
                next_next_next_spot = tuple(map(add, next_next_spot, direction_vector))
                next_next_next_spot_val = int(self.marble_positions_2d[next_next_next_spot[0]][next_next_next_spot[1]])
                if next_next_next_spot_val == ally_value:
                    # When enemy marbles are sandwiched by ally marble.
                    # You can't push them all together
                    pass

                elif next_next_next_spot_val == EMPTY_SPOT_VALUE:
                    # We can push the enemy marbles a spot
                    self.three_to_two_sumito += 1

                    move = Move(move_type=MoveType.InLine,
                                spots=[first_marble_pos, second_marble_pos, third_marble_pos, next_spot,
                                       next_next_spot],
                                direction=direction_vector)
                    self.moves_list.append(move.__str__())
                    return copy.deepcopy(self.generate_new_state_after_move(move))

                elif next_next_next_spot_val == OUTSIDE_OF_THE_BOARD_VALUE:
                    # Out of two enemy marbles, the last one will be fall out of the board.
                    self.three_to_two_sumito += 1

                    # We're not putting the last enemy marble's spot in the move as it's going to be kicked out of the board.
                    move = Move(move_type=MoveType.InLine,
                                spots=[first_marble_pos, second_marble_pos, third_marble_pos, next_spot],
                                direction=direction_vector)
                    self.moves_list.append(move.__str__())
                    return copy.deepcopy(self.generate_new_state_after_move(move))

                else:
                    pass

    def generate_side_step_moves_result_states(self, marble_positions: [(int, int)],
                                               direction_vector: (int, int)):
        left_positions = []
        left_common_positions = []
        left_directions = DirectionHelper.get_left_directions(direction_vector)
        new_result_states = []

        # Checking only left direction because it'll be checked from the other side too.
        for dir in left_directions:
            all_empty = True
            left_positions = [tuple(map(add, pos, dir)) for pos in marble_positions]

            for pos in left_positions:
                all_empty = all_empty and (self.marble_positions_2d[pos[0]][pos[1]] == EMPTY_SPOT_VALUE)

            if all_empty:
                move = Move(move_type=MoveType.SideStep, spots=marble_positions, direction=dir)
                self.moves_list.append(move.__str__())
                new_result_states.append(copy.deepcopy(self.generate_new_state_after_move(move)))

        return new_result_states

    def generate_new_state_after_move(self, move: Move) -> [[int]]:
        new_state = copy.deepcopy(self.marble_positions_2d)
        # first element in the first spot = the first marble
        # last element in the last spot = the last marble
        spots = move.get_spots()
        new_spots = [tuple(map(add, sp, move.direction)) for sp in spots]
        prev_x, prev_y, new_x, new_y = int(), int(), int(), int()

        if move.get_move_type() == MoveType.InLine:
            for index in reversed(range(len(spots))):
                prev_x, prev_y = spots[index]
                new_x, new_y = new_spots[index]
                new_state[new_x][new_y] = int(self.marble_positions_2d[prev_x][prev_y])

            # in-line-movement makes an empty spot after moving
            new_state[prev_x][prev_y] = EMPTY_SPOT_VALUE
            return new_state


        else:
            for index in range(len(spots)):
                prev_x, prev_y = spots[index]
                new_x, new_y = new_spots[index]
                new_state[new_x][new_y] = self.marble_positions_2d[prev_x][prev_y]
                new_state[prev_x][prev_y] = EMPTY_SPOT_VALUE
            return new_state

    def is_friendly_marble_spots(self, position_cube):
        position_2d = CoordinateHelper.fromCubeto2DArray(position_cube, with_gutter=True)

        if self.marble_positions_2d[position_2d[0]][position_2d[1]] == self.player_of_turn.value:
            return True
        else:
            return False

    def is_empty_spot(self, position_2d, position_cube=None):
        if position_cube is not None:
            position_2d = CoordinateHelper.fromCubeto2DArray(position_cube, with_gutter=True)

        if self.marble_positions_2d[position_2d[0]][position_2d[1]] == EMPTY_SPOT_VALUE:
            return True
        else:
            return False

    def get_surrounding_dir_positions(self, position_2d):
        surrounding_positions_2d = []
        for direction in DIRECTION_VECTORS_2D:
            surrounding_positions_2d.append((direction, tuple(map(add, position_2d, direction))))

        return surrounding_positions_2d

    def get_state_value_by_cube_pos(self, pos, state=None):
        pos_2d = CoordinateHelper.fromCubeto2DArray(pos, with_gutter=True)
        if state == None:
            return self.marble_positions_2d[pos_2d[0]][pos_2d[1]]
        return state[pos_2d[0]][pos_2d[1]]

    def set_state_value_by_cube_pos(self, pos, new_val, state=None):
        pos_2d = CoordinateHelper.fromCubeto2DArray(pos, with_gutter=True)
        if state == None:
            self.marble_positions_2d[pos_2d[0]][pos_2d[1]] = new_val
        state[pos_2d[0]][pos_2d[1]] = new_val

    def read_position_strings(self, position_strings):
        translate_movements = list()
        # format example: [('b', (0, 2)), ('b', (0, 1)), ('b', (1, 0)), ('b', (0, 0))]
        for position_string in position_strings:
            player = position_string[-1]
            coord = position_string[:-1]
            translate_movements.append((player, CoordinateHelper.from_cube_str_to_cube(coord)))
        return translate_movements

    def to_2d_array(self, marble_positions):
        result_array = EMPTY_GAME_BOARD_ARRAY
        for position in marble_positions:
            array_position_row, array_position_col = CoordinateHelper.fromCubeto2DArray(position.get_position(),
                                                                                        with_gutter=True)
            result_array[array_position_row][array_position_col] = position.get_team().value

        # print(result_array)
        # print(TEST_1_INPUT)
        # print(result_array == TEST_1_INPUT)
        return result_array

    def to_marble_position_list(self, marble_positions_2d):
        black_marble_position_list = []
        white_marble_position_list = []
        length = len(marble_positions_2d)

        for i in reversed(range(length)):
            for j in range(length):
                value = marble_positions_2d[i][j]
                if value != EMPTY_SPOT_VALUE and value != OUTSIDE_OF_THE_BOARD_VALUE:
                    if value == TeamEnum.BLACK.value:
                        cube_vector = CoordinateHelper.from2DArraytoCube((i, j))
                        cube_str = CoordinateHelper.from_cube_to_cube_str(cube_vector)
                        black_marble_position_list.append(cube_str + 'b')
                    elif value == TeamEnum.WHITE.value:
                        cube_vector = CoordinateHelper.from2DArraytoCube((i, j))
                        cube_str = CoordinateHelper.from_cube_to_cube_str(cube_vector)
                        white_marble_position_list.append(cube_str + 'w')

        return black_marble_position_list + white_marble_position_list

    def __str__(self):
        return f"\nPlayer of the turn : {self.player_of_turn}\n" \
               f"Marble Positions: {self.marble_positions}\n"

    def get_move_list(self):
        # print(self.moves_list)
        return self.moves_list
