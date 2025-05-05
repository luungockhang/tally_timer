# Constants are stored here

from enum import Enum

class Mode(Enum):
    LAST_TIME = 0
    CURRENT_DURATION = 1
    SPEED = 2

DEFAULT_LOG_PATH = "./logs/"