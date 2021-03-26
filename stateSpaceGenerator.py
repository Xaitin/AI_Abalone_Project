import string
from ssg import StateSpaceGenerator

TEST_MODE = False


def find_neighbors(s, b):
    if b:
        n1 = chr(ord(s[0]) + 1) + str(int(s[1]) + 1)
        n2 = s[0] + str(int(s[1]) + 1)
        n3 = chr(ord(s[0]) - 1) + s[1]
        n4 = chr(ord(s[0]) - 1) + str(int(s[1]) - 1)
        n5 = s[0] + str(int(s[1]) - 1)
        n6 = chr(ord(s[0]) + 1) + s[1]
        bn1 = chr(ord(s[0]) + 2) + str(int(s[1]) + 2)
        bn2 = s[0] + str(int(s[1]) + 2)
        bn3 = chr(ord(s[0]) - 2) + s[1]
        bn4 = chr(ord(s[0]) - 2) + str(int(s[1]) - 2)
        bn5 = s[0] + str(int(s[1]) - 2)
        bn6 = chr(ord(s[0]) + 2) + s[1]
        return [
            [n1, bn1],
            [n2, bn2],
            [n3, bn3],
            [n4, bn4],
            [n5, bn5],
            [n6, bn6]
        ]
    else:
        n1 = chr(ord(s[0]) + 1) + str(int(s[1]) + 1)
        n2 = s[0] + str(int(s[1]) + 1)
        n3 = chr(ord(s[0]) - 1) + s[1]
        n4 = chr(ord(s[0]) - 1) + str(int(s[1]) - 1)
        n5 = s[0] + str(int(s[1]) - 1)
        n6 = chr(ord(s[0]) + 1) + s[1]
        return [n1, n2, n3, n4, n5, n6]


def find_move_type(groups):
    new_groups = list()
    for s in groups:
        char_coord_m1 = ord(s[0])
        num_coord_m1 = int(s[1])
        char_coord_m2 = ord(s[3])
        num_coord_m2 = int(s[4])
        if char_coord_m1 < char_coord_m2 and num_coord_m1 < num_coord_m2:
            move_direction = 1
        # example E5 and E6
        elif char_coord_m1 == char_coord_m2 and num_coord_m1 < num_coord_m2:
            move_direction = 2
        # example E5 and D5
        elif char_coord_m1 > char_coord_m2 and num_coord_m1 == num_coord_m2:
            move_direction = 3
        # example E5 and D4
        elif char_coord_m1 > char_coord_m2 and num_coord_m1 > num_coord_m2:
            move_direction = 1
        # example E5 and E4
        elif char_coord_m1 == char_coord_m2 and num_coord_m1 > num_coord_m2:
            move_direction = 2
        # example E5 and F5
        elif char_coord_m1 < char_coord_m2 and num_coord_m1 == num_coord_m2:
            move_direction = 3
        else:
            print("Something went wrong!")
            return -1
        new_groups.append(s + str(move_direction))
    return new_groups


def find_paired_neighbors(s):
    char_coord_m1 = ord(s[0])
    num_coord_m1 = int(s[1])
    char_coord_m2 = ord(s[3])
    num_coord_m2 = int(s[4])
    # example E5 and F6
    if char_coord_m1 < char_coord_m2 and num_coord_m1 < num_coord_m2:
        # Searching with F6

        # n1 = G7
        n1 = chr(ord(s[3]) + 1) + str(int(s[4]) + 1)
        # n2 = F7
        n2 = s[3] + str(int(s[4]) + 1)
        # n3 = E6
        n3 = chr(ord(s[3]) - 1) + s[4]
        # n4 = D5
        n4 = chr(ord(s[3]) - 2) + str(int(s[4]) - 1)
        # n5 = D4
        n5 = chr(ord(s[3]) - 2) + str(int(s[4]) - 2)
        # n6 = E4
        n6 = chr(ord(s[3]) - 1) + str(int(s[4]) - 2)
        # n7 = F5
        n7 = s[3] + str(int(s[4]) - 1)
        # n8 = G6
        n8 = chr(ord(s[3]) + 1) + s[4]
        move_direction = 1
    # example E5 and E6
    elif char_coord_m1 == char_coord_m2 and num_coord_m1 < num_coord_m2:
        # Searching with E6

        # n1 = F7
        n1 = chr(ord(s[3]) + 1) + str(int(s[4]) + 1)
        # n2 = E7
        n2 = s[3] + str(int(s[4]) + 1)
        # n3 = D6
        n3 = chr(ord(s[3]) - 1) + s[4]
        # n4 = D5
        n4 = chr(ord(s[3]) - 1) + str(int(s[4]) - 1)
        # n5 = D4
        n5 = chr(ord(s[3]) - 1) + str(int(s[4]) - 2)
        # n6 = E4
        n6 = s[3] + str(int(s[4]) - 2)
        # n7 = F5
        n7 = chr(ord(s[3]) + 1) + str(int(s[4]) - 1)
        # n8 = F6
        n8 = chr(ord(s[3]) + 1) + s[4]
        move_direction = 2
    # example E5 and D5
    elif char_coord_m1 > char_coord_m2 and num_coord_m1 == num_coord_m2:
        # Searching with D5

        # n1 = E6
        n1 = chr(ord(s[3]) + 1) + str(int(s[4]) + 1)
        # n2 = D6
        n2 = s[3] + str(int(s[4]) + 1)
        # n3 = C5
        n3 = chr(ord(s[3]) - 1) + s[4]
        # n4 = C4
        n4 = chr(ord(s[3]) - 1) + str(int(s[4]) - 1)
        # n5 = D4
        n5 = s[3] + str(int(s[4]) - 1)
        # n6 = E4
        n6 = chr(ord(s[3]) + 1) + str(int(s[4]) - 1)
        # n7 = F5
        n7 = chr(ord(s[3]) + 2) + s[4]
        # n8 = F6
        n8 = chr(ord(s[3]) + 2) + str(int(s[4]) + 1)
        move_direction = 3
    # example E5 and D4
    elif char_coord_m1 > char_coord_m2 and num_coord_m1 > num_coord_m2:
        # Searching with D4

        # n1 = F6
        n1 = chr(ord(s[3]) + 2) + str(int(s[4]) + 2)
        # n2 = E6
        n2 = chr(ord(s[3]) + 1) + str(int(s[4]) + 2)
        # n3 = D5
        n3 = s[3] + str(int(s[4]) + 1)
        # n4 = C4
        n4 = chr(ord(s[3]) - 1) + s[4]
        # n5 = C3
        n5 = chr(ord(s[3]) - 1) + str(int(s[4]) - 1)
        # n6 = D3
        n6 = s[3] + str(int(s[4]) - 1)
        # n7 = E4
        n7 = chr(ord(s[3]) + 1) + s[4]
        # n8 = F5
        n8 = chr(ord(s[3]) + 2) + str(int(s[4]) + 1)
        move_direction = 1
    # example E5 and E4
    elif char_coord_m1 == char_coord_m2 and num_coord_m1 > num_coord_m2:
        # Searching with E4

        # n1 = F5
        n1 = chr(ord(s[3]) + 1) + str(int(s[4]) + 1)
        # n2 = F6
        n2 = chr(ord(s[3]) + 1) + str(int(s[4]) + 2)
        # n3 = E6
        n3 = s[3] + str(int(s[4]) + 2)
        # n4 = D5
        n4 = chr(ord(s[3]) - 1) + str(int(s[4]) + 1)
        # n5 = D4
        n5 = chr(ord(s[3]) - 1) + s[4]
        # n6 = D3
        n6 = chr(ord(s[3]) - 1) + str(int(s[4]) - 1)
        # n7 = E3
        n7 = s[3] + str(int(s[4]) - 1)
        # n8 = F4
        n8 = chr(ord(s[3]) + 1) + s[4]
        move_direction = 2
    # example E5 and F5
    elif char_coord_m1 < char_coord_m2 and num_coord_m1 == num_coord_m2:
        # Searching with F5

        # n1 = G6
        n1 = chr(ord(s[3]) + 1) + str(int(s[4]) + 1)
        # n2 = F6
        n2 = s[3] + str(int(s[4]) + 1)
        # n3 = E6
        n3 = chr(ord(s[3]) - 1) + str(int(s[4]) + 1)
        # n4 = D5
        n4 = chr(ord(s[3]) - 2) + s[4]
        # n5 = D4
        n5 = chr(ord(s[3]) - 2) + str(int(s[4]) - 1)
        # n6 = E4
        n6 = chr(ord(s[3]) - 1) + str(int(s[4]) - 1)
        # n7 = F4
        n7 = s[3] + str(int(s[4]) - 1)
        # n8 = G5
        n8 = chr(ord(s[3]) + 1) + s[4]
        move_direction = 3
    else:
        print("Something went wrong!")
        return -1

    return [n1, n2, n3, n4, n5, n6, n7, n8, move_direction]


