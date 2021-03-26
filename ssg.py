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
                self.board_result.append(movements)
            for line in self.board_result:
                print(line)

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

    def write_result_data(self, src, result):
        with open(src, mode='w') as file:
            for line in result:
                _str = ""
                for marble in line:
                    _str += marble + ","
                file.write(_str[:-1] + "\n")

    def generate(self):
        singular_moves = self.state_space.get_singular_move_resulting_marble_positions()
        double_moves = self.state_space.get_double_marble_move_resulting_marble_positions()
        triple_moves = self.state_space.get_triple_marble_move_resulting_marble_positions()
        print("singular:", len(singular_moves), "double:", len(double_moves), "triple:", len(triple_moves))

        return singular_moves + double_moves + triple_moves


def main():
    file_name = "Test1"
    state_space_generator = StateSpaceGenerator()
    state_space_generator.read_input_data(file_name + ".input")
    result = state_space_generator.generate()

    state_space_generator.write_result_data(src=file_name + "_gen" + ".board", result=result)
    #
    # print("result", len(result))
    # for re in result:
    #     # print(re)
    #     _str = ""
    #     for marble in re:
    #         _str += marble + " "
    #     # print(_str)
    #
    # # test with sort----------------------------------------------------------
    # # test_result = read.double_move_states + read.single_move_states
    # # set_result = [sorted(row) for row in test_result]
    # check_answer = StateSpaceGenerator()
    # check_answer.read_board_data(file_name + ".board")
    #
    # # print(len(set(tuple(row) for row in result)))
    # print()
    #
    # count = 0
    # for line in result:
    #     if line not in check_answer.board_result:
    #         count += 1
    #         print(line)
    # print("how many are wrong?", count)
    #
    # count = 0
    # for line in check_answer.board_result:
    #     if line not in result:
    #         count += 1
    #         print(line)
    # print("how many are missing?", count)

    # read.read_board_data("Test1.board")


if __name__ == '__main__':
    main()
