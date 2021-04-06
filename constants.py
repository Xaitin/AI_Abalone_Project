""" Ints """

HEIGHT_HEADER_FOOTER, GAMEBOARD_SIZE = 100, 500
WIDTH_SIDEBAR = 300
WINDOW_WIDTH, WINDOW_HEIGHT = GAMEBOARD_SIZE + 2 * WIDTH_SIDEBAR, GAMEBOARD_SIZE + 2 * HEIGHT_HEADER_FOOTER
PANEL_WIDTH, PANEL_HEIGHT = 220, 440
INPUT_BOX_WIDTH, INPUT_BOX_DISTANCE_FROM_CENTER = 100, 200
PANEL_DISTANCE_FROM_CENTER = 500
# x, y, z limits
BOARD_SIZE = 4
HEXAGON_SIDE_LENGTH = 30
MARBLE_SIZE = 40
BOARD_IMAGE_SIZE = HEXAGON_SIDE_LENGTH * 22

BUTTON_DISTANCE_1 = 150
BUTTON_DISTANCE_2 = 250
BUTTON_DISTANCE_3 = 350

TITLE_FONT_SIZE = 40
TITLE_DISTANCE_TOP = 50
SMALL_FONT_SIZE = 15

""" Floats """
COS30 = 0.8660254037844386
COS60 = 0.5
SIN30 = COS60
SIN60 = COS30

""" Coordinate Conversion """
LETTER_SHIFT = ord('E')
NUMBER_SHIFT = 5

""" Directions """
DIRECTION_VECTORS_CUBE = [(1, -1), (1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1)]
DIRECTION_VECTORS_2D = [(-1, 1), (0, 1), (1, 0), (1, -1), (0, -1), (-1, 0)]

""" Colors """
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
BOARD_COLOR = (132, 152, 191)
HEXAGON_OUTLINE_COLOR = (193, 199, 217)
SELECTED_HEXAGON_COLOR = (79, 99, 140)
WHITE_HEX = "'#FFFFFF'"
BLUE_HEX = "'#0000FF'"
BLACK_HEX = "'#000000'"
UI_TEXT_COLOR = WHITE_HEX
UI_TEXT_BG_COLOR = BLACK_HEX

""" Path """
WHITE_MARBLE_PATH = "drawables/white_marble.png"
BLACK_MARBLE_PATH = "drawables/black_marble.png"

""" Game Board States """
EMPTY_SPOT_VALUE = -1
OUTSIDE_OF_THE_BOARD_VALUE = -2

"""Invalid Position -2, Valid Empty position: -1, white marbles: 1, black marbles: 2"""
INITIAL_GAME_BOARD_STATE_DEFAULT = [
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
    [-2, -2, -2, -2, -2, 1, 1, 1, 1, 1, -2],
    [-2, -2, -2, -2, 1, 1, 1, 1, 1, 1, -2],
    [-2, -2, -2, -1, -1, 1, 1, 1, -1, -1, -2],
    [-2, -2, -1, -1, -1, -1, -1, -1, -1, -1, -2],
    [-2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2],
    [-2, -1, -1, -1, -1, -1, -1, -1, -1, -2, -2],
    [-2, -1, -1, 2, 2, 2, -1, -1, -2, -2, -2],
    [-2, 2, 2, 2, 2, 2, 2, -2, -2, -2, -2],
    [-2, 2, 2, 2, 2, 2, -2, -2, -2, -2, -2],
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]
]
INITIAL_GAME_BOARD_STATE_BELGIAN = [
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
    [-2, -2, -2, -2, -2, 1, 1, -1, 2, 2, -2],
    [-2, -2, -2, -2, 1, 1, 1, 2, 2, 2, -2],
    [-2, -2, -2, -1, 1, 1, -1, 2, 2, -1, -2],
    [-2, -2, -1, -1, -1, -1, -1, -1, -1, -1, -2],
    [-2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2],
    [-2, -1, -1, -1, -1, -1, -1, -1, -1, -2, -2],
    [-2, -1, 2, 2, -1, 1, 1, -1, -2, -2, -2],
    [-2, 2, 2, 2, 1, 1, 1, -2, -2, -2, -2],
    [-2, 2, 2, -1, 1, 1, -2, -2, -2, -2, -2],
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]
]