def find_grouped_neighbors(group):
    char_coord_m1 = ord(group[0])
    num_coord_m1 = int(group[1])
    char_coord_m2 = ord(group[6])
    num_coord_m2 = int(group[7])
    # sample D4 and F6
    if char_coord_m1 < char_coord_m2 and num_coord_m1 < num_coord_m2:
        # Searching with F6

        # n1 = G7
        n1 = chr(ord(group[6]) + 1) + str(int(group[7]) + 1)
        # n2 = F7
        n2 = group[6] + str(int(group[7]) + 1)
        # n3 = E6
        n3 = chr(ord(group[6]) - 1) + group[7]
        # n4 = D5
        n4 = chr(ord(group[6]) - 2) + str(int(group[7]) - 1)
        # n5 = C4
        n5 = chr(ord(group[6]) - 3) + str(int(group[7]) - 2)
        # n6 = C3
        n6 = chr(ord(group[6]) - 3) + str(int(group[7]) - 3)
        # n7 = D3
        n7 = chr(ord(group[6]) - 2) + str(int(group[7]) - 3)
        # n8 = E4
        n8 = chr(ord(group[6]) - 1) + str(int(group[7]) - 2)
        # n9 = F5
        n9 = group[6] + str(int(group[7]) - 1)
        # n10 = G6
        n10 = chr(ord(group[6]) + 1) + group[7]
        move_type = 1
    # example E4 and E6
    elif char_coord_m1 == char_coord_m2 and num_coord_m1 < num_coord_m2:
        # Searching with E6

        # n1 = F7
        n1 = chr(ord(group[6]) + 1) + str(int(group[7]) + 1)
        # n2 = E7
        n2 = group[6] + str(int(group[7]) + 1)
        # n3 = D6
        n3 = chr(ord(group[6]) - 1) + group[7]
        # n4 = D5
        n4 = chr(ord(group[6]) - 1) + str(int(group[7]) - 1)
        # n5 = D4
        n5 = chr(ord(group[6]) - 1) + str(int(group[7]) - 2)
        # n6 = D3
        n6 = chr(ord(group[6]) - 1) + str(int(group[7]) - 3)
        # n7 = E3
        n7 = group[6] + str(int(group[7]) - 3)
        # n8 = F4
        n8 = chr(ord(group[6]) + 1) + str(int(group[7]) - 2)
        # n9 = F5
        n9 = chr(ord(group[6]) + 1) + str(int(group[7]) - 1)
        # n10 = F6
        n10 = chr(ord(group[6]) + 1) + group[7]
        move_type = 2
        # example F5 and D5
    elif char_coord_m1 > char_coord_m2 and num_coord_m1 == num_coord_m2:
        # Searching with D5

        # n1 = E6
        n1 = chr(ord(group[6]) + 1) + str(int(group[7]) + 1)
        # n2 = D6
        n2 = group[6] + str(int(group[7]) + 1)
        # n3 = C5
        n3 = chr(ord(group[6]) - 1) + group[7]
        # n4 = C4
        n4 = chr(ord(group[6]) - 1) + str(int(group[7]) - 1)
        # n5 = D4
        n5 = group[6] + str(int(group[7]) - 1)
        # n6 = E4
        n6 = chr(ord(group[6]) + 1) + str(int(group[7]) - 1)
        # n7 = F4
        n7 = chr(ord(group[6]) + 2) + str(int(group[7]) - 1)
        # n8 = G5
        n8 = chr(ord(group[6]) + 3) + group[7]
        # n9 = F6
        n9 = chr(ord(group[6]) + 2) + str(int(group[7]) + 1)
        # n10 = E6
        n10 = chr(ord(group[6]) + 1) + str(int(group[7]) + 1)
        move_type = 3
        # example F6 and D4
    elif char_coord_m1 > char_coord_m2 and num_coord_m1 > num_coord_m2:
        # Searching with D4

        # n1 = G7
        n1 = chr(ord(group[6]) + 3) + str(int(group[7]) + 3)
        # n2 = F7
        n2 = chr(ord(group[6]) + 2) + str(int(group[7]) + 3)
        # n3 = E6
        n3 = chr(ord(group[6]) + 1) + str(int(group[7]) + 2)
        # n4 = D5
        n4 = group[6] + str(int(group[7]) + 1)
        # n5 = C4
        n5 = chr(ord(group[6]) - 1) + group[7]
        # n6 = C3
        n6 = chr(ord(group[6]) - 1) + str(int(group[7]) - 1)
        # n7 = D3
        n7 = group[6] + str(int(group[7]) - 1)
        # n8 = E4
        n8 = chr(ord(group[6]) + 1) + group[7]
        # n9 = F5
        n9 = chr(ord(group[6]) + 2) + str(int(group[7]) + 1)
        # n10 = G6
        n10 = chr(ord(group[6]) + 3) + str(int(group[7]) + 2)
        move_type = 1
        # example E6 and E4
    elif char_coord_m1 == char_coord_m2 and num_coord_m1 > num_coord_m2:
        # Searching with E4

        # n1 = F7
        n1 = chr(ord(group[6]) + 1) + str(int(group[7]) + 3)
        # n2 = E7
        n2 = group[6] + str(int(group[7]) + 3)
        # n3 = D6
        n3 = chr(ord(group[6]) - 1) + str(int(group[7]) + 2)
        # n4 = D5
        n4 = chr(ord(group[6]) - 1) + str(int(group[7]) + 1)
        # n5 = D4
        n5 = chr(ord(group[6]) - 1) + group[7]
        # n6 = D3
        n6 = chr(ord(group[6]) - 1) + str(int(group[7]) - 1)
        # n7 = E3
        n7 = group[6] + str(int(group[7]) - 1)
        # n8 = F4
        n8 = chr(ord(group[6]) + 1) + group[7]
        # n9 = F5
        n9 = chr(ord(group[6]) + 1) + str(int(group[7]) + 1)
        # n10 = F6
        n10 = chr(ord(group[6]) + 1) + str(int(group[7]) + 2)
        move_type = 2
        # example D5 and F5
    elif char_coord_m1 < char_coord_m2 and num_coord_m1 == num_coord_m2:
        # Searching with F5

        # n1 = E6
        n1 = chr(ord(group[6]) - 1) + str(int(group[7]) + 1)
        # n2 = D6
        n2 = chr(ord(group[6]) - 2) + str(int(group[7]) + 1)
        # n3 = C5
        n3 = chr(ord(group[6]) - 3) + group[7]
        # n4 = C4
        n4 = chr(ord(group[6]) - 3) + str(int(group[7]) - 1)
        # n5 = D4
        n5 = chr(ord(group[6]) - 2) + str(int(group[7]) - 1)
        # n6 = E4
        n6 = chr(ord(group[6]) - 1) + str(int(group[7]) - 1)
        # n7 = F4
        n7 = group[6] + str(int(group[7]) - 1)
        # n8 = G5
        n8 = chr(ord(group[6]) + 1) + group[7]
        # n9 = F6
        n9 = group[6] + str(int(group[7]) + 1)
        # n10 = E6
        n10 = chr(ord(group[6]) - 1) + str(int(group[7]) + 1)
        move_type = 3
    else:
        print("Something went wrong!")
        return -1

    return [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, move_type]


