import string


def find_neighbors(s):
    n1 = chr(ord(s[0]) + 1) + str(int(s[1]) + 1)
    n2 = s[0] + str(int(s[1]) + 1)
    n3 = chr(ord(s[0]) - 1) + s[1]
    n4 = chr(ord(s[0]) - 1) + str(int(s[1]) - 1)
    n5 = s[0] + str(int(s[1]) - 1)
    n6 = chr(ord(s[0]) + 1) + s[1]
    return [n1, n2, n3, n4, n5, n6]


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


class stateGenerator:
    def __init__(self):
        self.player = None
        self.input_result = list()
        self.board_result = list()
        self.single_move_states = list()
        self.double_move_states = list()
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
                    string = line.split(',')
                    self.input_result = string

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
            formatted_pair = str(pair).translate(str.maketrans('', '', string.punctuation))
            neighbors = find_paired_neighbors(formatted_pair)
            print(neighbors)
            m1 = formatted_pair[0] + formatted_pair[1]
            m2 = formatted_pair[3] + formatted_pair[4]
            self.attempt_paired_moves(m1, m2, neighbors)
        print("\nPrinting Double Moves\n")
        output = ""
        for v in self.double_move_states:
            output += (str(v) + "\n")
        print(output)

    def attempt_paired_moves(self, m1, m2, neighbors):
        marble_one = m1 + self.player
        marble_two = m2 + self.player
        move_type = neighbors[8]
        # neighbors at indexes 0 and 4 are always in-line. Other neighbors are side-step
        if move_type == 1:
            upwards_in_line = neighbors[0]
            downwards_in_line = neighbors[4]
        # neighbors at indexes 1 and 5 are always in-line. Other neighbors are side-step
        elif move_type == 2:
            right_in_line = neighbors[1]
            left_in_line = neighbors[5]
        # neighbors at indexes 4 and 7 are always in-line. Other neighbors are side-step
        elif move_type == 3:
            upwards_in_line = neighbors[7]
            downwards_in_line = neighbors[4]

    def find_pairs(self, s):
        pairs = list()
        neighbors = find_neighbors(s)
        for neighbor in neighbors:
            if neighbor + self.player in self.input_result \
                    and neighbor + self.player not in pairs \
                    and neighbor in self.valid_squares:
                pairs.append(neighbor + self.player)
        return pairs

    def find_singular_moves(self):
        for marble in self.input_result:
            if marble[2] == self.player:
                neighbors = find_neighbors(marble)
                for neighbor in neighbors:
                    if neighbor in self.valid_squares and neighbor + 'b' not in self.input_result \
                            and neighbor + 'w' not in self.input_result:
                        self.make_singular_move(neighbor, marble)
        # Formatting output of singular moves.
        output = ""
        for value in self.single_move_states:
            output += (str(value) + "\n")
        print(output)

    def make_singular_move(self, target, moving_marble):
        index = self.input_result.index(moving_marble)
        current_pieces = self.input_result.copy()
        current_pieces[index] = target + self.player
        self.single_move_states.append(current_pieces)


def main():
    read = stateGenerator()
    read.read_input_data("Test2.input")
    read.find_singular_moves()
    read.find_double_moves()
    # read.read_board_data("Test1.board")


if __name__ == '__main__':
    main()