INITIAL_GAME_BOARD_STATE_GERMAN = [
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
    [-2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -2],
    [-2, -2, -2, -2, 1, 1, -1, -1, 2, 2, -2],
    [-2, -2, -2, 1, 1, 1, -1, 2, 2, 2, -2],
    [-2, -2, -1, 1, 1, -1, -1, 2, 2, -1, -2],
    [-2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2],
    [-2, -1, 2, 2, -1, -1, 1, 1, -1, -2, -2],
    [-2, 2, 2, 2, -1, 1, 1, 1, -2, -2, -2],
    [-2, 2, 2, -1, -1, 1, 1, -2, -2, -2, -2],
    [-2, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2],
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]
]

INITIAL_GAME_BOARD_SETUPS = [
    INITIAL_GAME_BOARD_STATE_DEFAULT,
    INITIAL_GAME_BOARD_STATE_GERMAN,
    INITIAL_GAME_BOARD_STATE_BELGIAN
]

EMPTY_GAME_BOARD_ARRAY = [
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
    [-2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -2],
    [-2, -2, -2, -2, -1, -1, -1, -1, -1, -1, -2],
    [-2, -2, -2, -1, -1, -1, -1, -1, -1, -1, -2],
    [-2, -2, -1, -1, -1, -1, -1, -1, -1, -1, -2],
    [-2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2],
    [-2, -1, -1, -1, -1, -1, -1, -1, -1, -2, -2],
    [-2, -1, -1, -1, -1, -1, -1, -1, -2, -2, -2],
    [-2, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2],
    [-2, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2],
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]
]

TEST_1_INPUT = [
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
    [-2, -2, -2, -2, -2, -1, -1, -1, -1, -1, -2],
    [-2, -2, -2, -2, -1, -1, 2, 1, 1, 1, -2],
    [-2, -2, -2, -1, -1, 1, 2, 1, 1, 1, -2],
    [-2, -2, -1, -1, 1, 2, 2, 2, 2, -1, -2],
    [-2, -1, -1, -1, 2, 2, 2, 1, -1, -1, -2],
    [-2, -1, -1, 1, 1, 2, 1, -1, -1, -2, -2],
    [-2, -1, -1, 1, 1, 2, -1, -1, -2, -2, -2],
    [-2, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2],
    [-2, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2],
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]
]

LOSE_MARBLE_NUM = 9

BOARD_ARRAY_SIZE = 11
FDZ = -10
SDZ = -5

DANGER_ZONE_INDICATOR = [
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
    [-2, -2, -2, -2, -2, FDZ, FDZ, FDZ, FDZ, FDZ, -2],
    [-2, -2, -2, -2, FDZ, SDZ, SDZ, SDZ, SDZ, FDZ, -2],
    [-2, -2, -2, FDZ, SDZ, 0, 0, 0, SDZ, FDZ, -2],
    [-2, -2, FDZ, SDZ, 0, 0, 0, 0, SDZ, FDZ, -2],
    [-2, FDZ, SDZ, 0, 0, 0, 0, 0, SDZ, FDZ, -2],
    [-2, FDZ, SDZ, 0, 0, 0, 0, SDZ, FDZ, -2, -2],
    [-2, FDZ, SDZ, 0, 0, 0, SDZ, FDZ, -2, -2, -2],
    [-2, FDZ, SDZ, SDZ, SDZ, SDZ, FDZ, -2, -2, -2, -2],
    [-2, FDZ, FDZ, FDZ, FDZ, FDZ, -2, -2, -2, -2, -2],
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2]
]

