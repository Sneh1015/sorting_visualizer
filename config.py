"""
config.py
---------
All the fixed settings (constants) of the project live here.
If you want to change a colour, the window size or a slider range,
this is the only file you need to edit.
"""

# ---------- Window ----------
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700
FPS = 60
TITLE = "Sorting Visualizer"

# ---------- Layout (pixel positions) ----------
ALGO_BUTTON_Y = 70           # y position of the row of algorithm buttons
SLIDER_Y = 150               # y position of the two sliders
BAR_AREA = (20, 195, 1060, 410)   # (x, y, width, height) of the bar drawing area
BOTTOM_BUTTON_Y = 630        # y position of Start / Generate buttons

# ---------- Array values ----------
MIN_VALUE = 1                # smallest bar value
MAX_VALUE = 400              # biggest bar value (same as the original project)

# ---------- Sliders (same ranges as the original HTML project) ----------
DEFAULT_SIZE = 60
MIN_SIZE, MAX_SIZE = 20, 100       # number of bars
DEFAULT_SPEED = 100
MIN_SPEED, MAX_SPEED = 10, 240     # higher value = faster animation
DELAY_BASE = 245                   # delay(ms) = DELAY_BASE - speed

# ---------- Colours (R, G, B) ----------
BACKGROUND = (18, 18, 18)
PANEL = (30, 30, 47)
PANEL_BORDER = (51, 51, 51)
TEXT = (224, 224, 224)
TITLE_COLOR = (161, 182, 211)

BTN_NORMAL = (75, 92, 107)
BTN_HOVER = (91, 106, 122)
BTN_SELECTED = (0, 114, 255)
BTN_DISABLED = (50, 55, 60)
BTN_TEXT_DISABLED = (120, 120, 120)

BAR_DEFAULT = (0, 150, 255)      # blue   -> untouched bar
BAR_COMPARE = (255, 215, 0)      # yellow -> bars being compared
BAR_SWAP = (220, 53, 69)         # red    -> bars being swapped / overwritten
BAR_PIVOT = (170, 90, 220)       # purple -> pivot (Quick Sort)
BAR_SORTED = (40, 167, 69)       # green  -> bar is in its final place

SLIDER_TRACK = (60, 60, 60)
SLIDER_KNOB = (75, 130, 190)
