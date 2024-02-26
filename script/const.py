from .display import Display
from .save_system import SaveSystem

def rgb(r, g, b):
    return "#%02x%02x%02x" % (r, g, b)


Display.init()

APP_WIDTH = 150
APP_HEIGHT = 80
APP_GEOMETRY = f"{APP_WIDTH}x{APP_HEIGHT}"

APP_POSITION_X = Display.get_desktop_size()[0] - APP_WIDTH
APP_POSITION_Y = SaveSystem.loadData(SaveSystem.POS_PATH, 200)
APP_TRANSPARENCY = SaveSystem.loadData(SaveSystem.ALPHA_PATH, 50)



IGNORED_COLOR = rgb(10, 10, 10)

CURSORS = (
    "arrow",
    "circle",
    "clock",
    "cross",
    "dotbox",
    "exchange",
    "fleur",
    "heart",
    "heart",
    "man",
    "mouse",
    "pirate",
    "plus",
    "shuttle",
    "sizing",
    "spider",
    "spraycan",
    "star",
    "target",
    "tcross",
    "trek",
    "watch",
)

CURRENT_CURSOR = 12
NET_SPEED_UPDATE_DELAY = 1000 # in ms

BYTE_TO_GB = 1 / (1024 * 1024 * 1024)
