LETTER_SHIFT = 69
NUMBER_SHIFT = 5


class ReadFile:
    def __init__(self):
        self.player = None
        self.input_result = list()
        self.movements = list()
        self.marble_movements = list()
        self.board_result = list()

    def read_board_data(self, src):
        # read lines, read board file
        with open(src, mode='r', encoding='utf-8') as file:
            lines = [line.strip() for line in file]
            for line in lines:
                movements = line.split(',')
                # self.steps.append(self.movement_player_movements(movements))
                self.board_result.append(self.distinct_by_player(movements))

    def read_input_data(self, src):
        # read lines, read input file
        # expected result: [('start player', 'b'), [('b', (0, 2)), ('b', (0, 1)), ('b', (1, 0)), ('b', (0, 0))]}
        with open(src, mode='r', encoding='utf-8') as file:
            lines = [line.strip() for line in file]
            self.player = lines[0]
            self.movements = lines[1].split(',')
            self.input_result.append(("start player", self.player))
            self.input_result.append(self.movement_player_movements(self.movements))
            print(self.input_result)

    # 1st way to read data
    def movement_player_movements(self, movements):
        translate_movements = list()
        # format example: [('b', (0, 2)), ('b', (0, 1)), ('b', (1, 0)), ('b', (0, 0))]
        for movement in movements:
            coord = movement[:-1]
            player = movement[-1]
            translate_movements.append((player, self.translate_coord(coord)))
        return translate_movements

    # 2nd way to read data
    def distinct_by_player(self, movements):
        # format example: result = ([(-1, 2), (0, 1), (-1, 0), (-1, -3)], [(2, 2), (1, 2), (2, 1), (-3, -3), (-4, -3)])
        # result[0]: black, result[1]: white
        black_marble_movements = list()
        white_marble_movements = list()
        for movement in movements:
            coord = movement[:-1]
            player = movement[-1]
            if player == 'b':
                black_marble_movements.append(self.translate_coord(coord))
            else:
                white_marble_movements.append(self.translate_coord(coord))
        return black_marble_movements, white_marble_movements

    @staticmethod
    def translate_coord(coord):
        x = NUMBER_SHIFT - int(coord[1])
        y = LETTER_SHIFT - ord(coord[0])
        return x, y


def main():
    read = ReadFile()
    read.read_input_data("Test1.input")
    # read.read_board_data("Test1.board")


if __name__ == '__main__':
    main()
