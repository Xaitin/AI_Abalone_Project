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

""" Colors """
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
BOARD_COLOR = (132, 152, 191)
HEXAGON_OUTLINE_COLOR = (193, 199, 217)
SELECTED_HEXAGON_COLOR = (79, 99, 140)

""" Path """
WHITE_MARBLE_PATH = "drawables/white_marble.png"
BLACK_MARBLE_PATH = "drawables/black_marble.png"

""" Game Board States """
INITIAL_GAME_BOARD_STATE_DEFAULT = [
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
    [-2, -2, -2, -2, -2, 2, 2, 2, 2, 2, -2],
    [-2, -2, -2, -2, 2, 2, 2, 2, 2, 2, -2],
    [-2, -2, -2, -1, -1, 2, 2, 2, -1, -1, -2],
    [-2, -2, -1, -1, -1, -1, -1, -1, -1, -1, -2],
    [-2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2],
    [-2, -1, -1, -1, -1, -1, -1, -1, -1, -2, -2],
    [-2, -1, -1, 1, 1, 1, -1, -1, -2, -2, -2],
    [-2, 1, 1, 1, 1, 1, 1, -2, -2, -2, -2],
    [-2, 1, 1, 1, 1, 1, -2, -2, -2, -2, -2],
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
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
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
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
    [-2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2],
]

INITIAL_GAME_BOARD_SETUPS = [
    INITIAL_GAME_BOARD_STATE_DEFAULT,
    INITIAL_GAME_BOARD_STATE_BELGIAN,
    INITIAL_GAME_BOARD_STATE_GERMAN
]
