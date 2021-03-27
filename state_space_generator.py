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
        """
        Reads Test.board for testing purposes.
        :param src: Test.board file name
        :return: none
        """
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
        """
        Reads the Test.input file for the marbles' current positions (state_space).
        :param src: Test.input file name
        :return: none
        """
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
        """
        Formats the resulting board state output and writes to file.
        :param src:  file name
        :param result: board_state list
        :return: none
        """
        with open(src, mode='w') as file:
            for line in result:
                _str = ""
                for marble in line:
                    _str += marble + ","
                file.write(_str[:-1] + "\n")

    def write_move_result_data(self, src, result):
        """
        Formats the moves taken and writes to file.
        :param src: file name
        :param result: move_list list
        :return: none
        """
        with open(src, mode='w') as file:
            for line in result:
                # _str = "" + line
                file.write(line + "\n")

    def generate_resulting_board_states(self):
        """
        Generates all the single, double and triple marble movements and gives their resulting board states.
        :return: combined list of all resulting board states
        """
        singular_moves = self.state_space.get_singular_move_resulting_marble_positions()
        double_moves = self.state_space.get_double_marble_move_resulting_marble_positions()
        triple_moves = self.state_space.get_triple_marble_move_resulting_marble_positions()
        print("singular:", len(singular_moves), "double:", len(double_moves), "triple:", len(triple_moves))

        return singular_moves + double_moves + triple_moves

    @staticmethod
    def check_board_answer(result, file_name):
        print("result", len(result))
        for re in result:
            # print(re)
            _str = ""
            for marble in re:
                _str += marble + " "
            # print(_str)

        # test with sort----------------------------------------------------------
        # test_result = read.double_move_states + read.single_move_states
        # set_result = [sorted(row) for row in test_result]
        check_answer = StateSpaceGenerator()
        check_answer.read_board_data(file_name.replace("Given", "Static") + ".board")

        # print(len(set(tuple(row) for row in result)))
        print()

        count = 0
        for line in result:
            if line not in check_answer.board_result:
                count += 1
                print(line)
        print("how many are wrong?", count)

        count = 0
        for line in check_answer.board_result:
            if line not in result:
                count += 1
                print(line)
        print("how many are missing?", count)

        # read.read_board_data("StaticTest1.board")


def main():

    # Instantiates a StateSpaceGenerator and generates resulting board state based on given Test.input file.
    state_space_generator = StateSpaceGenerator()
    success = True
    while success:
        try:
            # Asks for Test.input file name without extension here.
            file_name = input("Please enter the name of the input file without the extension (e.g. Test1): ")
            state_space_generator.read_input_data(file_name + ".input")
            success = False
        except FileNotFoundError as e:
            print(f"{e}")
    result = state_space_generator.generate_resulting_board_states()

    # Writes Test.board and Test.move output files.
    state_space_generator.write_result_data(src=file_name + ".board", result=result)
    state_space_generator.write_move_result_data(src=file_name + ".move",
                                                 result=state_space_generator.state_space.get_move_list())

    # state_space_generator.check_board_answer(result, file_name)


if __name__ == '__main__':
    main()