class stateGenerator:
    def __init__(self):
        self.player = None
        self.input_result = list()
        self.board_result = list()
        self.single_move_states = list()
        self.double_move_states = list()
        self.triple_move_states = list()
        self.valid_squares = {"A1", "A2", "A3", "A4", "A5",
                              "B1", "B2", "B3", "B4", "B5", "B6",
                              "C1", "C2", "C3", "C4", "C5", "C6", "C7",
                              "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8",
                              "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9",
                              "F2", "F3", "F4", "F5", "F6", "F7", "F8", "F9",
                              "G3", "G4", "G5", "G6", "G7", "G8", "G9",
                              "H4", "H5", "H6", "H7", "H8", "H9",
                              "I5", "I6", "I7", "I8", "I9"}

    def read_input_data(self, src):
        with open(src, mode='r', encoding='utf-8') as file:
            lines = [line.strip() for line in file]
            self.player = lines[0]
            for line in lines:
                if len(line) > 5:
                    value = line.split(',')
                    self.input_result = value

    def find_double_moves(self):
        paired_selections = list()
        for marble in self.input_result:
            if marble[2] == self.player:
                selections = self.find_pairs(marble)
                for selection in selections:
                    combination1 = [marble + selection]
                    combination2 = [selection + marble]
                    if combination1 not in paired_selections \
                            and combination2 not in paired_selections:
                        paired_selections.append(combination1)
        for pair in paired_selections:
            formatted_pair = str(pair).translate(
                str.maketrans('', '', string.punctuation))
            neighbors = find_paired_neighbors(formatted_pair)
            m1 = formatted_pair[0] + formatted_pair[1]
            m2 = formatted_pair[3] + formatted_pair[4]
            self.attempt_paired_moves(m1, m2, neighbors)
        if TEST_MODE:
            print("\nPrinting Double Moves\n")
        output = ""
        for v in self.double_move_states:
            output += (str(v) + "\n")
        if TEST_MODE:
            print(output)

    def find_triple_moves(self):
        grouped_selections = list()
        for marble in self.input_result:
            if marble[2] == self.player:
                selections = self.find_groups(marble)
                for selection in selections:
                    combinations = [
                        [marble + (selection[0] + self.player) + (selection[1] + self.player)],
                        [marble + (selection[1] + self.player) + (selection[0] + self.player)],
                        [(selection[1] + self.player) + marble + (selection[0] + self.player)],
                        [(selection[0] + self.player) + marble + (selection[1] + self.player)],
                        [(selection[0] + self.player) + (selection[1] + self.player) + marble],
                        [(selection[1] + self.player) + (selection[0] + self.player) + marble]
                    ]
                    exists = True
                    for combination in combinations:
                        if combination[0] in grouped_selections:
                            exists = False
                        m1 = combination[0][0] + combination[0][1]
                        m2 = combination[0][3] + combination[0][4]
                        m3 = combination[0][6] + combination[0][7]
                        if m1 not in self.valid_squares or m2 not in self.valid_squares or m3 not in self.valid_squares:
                            exists = False
                    if exists:
                        grouped_selections.append(combinations[0][0])
        self.attempt_grouped_moves(grouped_selections)
        print("\nPrinting Triple Moves\n")
        output = ""
        for v in self.triple_move_states:
            output += (str(v) + "\n")
        print(output)

    def attempt_grouped_moves(self, groups):
        for group in groups:
            neighbors = find_grouped_neighbors(group)
            move_type = neighbors[10]
            p = self.player
            marble_one = group[0] + group[1]
            marble_two = group[3] + group[4]
            marble_three = group[6] + group[7]
            index_marble_one = self.input_result.index(marble_one + p)
            index_marble_two = self.input_result.index(marble_two + p)
            index_marble_three = self.input_result.index(marble_three + p)
            if p == 'b':
                opponent = 'w'
            else:
                opponent = 'b'
            if move_type == 1:
                upwards_in_line = neighbors[0]
                # if theres an opponent in the way
                if upwards_in_line + opponent in self.input_result:
                    behind_opponent = chr(ord(upwards_in_line[0]) + 1) + str(int(upwards_in_line[1]) + 1)
                    # if theres a friendly marble behind opponent
                    if behind_opponent + self.player in self.input_result:
                        pass
                    # if theres an opponent behind opponent
                    elif behind_opponent + opponent in self.input_result:
                        behind_opponent_2 = chr(ord(upwards_in_line[0]) + 2) + str(int(upwards_in_line[1]) + 2)
                        # if there is 3 opponents lined up
                        if behind_opponent_2 + opponent in self.input_result:
                            pass
                        # only 2 opponent lined up, can push
                        else:
                            index_opponent = self.input_result.index(upwards_in_line + opponent)
                            current_pieces = self.input_result.copy()
                            current_pieces[index_opponent] = chr(ord(upwards_in_line[0]) + 2) + str(int(upwards_in_line[1]) + 2)
                            current_pieces[index_marble_one] = chr(ord(marble_one[0]) + 1) + str(
                                int(marble_one[1]) + 1) + self.player
                            current_pieces[index_marble_two] = chr(ord(marble_two[0]) + 1) + str(
                                int(marble_two[1]) + 1) + self.player
                            current_pieces[index_marble_three] = chr(ord(marble_three[0]) + 1) + str(
                                int(marble_three[1]) + 1) + self.player
                            self.double_move_states.append(self.ten_catch(current_pieces))
                    else:
                        index_opponent = self.input_result.index(upwards_in_line + opponent)
                        current_pieces = self.input_result.copy()
                        current_pieces[index_opponent] = behind_opponent + opponent
                        current_pieces[index_marble_one] = chr(ord(marble_one[0]) + 1) + str(
                            int(marble_one[1]) + 1) + self.player
                        current_pieces[index_marble_two] = chr(ord(marble_two[0]) + 1) + str(
                            int(marble_two[1]) + 1) + self.player
                        current_pieces[index_marble_three] = chr(ord(marble_three[0]) + 1) + str(
                            int(marble_three[1]) + 1) + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))
                # if theres a friendly marble in the way
                elif upwards_in_line + p in self.input_result:
                    pass
                # no marbles in the way
                else:
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = chr(ord(marble_one[0]) + 1) + str(
                        int(marble_one[1]) + 1) + self.player
                    current_pieces[index_marble_two] = chr(ord(marble_two[0]) + 1) + str(
                        int(marble_two[1]) + 1) + self.player
                    current_pieces[index_marble_three] = chr(ord(marble_three[0]) + 1) + str(
                        int(marble_three[1]) + 1) + self.player
                    self.double_move_states.append(self.ten_catch(current_pieces))

                downwards_in_line = neighbors[4]
                # if theres an opponent in the way
                if downwards_in_line + opponent in self.input_result:
                    behind_opponent = chr(ord(downwards_in_line[0]) - 1) + str(int(downwards_in_line[1]) - 1)
                    # if theres a friendly marble behind opponent
                    if behind_opponent + self.player in self.input_result:
                        pass
                    # if theres an opponent behind opponent
                    elif behind_opponent + opponent in self.input_result:
                        behind_opponent_2 = chr(ord(downwards_in_line[0]) - 2) + str(int(downwards_in_line[1]) - 2)
                        # if there is 3 opponents lined up
                        if behind_opponent_2 + opponent in self.input_result:
                            pass
                        # only 2 opponent lined up, can push
                        else:
                            index_opponent = self.input_result.index(downwards_in_line + opponent)
                            current_pieces = self.input_result.copy()
                            current_pieces[index_opponent] = chr(ord(downwards_in_line[0]) - 2) + str(
                                int(downwards_in_line[1]) - 2)
                            current_pieces[index_marble_one] = chr(ord(marble_one[0]) - 1) + str(
                                int(marble_one[1]) - 1) + self.player
                            current_pieces[index_marble_two] = chr(ord(marble_two[0]) - 1) + str(
                                int(marble_two[1]) - 1) + self.player
                            current_pieces[index_marble_three] = chr(ord(marble_three[0]) - 1) + str(
                                int(marble_three[1]) - 1) + self.player
                            self.double_move_states.append(self.ten_catch(current_pieces))
                    else:
                        index_opponent = self.input_result.index(upwards_in_line + opponent)
                        current_pieces = self.input_result.copy()
                        current_pieces[index_opponent] = behind_opponent + opponent
                        current_pieces[index_marble_one] = chr(ord(marble_one[0]) - 1) + str(
                            int(marble_one[1]) - 1) + self.player
                        current_pieces[index_marble_two] = chr(ord(marble_two[0]) - 1) + str(
                            int(marble_two[1]) - 1) + self.player
                        current_pieces[index_marble_three] = chr(ord(marble_three[0]) - 1) + str(
                            int(marble_three[1]) - 1) + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))
                    # if theres a friendly marble in the way
                elif upwards_in_line + p in self.input_result:
                    pass
                    # no marbles in the way
                else:
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = chr(ord(marble_one[0]) - 1) + str(
                        int(marble_one[1]) - 1) + self.player
                    current_pieces[index_marble_two] = chr(ord(marble_two[0]) - 1) + str(
                        int(marble_two[1]) - 1) + self.player
                    current_pieces[index_marble_three] = chr(ord(marble_three[0]) - 1) + str(
                        int(marble_three[1]) - 1) + self.player
                    self.double_move_states.append(self.ten_catch(current_pieces))
                # cant side step to right.
                if neighbors[2] + 'b' in self.input_result or neighbors[2] + 'w' in self.input_result \
                        and neighbors[3] + 'b' in self.input_result or neighbors[3] + 'w' in self.input_result:
                    pass
                else:
                    if neighbors[1] + 'b' in self.input_result or neighbors[1] + 'w' in self.input_result:
                        pass
                    else:
                        # perform side step one
                        current_pieces = self.input_result.copy()
                        current_pieces[index_marble_one] = marble_one[0] + str(int(marble_one[1]) + 1) + self.player
                        current_pieces[index_marble_two] = marble_two[0] + str(int(marble_two[1]) + 1) + self.player
                        current_pieces[index_marble_three] = marble_three[0] + str(int(marble_three[1]) + 1) + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))
                    if neighbors[4] + 'b' in self.input_result or neighbors[4] + 'w' in self.input_result:
                        pass
                    else:
                        # perform side step two
                        current_pieces = self.input_result.copy()
                        current_pieces[index_marble_one] = chr(ord(marble_one[0]) - 1) + marble_one[1] + self.player
                        current_pieces[index_marble_two] = chr(ord(marble_two[0]) - 1) + marble_two[1] + self.player
                        current_pieces[index_marble_three] = chr(ord(marble_three[0]) - 1) + marble_three[1] + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))
                # cant side step to left.
                if neighbors[7] + 'b' in self.input_result or neighbors[7] + 'w' in self.input_result \
                        and neighbors[8] + 'b' in self.input_result or neighbors[8] + 'w' in self.input_result:
                    pass
                else:
                    if neighbors[6] + 'b' in self.input_result or neighbors[6] + 'w' in self.input_result:
                        pass
                    else:
                        # perform side step one
                        current_pieces = self.input_result.copy()
                        current_pieces[index_marble_one] = marble_one[0] + str(int(marble_one[1]) - 1) + self.player
                        current_pieces[index_marble_two] = marble_two[0] + str(int(marble_two[1]) - 1) + self.player
                        current_pieces[index_marble_three] = marble_three[0] + str(int(marble_three[1]) - 1) + self.player
                        self.double_move_states.append(current_pieces)
                    if neighbors[9] + 'b' in self.input_result or neighbors[9] + 'w' in self.input_result:
                        pass
                    else:
                        # perform side step two
                        current_pieces = self.input_result.copy()
                        current_pieces[index_marble_one] = chr(ord(marble_one[0]) + 1) + marble_one[1] + self.player
                        current_pieces[index_marble_two] = chr(ord(marble_two[0]) + 1) + marble_two[1] + self.player
                        current_pieces[index_marble_three] = chr(ord(marble_three[0]) + 1) + marble_three[1] + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))
            elif move_type == 2:
                upwards_in_line = neighbors[1]
                # if theres an opponent in the way
                if upwards_in_line + opponent in self.input_result:
                    behind_opponent = upwards_in_line[0] + str(int(upwards_in_line[1]) + 1)
                    # if theres a friendly marble behind opponent
                    if behind_opponent + self.player in self.input_result:
                        pass
                    # if theres an opponent behind opponent
                    elif behind_opponent + opponent in self.input_result:
                        behind_opponent_2 = upwards_in_line[0] + str(int(upwards_in_line[1]) + 2)
                        # if there is 3 opponents lined up
                        if behind_opponent_2 + opponent in self.input_result:
                            pass
                        # only 2 opponent lined up, can push
                        else:
                            index_opponent = self.input_result.index(upwards_in_line + opponent)
                            current_pieces = self.input_result.copy()
                            current_pieces[index_opponent] = upwards_in_line[0] + str(int(upwards_in_line[1]) + 2)
                            current_pieces[index_marble_one] = marble_one[0] + str(
                                int(marble_one[1]) + 1) + self.player
                            current_pieces[index_marble_two] = marble_two[0] + str(
                                int(marble_two[1]) + 1) + self.player
                            current_pieces[index_marble_three] = marble_three[0] + str(
                                int(marble_three[1]) + 1) + self.player
                            self.double_move_states.append(self.ten_catch(current_pieces))
                    else:
                        index_opponent = self.input_result.index(upwards_in_line + opponent)
                        current_pieces = self.input_result.copy()
                        current_pieces[index_opponent] = behind_opponent + opponent
                        current_pieces[index_marble_one] = marble_one[0] + str(
                            int(marble_one[1]) + 1) + self.player
                        current_pieces[index_marble_two] = marble_two[0] + str(
                            int(marble_two[1]) + 1) + self.player
                        current_pieces[index_marble_three] = marble_three[0] + str(
                            int(marble_three[1]) + 1) + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))
                # if theres a friendly marble in the way
                elif upwards_in_line + p in self.input_result:
                    pass
                # no marbles in the way
                else:
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = marble_one[0] + str(
                        int(marble_one[1]) + 1) + self.player
                    current_pieces[index_marble_two] = marble_two[0] + str(
                        int(marble_two[1]) + 1) + self.player
                    current_pieces[index_marble_three] = marble_three[0] + str(
                        int(marble_three[1]) + 1) + self.player
                    self.double_move_states.append(self.ten_catch(current_pieces))

                downwards_in_line = neighbors[6]
                # if theres an opponent in the way
                if downwards_in_line + opponent in self.input_result:
                    behind_opponent = downwards_in_line[0] + str(int(downwards_in_line[1]) - 1)
                    # if theres a friendly marble behind opponent
                    if behind_opponent + self.player in self.input_result:
                        pass
                    # if theres an opponent behind opponent
                    elif behind_opponent + opponent in self.input_result:
                        behind_opponent_2 = downwards_in_line[0] + str(int(downwards_in_line[1]) - 2)
                        # if there is 3 opponents lined up
                        if behind_opponent_2 + opponent in self.input_result:
                            pass
                        # only 2 opponent lined up, can push
                        else:
                            index_opponent = self.input_result.index(downwards_in_line + opponent)
                            current_pieces = self.input_result.copy()
                            current_pieces[index_opponent] = downwards_in_line[0] + str(
                                int(downwards_in_line[1]) - 2)
                            current_pieces[index_marble_one] = marble_one[0] + str(
                                int(marble_one[1]) - 1) + self.player
                            current_pieces[index_marble_two] = marble_two[0] + str(
                                int(marble_two[1]) - 1) + self.player
                            current_pieces[index_marble_three] = marble_three[0] + str(
                                int(marble_three[1]) - 1) + self.player
                            self.double_move_states.append(self.ten_catch(current_pieces))
                    else:
                        index_opponent = self.input_result.index(upwards_in_line + opponent)
                        current_pieces = self.input_result.copy()
                        current_pieces[index_opponent] = behind_opponent + opponent
                        current_pieces[index_marble_one] = marble_one[0] + str(
                            int(marble_one[1]) - 1) + self.player
                        current_pieces[index_marble_two] = marble_two[0] + str(
                            int(marble_two[1]) - 1) + self.player
                        current_pieces[index_marble_three] = marble_three[0] + str(
                            int(marble_three[1]) - 1) + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))
                    # if theres a friendly marble in the way
                elif upwards_in_line + p in self.input_result:
                    pass
                    # no marbles in the way
                else:
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = marble_one[0] + str(
                        int(marble_one[1]) - 1) + self.player
                    current_pieces[index_marble_two] = marble_two[0] + str(
                        int(marble_two[1]) - 1) + self.player
                    current_pieces[index_marble_three] = marble_three[0] + str(
                        int(marble_three[1]) - 1) + self.player
                    self.double_move_states.append(self.ten_catch(current_pieces))
                # cant side step up.
                if neighbors[8] + 'b' in self.input_result or neighbors[8] + 'w' in self.input_result \
                        and neighbors[9] + 'b' in self.input_result or neighbors[9] + 'w' in self.input_result:
                    pass
                else:
                    if neighbors[0] + 'b' in self.input_result or neighbors[0] + 'w' in self.input_result:
                        pass
                    else:
                        # perform side step one
                        current_pieces = self.input_result.copy()
                        current_pieces[index_marble_one] = chr(ord(marble_one[0]) + 1) + str(int(marble_one[1]) + 1) + self.player
                        current_pieces[index_marble_two] = chr(ord(marble_two[0]) + 1) + str(int(marble_two[1]) + 1) + self.player
                        current_pieces[index_marble_three] = chr(ord(marble_three[0]) + 1) + str(int(marble_three[1]) + 1) + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))
                    if neighbors[7] + 'b' in self.input_result or neighbors[7] + 'w' in self.input_result:
                        pass
                    else:
                        # perform side step two
                        current_pieces = self.input_result.copy()
                        current_pieces[index_marble_one] = chr(ord(marble_one[0]) + 1) + marble_one[1] + self.player
                        current_pieces[index_marble_two] = chr(ord(marble_two[0]) + 1) + marble_two[1] + self.player
                        current_pieces[index_marble_three] = chr(ord(marble_three[0]) + 1) + marble_three[1] + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))
                # cant side step down.
                if neighbors[3] + 'b' in self.input_result or neighbors[3] + 'w' in self.input_result \
                        and neighbors[4] + 'b' in self.input_result or neighbors[4] + 'w' in self.input_result:
                    pass
                else:
                    if neighbors[2] + 'b' in self.input_result or neighbors[2] + 'w' in self.input_result:
                        pass
                    else:
                        # perform side step one
                        current_pieces = self.input_result.copy()
                        current_pieces[index_marble_one] = chr(ord(marble_one[0]) - 1) + marble_one[1] + self.player
                        current_pieces[index_marble_two] = chr(ord(marble_two[0]) - 1) + marble_two[1] + self.player
                        current_pieces[index_marble_three] = chr(ord(marble_three[0]) - 1) + marble_three[1] + self.player
                        self.double_move_states.append(current_pieces)
                    if neighbors[5] + 'b' in self.input_result or neighbors[5] + 'w' in self.input_result:
                        pass
                    else:
                        # perform side step two
                        current_pieces = self.input_result.copy()
                        current_pieces[index_marble_one] = chr(ord(marble_one[0]) - 1) + str(
                            int(marble_one[1]) - 1) + self.player
                        current_pieces[index_marble_two] = chr(ord(marble_two[0]) - 1) + str(
                            int(marble_two[1]) - 1) + self.player
                        current_pieces[index_marble_three] = chr(ord(marble_three[0]) - 1) + str(
                            int(marble_three[1]) - 1) + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))
            elif move_type == 3:
                upwards_in_line = neighbors[9]
                # if theres an opponent in the way
                if upwards_in_line + opponent in self.input_result:
                    behind_opponent = chr(ord(upwards_in_line[0]) + 1) + upwards_in_line[1]
                    # if theres a friendly marble behind opponent
                    if behind_opponent + self.player in self.input_result:
                        pass
                    # if theres an opponent behind opponent
                    elif behind_opponent + opponent in self.input_result:
                        behind_opponent_2 = chr(ord(upwards_in_line[0]) + 2) + upwards_in_line[1]
                        # if there is 3 opponents lined up
                        if behind_opponent_2 + opponent in self.input_result:
                            pass
                        # only 2 opponent lined up, can push
                        else:
                            index_opponent = self.input_result.index(upwards_in_line + opponent)
                            current_pieces = self.input_result.copy()
                            current_pieces[index_opponent] = chr(ord(upwards_in_line[0]) + 2) + upwards_in_line[1]
                            current_pieces[index_marble_one] = chr(ord(marble_one[0]) + 1) + marble_one[1] + self.player
                            current_pieces[index_marble_two] = chr(ord(marble_two[0]) + 1) + marble_two[1] + self.player
                            current_pieces[index_marble_three] = chr(ord(marble_three[0]) + 1) + marble_three[1] + self.player
                            self.double_move_states.append(self.ten_catch(current_pieces))
                    else:
                        index_opponent = self.input_result.index(upwards_in_line + opponent)
                        current_pieces = self.input_result.copy()
                        current_pieces[index_opponent] = behind_opponent + opponent
                        current_pieces[index_marble_one] = chr(ord(marble_one[0]) + 1) + marble_one[1] + self.player
                        current_pieces[index_marble_two] = chr(ord(marble_two[0]) + 1) + marble_two[1] + self.player
                        current_pieces[index_marble_three] = chr(ord(marble_three[0]) + 1) + marble_three[1] + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))
                # if theres a friendly marble in the way
                elif upwards_in_line + p in self.input_result:
                    pass
                # no marbles in the way
                else:
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = chr(ord(marble_one[0]) + 1) + marble_one[1] + self.player
                    current_pieces[index_marble_two] = chr(ord(marble_two[0]) + 1) + marble_two[1] + self.player
                    current_pieces[index_marble_three] = chr(ord(marble_three[0]) + 1) + marble_three[1] + self.player
                    self.double_move_states.append(self.ten_catch(current_pieces))

                downwards_in_line = neighbors[4]
                # if theres an opponent in the way
                if downwards_in_line + opponent in self.input_result:
                    behind_opponent = chr(ord(downwards_in_line[0]) - 1) + downwards_in_line[1]
                    # if theres a friendly marble behind opponent
                    if behind_opponent + self.player in self.input_result:
                        pass
                    # if theres an opponent behind opponent
                    elif behind_opponent + opponent in self.input_result:
                        behind_opponent_2 = chr(ord(downwards_in_line[0]) - 2) + downwards_in_line[1]
                        # if there is 3 opponents lined up
                        if behind_opponent_2 + opponent in self.input_result:
                            pass
                        # only 2 opponent lined up, can push
                        else:
                            index_opponent = self.input_result.index(downwards_in_line + opponent)
                            current_pieces = self.input_result.copy()
                            current_pieces[index_opponent] = chr(ord(downwards_in_line[0]) - 2) + downwards_in_line[1]
                            current_pieces[index_marble_one] = chr(ord(marble_one[0]) - 1) + marble_one[1] + self.player
                            current_pieces[index_marble_two] = chr(ord(marble_two[0]) - 1) + marble_two[1] + self.player
                            current_pieces[index_marble_three] = chr(ord(marble_three[0]) - 1) + marble_three[1] + self.player
                            self.double_move_states.append(self.ten_catch(current_pieces))
                    else:
                        index_opponent = self.input_result.index(upwards_in_line + opponent)
                        current_pieces = self.input_result.copy()
                        current_pieces[index_opponent] = behind_opponent + opponent
                        current_pieces[index_marble_one] = chr(ord(marble_one[0]) - 1) + marble_one[1] + self.player
                        current_pieces[index_marble_two] = chr(ord(marble_two[0]) - 1) + marble_two[1] + self.player
                        current_pieces[index_marble_three] = chr(ord(marble_three[0]) - 1) + marble_three[1] + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))
                    # if theres a friendly marble in the way
                elif upwards_in_line + p in self.input_result:
                    pass
                    # no marbles in the way
                else:
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = chr(ord(marble_one[0]) - 1) + marble_one[1] + self.player
                    current_pieces[index_marble_two] = chr(ord(marble_two[0]) - 1) + marble_two[1] + self.player
                    current_pieces[index_marble_three] = chr(ord(marble_three[0]) - 1) + str(
                        int(marble_three[1]) - 1) + self.player
                    self.double_move_states.append(self.ten_catch(current_pieces))
                # cant side step to right.
                if neighbors[2] + 'b' in self.input_result or neighbors[2] + 'w' in self.input_result \
                        and neighbors[3] + 'b' in self.input_result or neighbors[3] + 'w' in self.input_result:
                    pass
                else:
                    if neighbors[1] + 'b' in self.input_result or neighbors[1] + 'w' in self.input_result:
                        pass
                    else:
                        # perform side step one
                        current_pieces = self.input_result.copy()
                        current_pieces[index_marble_one] = marble_one[0] + str(int(marble_one[1]) + 1) + self.player
                        current_pieces[index_marble_two] = marble_two[0] + str(int(marble_two[1]) + 1) + self.player
                        current_pieces[index_marble_three] = marble_three[0] + str(
                            int(marble_three[1]) + 1) + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))
                    if neighbors[4] + 'b' in self.input_result or neighbors[4] + 'w' in self.input_result:
                        pass
                    else:
                        # perform side step two
                        current_pieces = self.input_result.copy()
                        current_pieces[index_marble_one] = chr(ord(marble_one[0]) - 1) + marble_one[1] + self.player
                        current_pieces[index_marble_two] = chr(ord(marble_two[0]) - 1) + marble_two[1] + self.player
                        current_pieces[index_marble_three] = chr(ord(marble_three[0]) - 1) + marble_three[
                            1] + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))
                # cant side step to left.
                if neighbors[7] + 'b' in self.input_result or neighbors[7] + 'w' in self.input_result \
                        and neighbors[8] + 'b' in self.input_result or neighbors[8] + 'w' in self.input_result:
                    pass
                else:
                    if neighbors[6] + 'b' in self.input_result or neighbors[6] + 'w' in self.input_result:
                        pass
                    else:
                        # perform side step one
                        current_pieces = self.input_result.copy()
                        current_pieces[index_marble_one] = marble_one[0] + str(int(marble_one[1]) - 1) + self.player
                        current_pieces[index_marble_two] = marble_two[0] + str(int(marble_two[1]) - 1) + self.player
                        current_pieces[index_marble_three] = marble_three[0] + str(
                            int(marble_three[1]) - 1) + self.player
                        self.double_move_states.append(current_pieces)
                    if neighbors[9] + 'b' in self.input_result or neighbors[9] + 'w' in self.input_result:
                        pass
                    else:
                        # perform side step two
                        current_pieces = self.input_result.copy()
                        current_pieces[index_marble_one] = chr(ord(marble_one[0]) + 1) + marble_one[1] + self.player
                        current_pieces[index_marble_two] = chr(ord(marble_two[0]) + 1) + marble_two[1] + self.player
                        current_pieces[index_marble_three] = chr(ord(marble_three[0]) + 1) + marble_three[
                            1] + self.player
                        self.double_move_states.append(self.ten_catch(current_pieces))

    def find_groups(self, s):
        pairs = list()
        neighbors = find_neighbors(s, True)
        for neighbor in neighbors:
            all_neighbors_friendly = False
            for n in neighbor:
                if n in self.valid_squares \
                        and n + self.player in self.input_result:
                    all_neighbors_friendly = True
            if all_neighbors_friendly:
                pairs.append(neighbor)
        return pairs

    def find_pairs(self, s):
        pairs = list()
        neighbors = find_neighbors(s, False)
        for neighbor in neighbors:
            if neighbor + self.player in self.input_result \
                    and neighbor + self.player not in pairs \
                    and neighbor in self.valid_squares:
                pairs.append(neighbor + self.player)
        return pairs

    def is_valid_square(self, square_str):
        return square_str in self.valid_squares

    def attempt_paired_moves(self, m1, m2, neighbors):
        p = self.player
        marble_one = m1
        marble_two = m2
        index_marble_one = self.input_result.index(marble_one + p)
        index_marble_two = self.input_result.index(marble_two + p)
        if p == 'b':
            opponent = 'w'
        else:
            opponent = 'b'
        move_type = neighbors[8]
        # neighbors at indexes 0 and 4 are always in-line. Other neighbors are side-step
        if move_type == 1:
            upwards_in_line = neighbors[0]
            if not self.is_valid_square(upwards_in_line):
                return
            # if theres an opponent in the way
            if upwards_in_line + opponent in self.input_result:
                behind_opponent = chr(
                    ord(upwards_in_line[0]) + 1) + str(int(upwards_in_line[1]) + 1)
                # if the opponent has 2 marbles in this line
                if behind_opponent + opponent in self.input_result or behind_opponent + self.player in self.input_result:
                    pass
                else:
                    index_opponent = self.input_result.index(
                        upwards_in_line + opponent)
                    current_pieces = self.input_result.copy()
                    current_pieces[index_opponent] = behind_opponent + opponent
                    current_pieces[index_marble_one] = chr(ord(marble_one[0]) + 1) + str(
                        int(marble_one[1]) + 1) + self.player
                    current_pieces[index_marble_two] = chr(ord(marble_two[0]) + 1) + str(
                        int(marble_two[1]) + 1) + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))
            # if theres a friendly marble in the way
            elif upwards_in_line + p in self.input_result:
                pass
            # no marbles in the way
            else:
                current_pieces = self.input_result.copy()
                current_pieces[index_marble_one] = chr(ord(marble_one[0]) + 1) + str(
                    int(marble_one[1]) + 1) + self.player
                current_pieces[index_marble_two] = chr(ord(marble_two[0]) + 1) + str(
                    int(marble_two[1]) + 1) + self.player
                self.double_move_states.append(self.ten_catch(current_pieces))

            downwards_in_line = neighbors[4]
            if not self.is_valid_square(downwards_in_line):
                return
            # if theres an opponent in the way
            if downwards_in_line + opponent in self.input_result:
                behind_opponent = chr(
                    ord(downwards_in_line[0]) - 1) + str(int(downwards_in_line[1]) - 1)
                # if the opponent has 2 marbles in this line
                if behind_opponent + opponent in self.input_result or behind_opponent + self.player in self.input_result:
                    pass
                else:
                    index_opponent = self.input_result.index(
                        downwards_in_line + opponent)
                    current_pieces = self.input_result.copy()
                    current_pieces[index_opponent] = behind_opponent + opponent
                    current_pieces[index_marble_one] = chr(ord(marble_one[0]) - 1) + str(
                        int(marble_one[1]) - 1) + self.player
                    current_pieces[index_marble_two] = chr(ord(marble_two[0]) - 1) + str(
                        int(marble_two[1]) - 1) + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))
            # if theres a friendly marble in the way
            elif downwards_in_line + p in self.input_result:
                pass
            # no marbles in the way
            else:
                current_pieces = self.input_result.copy()
                current_pieces[index_marble_one] = chr(ord(marble_one[0]) - 1) + str(
                    int(marble_one[1]) - 1) + self.player
                current_pieces[index_marble_two] = chr(ord(marble_two[0]) - 1) + str(
                    int(marble_two[1]) - 1) + self.player
                self.double_move_states.append(self.ten_catch(current_pieces))

            ### Side-step movements
            # cant side step to right.
            if neighbors[2] + 'b' in self.input_result or neighbors[2] + 'w' in self.input_result or not self.is_valid_square(neighbors[2]):
                pass
            else:
                if neighbors[1] + 'b' in self.input_result or neighbors[1] + 'w' in self.input_result or not self.is_valid_square(neighbors[1]):
                    pass
                else:
                    # perform side step one
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = marble_one[0] + \
                        str(int(marble_one[1]) + 1) + self.player
                    current_pieces[index_marble_two] = marble_two[0] + \
                        str(int(marble_two[1]) + 1) + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))
                if neighbors[3] + 'b' in self.input_result or neighbors[3] + 'w' in self.input_result or not self.is_valid_square(neighbors[3]):
                    pass
                else:
                    # perform side step two
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = chr(
                        ord(marble_one[0]) - 1) + marble_one[1] + self.player
                    current_pieces[index_marble_two] = chr(
                        ord(marble_two[0]) - 1) + marble_two[1] + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))
            # cant side step to left.
            if neighbors[6] + 'b' in self.input_result or neighbors[6] + 'w' in self.input_result or not self.is_valid_square(neighbors[6]):
                pass
            else:
                if neighbors[5] + 'b' in self.input_result or neighbors[5] + 'w' in self.input_result or not self.is_valid_square(neighbors[5]):
                    pass
                else:
                    # perform side step one
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = marble_one[0] + \
                        str(int(marble_one[1]) - 1) + self.player
                    current_pieces[index_marble_two] = marble_two[0] + \
                        str(int(marble_two[1]) - 1) + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))
                if neighbors[7] + 'b' in self.input_result or neighbors[7] + 'w' in self.input_result or not self.is_valid_square(neighbors[7]):
                    pass
                else:
                    # perform side step two
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = chr(
                        ord(marble_one[0]) + 1) + marble_one[1] + self.player
                    current_pieces[index_marble_two] = chr(
                        ord(marble_two[0]) + 1) + marble_two[1] + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))

        # neighbors at indexes 1 and 5 are always in-line. Other neighbors are side-step
        elif move_type == 2:
            right_in_line = neighbors[1]
            if not self.is_valid_square(right_in_line):
                return
            if right_in_line + opponent in self.input_result:
                behind_opponent = right_in_line[0] + \
                    str(int(right_in_line[1]) + 1)
                # if the opponent has 2 marbles in this line
                if behind_opponent + opponent in self.input_result or behind_opponent + self.player in self.input_result:
                    pass
                else:
                    index_opponent = self.input_result.index(
                        right_in_line + opponent)
                    current_pieces = self.input_result.copy()
                    current_pieces[index_opponent] = behind_opponent + opponent
                    current_pieces[index_marble_one] = marble_one[0] + \
                        str(int(marble_one[1]) + 1) + self.player
                    current_pieces[index_marble_two] = marble_two[0] + \
                        str(int(marble_two[1]) + 1) + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))
            # if theres a friendly marble in the way
            elif right_in_line + p in self.input_result:
                pass
            # no marbles in the way
            else:
                current_pieces = self.input_result.copy()
                current_pieces[index_marble_one] = marble_one[0] + \
                    str(int(marble_one[1]) + 1) + self.player
                current_pieces[index_marble_two] = marble_two[0] + \
                    str(int(marble_two[1]) + 1) + self.player
                self.double_move_states.append(self.ten_catch(current_pieces))

            left_in_line = neighbors[5]
            if not self.is_valid_square(left_in_line):
                return
            if left_in_line + opponent in self.input_result:
                behind_opponent = left_in_line[0] + \
                    str(int(left_in_line[1]) - 1)
                # if the opponent has 2 marbles in this line
                if behind_opponent + opponent in self.input_result or behind_opponent + self.player in self.input_result:
                    pass
                else:
                    index_opponent = self.input_result.index(
                        left_in_line + opponent)
                    current_pieces = self.input_result.copy()
                    current_pieces[index_opponent] = behind_opponent + opponent
                    current_pieces[index_marble_one] = marble_one[0] + \
                        str(int(marble_one[1]) - 1) + self.player
                    current_pieces[index_marble_two] = marble_two[0] + \
                        str(int(marble_two[1]) - 1) + self.player
                    self.double_move_states.append(
                        self.ten_catch(self.ten_catch(current_pieces)))
            # if theres a friendly marble in the way
            elif left_in_line + p in self.input_result:
                pass
            # no marbles in the way
            else:
                current_pieces = self.input_result.copy()
                current_pieces[index_marble_one] = marble_one[0] + \
                    str(int(marble_one[1]) - 1) + self.player
                current_pieces[index_marble_two] = marble_two[0] + \
                    str(int(marble_two[1]) - 1) + self.player
                self.double_move_states.append(self.ten_catch(current_pieces))

            ### Side-step movements
            # cant side step up.
            if neighbors[7] + 'b' in self.input_result or neighbors[7] + 'w' in self.input_result or not self.is_valid_square(neighbors[7]):
                pass
            else:
                if neighbors[0] + 'b' in self.input_result or neighbors[0] + 'w' in self.input_result or not self.is_valid_square(neighbors[0]):
                    pass
                else:
                    # perform side step one
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = chr(ord(marble_one[0]) + 1) + str(
                        int(marble_one[1]) + 1) + self.player
                    current_pieces[index_marble_two] = chr(ord(marble_two[0]) + 1) + str(
                        int(marble_two[1]) + 1) + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))
                if neighbors[6] + 'b' in self.input_result or neighbors[6] + 'w' in self.input_result or not self.is_valid_square(neighbors[6]):
                    pass
                else:
                    # perform side step two
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = chr(
                        ord(marble_one[0]) + 1) + marble_one[1] + self.player
                    current_pieces[index_marble_two] = chr(
                        ord(marble_two[0]) + 1) + marble_two[1] + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))
            # cant side step down.
            if neighbors[3] + 'b' in self.input_result or neighbors[3] + 'w' in self.input_result or not self.is_valid_square(neighbors[3]):
                pass
            else:
                if neighbors[4] + 'b' in self.input_result or neighbors[4] + 'w' in self.input_result or not self.is_valid_square(neighbors[4]):
                    pass
                else:
                    # perform side step one
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = chr(ord(marble_one[0]) - 1) + str(
                        int(marble_one[1]) - 1) + self.player
                    current_pieces[index_marble_two] = chr(ord(marble_two[0]) - 1) + str(
                        int(marble_two[1]) - 1) + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))
                if neighbors[2] + 'b' in self.input_result or neighbors[2] + 'w' in self.input_result or not self.is_valid_square(neighbors[2]):
                    pass
                else:
                    # perform side step two
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = chr(
                        ord(marble_one[0]) - 1) + marble_one[1] + self.player
                    current_pieces[index_marble_two] = chr(
                        ord(marble_two[0]) - 1) + marble_two[1] + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))
        # neighbors at indexes 4 and 7 are always in-line. Other neighbors are side-step
        elif move_type == 3:

            # Upwards in-line movements
            upwards_in_line = neighbors[7]
            if not self.is_valid_square(upwards_in_line):
                return
            # if theres an opponent in the way
            if upwards_in_line + opponent in self.input_result:
                behind_opponent = chr(
                    ord(upwards_in_line[0]) + 1) + upwards_in_line[1]
                # if the opponent has 2 marbles in this line
                if behind_opponent + opponent in self.input_result or behind_opponent + self.player in self.input_result:
                    pass
                else:
                    index_opponent = self.input_result.index(
                        upwards_in_line + opponent)
                    current_pieces = self.input_result.copy()
                    current_pieces[index_opponent] = behind_opponent + opponent
                    current_pieces[index_marble_one] = chr(
                        ord(marble_one[0]) + 1) + marble_one[1] + self.player
                    current_pieces[index_marble_two] = chr(
                        ord(marble_two[0]) + 1) + marble_two[1] + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))
            # if theres a friendly marble in the way
            elif upwards_in_line + p in self.input_result:
                pass
            # no marbles in the way
            else:
                current_pieces = self.input_result.copy()
                current_pieces[index_marble_one] = chr(
                    ord(marble_one[0]) + 1) + marble_one[1] + self.player
                current_pieces[index_marble_two] = chr(
                    ord(marble_two[0]) + 1) + marble_two[1] + self.player
                self.double_move_states.append(self.ten_catch(current_pieces))

            # Downwards in-line movements
            downwards_in_line = neighbors[3]
            if not self.is_valid_square(downwards_in_line):
                return
            # if theres an opponent in the way
            if downwards_in_line + opponent in self.input_result:
                behind_opponent = chr(
                    ord(downwards_in_line[0]) - 1) + downwards_in_line[1]
                # if the opponent has 2 marbles in this line
                if behind_opponent + opponent in self.input_result or behind_opponent + self.player in self.input_result:
                    pass
                else:
                    index_opponent = self.input_result.index(
                        downwards_in_line + opponent)
                    current_pieces = self.input_result.copy()
                    current_pieces[index_opponent] = behind_opponent + opponent
                    current_pieces[index_marble_one] = chr(
                        ord(marble_one[0]) - 1) + marble_one[1] + self.player
                    current_pieces[index_marble_two] = chr(
                        ord(marble_two[0]) - 1) + marble_two[1] + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))
            # if theres a friendly marble in the way
            elif downwards_in_line + p in self.input_result:
                pass
            # no marbles in the way
            else:
                current_pieces = self.input_result.copy()
                current_pieces[index_marble_one] = chr(
                    ord(marble_one[0]) - 1) + marble_one[1] + self.player
                current_pieces[index_marble_two] = chr(
                    ord(marble_two[0]) - 1) + marble_two[1] + self.player
                self.double_move_states.append(self.ten_catch(current_pieces))

            # Side-step movements
            # cant side step to right.
            if neighbors[1] + 'b' in self.input_result or neighbors[1] + 'w' in self.input_result or not self.is_valid_square(neighbors[1]):
                pass
            else:
                if neighbors[0] + 'b' in self.input_result or neighbors[0] + 'w' in self.input_result or not self.is_valid_square(neighbors[0]):
                    pass
                else:
                    # perform side step one
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = chr(ord(marble_one[0]) + 1) + str(
                        int(marble_one[1]) + 1) + self.player
                    current_pieces[index_marble_two] = chr(ord(marble_two[0]) + 1) + str(
                        int(marble_two[1]) + 1) + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))

                if neighbors[2] + 'b' in self.input_result or neighbors[2] + 'w' in self.input_result or not self.is_valid_square(neighbors[2]):
                    pass
                else:
                    # perform side step two
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = marble_one[0] + str(
                        int(marble_one[1]) + 1) + self.player
                    current_pieces[index_marble_two] = marble_two[0] + str(
                        int(marble_two[1]) + 1) + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))

            # cant side step to left.
            if neighbors[6] + 'b' in self.input_result or neighbors[6] + 'w' in self.input_result or not self.is_valid_square(neighbors[6]):
                pass
            else:
                if neighbors[5] + 'b' in self.input_result or neighbors[5] + 'w' in self.input_result or not self.is_valid_square(neighbors[5]):
                    pass
                else:
                    # perform side step one
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = marble_one[0] + \
                        str(int(marble_one[1]) - 1) + self.player
                    current_pieces[index_marble_two] = marble_two[0] + \
                        str(int(marble_two[1]) - 1) + self.player
                    self.double_move_states.append(current_pieces)
                if neighbors[7] + 'b' in self.input_result or neighbors[7] + 'w' in self.input_result or not self.is_valid_square(neighbors[7]):
                    pass
                else:
                    # perform side step two
                    current_pieces = self.input_result.copy()
                    current_pieces[index_marble_one] = chr(
                        ord(marble_one[0]) + 1) + marble_one[1] + self.player
                    current_pieces[index_marble_two] = chr(
                        ord(marble_two[0]) + 1) + marble_two[1] + self.player
                    self.double_move_states.append(
                        self.ten_catch(current_pieces))

    def ten_catch(self, current_pieces):
        for piece in current_pieces:
            if '10' in piece:
                current_pieces.remove(piece)
        return current_pieces

    def find_singular_moves(self):
        for marble in self.input_result:
            if marble[2] == self.player:
                neighbors = find_neighbors(marble, False)
                for neighbor in neighbors:
                    if neighbor in self.valid_squares and neighbor + 'b' not in self.input_result \
                            and neighbor + 'w' not in self.input_result:
                        self.make_singular_move(neighbor, marble)
        # Formatting output of singular moves.
        output = ""
        for value in self.single_move_states:
            output += (str(value) + "\n")
        # print(output)

    def make_singular_move(self, target, moving_marble):
        index = self.input_result.index(moving_marble)
        current_pieces = self.input_result.copy()
        current_pieces[index] = target + self.player
        self.single_move_states.append(current_pieces)


def main():
    file_name = "Test1"
    read = stateGenerator()
    read.read_input_data(file_name + ".input")
    read.find_singular_moves()
    read.find_double_moves()
    read.find_triple_moves()

    # test with set
    test_result = read.double_move_states + read.single_move_states
    set_result = [sorted(row) for row in test_result]
    check_answer = StateSpaceGenerator()
    check_answer.read_board_data(file_name + ".board")
    check_answer_set = [sorted(row) for row in check_answer.board_result]
    # print(len(set(tuple(row) for row in test_result)))
    print("-" * 20)
    count = 0

    print("result:")
    for line in test_result:
        print(line)
    print("\n\n\n\n")

    print("answer:")
    for line in check_answer_set:
        print(line)
    print("\n\n\n\n")

    for line in check_answer_set:
        if line not in set_result:
            count += 1
            print(line)
    print(count)

    with open(file_name + "_generated" + ".board", mode='w') as file:
        for result in test_result:
            file.write(str(result))
            file.write('\n')


if __name__ == '__main__':
    main()
