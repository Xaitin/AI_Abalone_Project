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
    n1 = chr(ord(s[0]) + 1) + str(int(s[1]) + 1) + chr(ord(s[3]) + 1) + str(int(s[4]) + 1)
    n2 = s[0] + str(int(s[1]) + 1) + s[3] + str(int(s[4]) + 1)
    n3 = chr(ord(s[0]) - 1) + s[1] + chr(ord(s[3]) - 1) + s[4]
    n4 = chr(ord(s[0]) - 1) + str(int(s[1]) - 1) + chr(ord(s[3]) - 1) + str(int(s[4]) - 1)
    n5 = s[0] + str(int(s[1]) - 1) + s[3] + str(int(s[4]) - 1)
    n6 = chr(ord(s[0]) + 1) + s[1] + chr(ord(s[3]) + 1) + s[4]
    return [n1, n2, n3, n4, n5, n6]


class stateGenerator:
    def __init__(self):
        self.player = None
        self.input_result = list()
        self.board_result = list()
        self.output_moves = list()
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
            print(formatted_pair)
            neighbors = find_paired_neighbors(formatted_pair)
            print(neighbors)

    def find_pairs(self, s):
        pairs = list()
        neighbors = find_neighbors(s)
        for neighbor in neighbors:
            if neighbor + self.player in self.input_result \
                    and neighbor + self.player not in pairs:
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
        output = ""
        for value in self.output_moves:
            output += (str(value) + "\n")
        print(output)

    def make_singular_move(self, target, moving_marble):
        index = self.input_result.index(moving_marble)
        current_pieces = self.input_result.copy()
        current_pieces[index] = target + self.player
        self.output_moves.append(current_pieces)


def main():
    read = stateGenerator()
    read.read_input_data("Test2.input")
    read.find_singular_moves()
    read.find_double_moves()
    # read.read_board_data("Test1.board")


if __name__ == '__main__':
    main()
