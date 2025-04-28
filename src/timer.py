import time
import datetime

class Timer:
    def __init__(self):
        self.initial_time = time.time()
        self.average_time = self.initial_time
        self.time_since_last = 0
        self.current_time = self.initial_time
    
    def stop(self):
        pass