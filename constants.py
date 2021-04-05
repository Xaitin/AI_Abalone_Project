""" Ints """

HEIGHT_HEADER_FOOTER, GAMEBOARD_SIZE = 100, 500
WIDTH_SIDEBAR = 300
WINDOW_WIDTH, WINDOW_HEIGHT = GAMEBOARD_SIZE + 2 * WIDTH_SIDEBAR, GAMEBOARD_SIZE + 2 * HEIGHT_HEADER_FOOTER
PANEL_WIDTH, PANEL_HEIGHT = 220, 410
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
    "I5": -1, "I6": -1, "I7": -1, "I8": -1, "I9": -1,
    "H4": -1, "H5": 0, "H6": 0, "H7": 0, "H8": 0, "H9": -1,
    "G3": -1, "G4": 0, "G5": 1, "G6": 1, "G7": 1, "G8": 0, "G9": -1,
    "F2": -1, "F3": 0, "F4": 1, "F5": 2, "F6": 2, "F7": 1, "F8": 0, "F9": -1,
    "E1": -1, "E2": 0, "E3": 1, "E4": 2, "E5": 2, "E6": 2, "E7": 1, "E8": 0, "E9": -1,
    "D1": -1, "D2": 0, "D3": 1, "D4": 2, "D5": 2, "D6": 1, "D7": 0, "D8": -1,
    "C1": -1, "C2": 0, "C3": 1, "C4": 1, "C5": 1, "C6": 0, "C7": -1,
    "B1": -1, "B2": 0, "B3": 0, "B4": 0, "B5": 0, "B6": -1,
    "A1": -1, "A2": -1, "A3": -1, "A4": -1, "A5": -1
}

ENEMY_SQUARE_VALUES = {
    "I5": 4, "I6": 4, "I7": 4, "I8": 4, "I9": 4,
    "H4": 4, "H5": 3, "H6": 3, "H7": 3, "H8": 3, "H9": 4,
    "G3": 4, "G4": 3, "G5": 2, "G6": 2, "G7": 2, "G8": 3, "G9": 4,
    "F2": 4, "F3": 3, "F4": 2, "F5": 0, "F6": 0, "F7": 2, "F8": 3, "F9": 4,
    "E1": 4, "E2": 3, "E3": 2, "E4": 0, "E5": 0, "E6": 0, "E7": 2, "E8": 3, "E9": 4,
    "D1": 4, "D2": 3, "D3": 2, "D4": 0, "D5": 0, "D6": 2, "D7": 3, "D8": 4,
    "C1": 4, "C2": 3, "C3": 2, "C4": 2, "C5": 2, "C6": 3, "C7": 4,
    "B1": 4, "B2": 3, "B3": 3, "B4": 3, "B5": 3, "B6": 4,
    "A1": 4, "A2": 4, "A3": 4, "A4": 4, "A5": 4
}


DEFAULT_AGENT_LIST = ["w", "A1b,A2b,A3b,A4b,A5b,B1b,B2b,B3b,B4b,B5b,B6b,C3b,C4b,C5b,G5w,G6w,G7w,H4w,H5w,H6w,H7w,H8w,H9w,I5w,I6w,I7w,I8w,I9w"]