import time
import datetime

class Timer:
    def __init__(self):
        self.initial_time = 0
        self.average_time = 0
        self.time_since_last = 0
        self.current_time = 0
    
    def start(self):
        self.initial_time = time.time()
        self.current_time = self.initial_time
    
    def stop(self):
        pass

class TallyTimer(Timer):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.avg_time_since_last = 0
            
