from state_space import StateSpace


class StateSpaceGenerator:
    def __init__(self):
        # self.player = None
        # self.input_result = list()
        self.marble_positions = list()
        self.marble_movements = list()
        self.board_result = list()
        self.state_space = None

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
            player = lines[0]
            marble_positions = lines[1].split(',')
            # self.input_result.append(("player_of_the_turn", self.player))
            # self.input_result.append(self.movement_player_movements(self.marble_positions))
            # print(self.input_result)
            self.state_space = StateSpace(marble_positions, player)
            print(self.state_space)


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

    def generate(self):
        result_marble_positions = []
        result_marble_positions += self.state_space.get_singular_move_resulting_marble_positions()



        return result_marble_positions




def main():
    stateSpaceGenerator = StateSpaceGenerator()
    stateSpaceGenerator.read_input_data("Test1.input")
    result = stateSpaceGenerator.generate()
    print("result", len(result))
    for re in result:
        print(re)

    # read.read_board_data("Test1.board")


if __name__ == '__main__':
    main()
