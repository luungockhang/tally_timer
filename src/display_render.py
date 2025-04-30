# Will handle display later instead of global variables
# hopefully :D

import timer

class Display:
    def __init__(self, timer_obj, status, counting):
        self.timer_obj = timer_obj
        self.status = status
        self.counting = counting