MANHATTAN_WEIGHT = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 0],
    [0, 0, 0, 1, 2, 3, 3, 2, 1, 0, 0],
    [0, 0, 1, 2, 3, 4, 3, 2, 1, 0, 0],
    [0, 0, 1, 2, 3, 3, 2, 1, 0, 0, 0],
    [0, 0, 1, 2, 2, 2, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]


DEFAULT_MARBLE_POSITION = ['C5b', 'D5b', 'E4b', 'E5b', 'E6b', 'F5b', 'F6b', 'F7b', 'F8b', 'G6b', 'H6b', 'C3w', 'C4w', 'D3w', 'D4w', 'D6w', 'E7w', 'F4w', 'G5w', 'G7w', 'G8w', 'G9w', 'H7w', 'H8w', 'H9w']
STANDARD_MARBLE_POSITION = ['A1b', 'A2b', 'A3b', 'A4b', 'A5b', 'B1b', 'B2b', 'B3b', 'B5b', 'B6b', 'C3b', 'C4b', 'C5b', 'G5w', 'G6w', 'G7w', 'H4w', 'H5w', 'H6w', 'H7w', 'H9w', 'I5w', 'I6w', 'I7w', 'I8w', 'I9w']

FRIENDLY_SQUARE_VALUES = {
    "I5": -100, "I6": -100, "I7": -100, "I8": -100, "I9": -100,
    "H4": -100, "H5": 0, "H6": 0, "H7": 0, "H8": 0, "H9": -100,
    "G3": -100, "G4": 0, "G5": 10, "G6": 10, "G7": 10, "G8": 0, "G9": -100,
    "F2": -100, "F3": 0, "F4": 10, "F5": 30, "F6": 30, "F7": 10, "F8": 0, "F9": -100,
    "E1": -100, "E2": 0, "E3": 10, "E4": 30, "E5": 50, "E6": 30, "E7": 10, "E8": 0, "E9": -100,
    "D1": -100, "D2": 0, "D3": 10, "D4": 30, "D5": 30, "D6": 10, "D7": 0, "D8": -100,
    "C1": -100, "C2": 0, "C3": 10, "C4": 10, "C5": 10, "C6": 0, "C7": -100,
    "B1": -100, "B2": 0, "B3": 0, "B4": 0, "B5": 0, "B6": -100,
    "A1": -100, "A2": -100, "A3": -100, "A4": -100, "A5": -100
}

ENEMY_SQUARE_VALUES = {
    "I5": 100, "I6": 100, "I7": 100, "I8": 100, "I9": 100,
    "H4": 100, "H5": 60, "H6": 60, "H7": 60, "H8": 60, "H9": 100,
    "G3": 100, "G4": 60, "G5": 40, "G6": 40, "G7": 40, "G8": 60, "G9": 100,
    "F2": 100, "F3": 60, "F4": 40, "F5": 20, "F6": 20, "F7": 40, "F8": 60, "F9": 100,
    "E1": 100, "E2": 60, "E3": 40, "E4": 20, "E5": 0, "E6": 20, "E7": 40, "E8": 60, "E9": 100,
    "D1": 100, "D2": 60, "D3": 40, "D4": 20, "D5": 20, "D6": 40, "D7": 60, "D8": 100,
    "C1": 100, "C2": 60, "C3": 40, "C4": 40, "C5": 40, "C6": 60, "C7": 100,
    "B1": 100, "B2": 60, "B3": 60, "B4": 60, "B5": 60, "B6": 100,
    "A1": 100, "A2": 100, "A3": 100, "A4": 100, "A5": 100
}


DEFAULT_AGENT_LIST = ["w", "A1b,A2b,A3b,A4b,A5b,B1b,B2b,B3b,B4b,B5b,B6b,C3b,C4b,C5b,G5w,G6w,G7w,H4w,H5w,H6w,H7w,H8w,H9w,I5w,I6w,I7w,I8w,I9w"]