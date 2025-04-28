import time
import datetime

class Timer:
    def __init__(self):
        self.initial_time = 0       # Initial time when started
        self.current_time = 0       # Current time
    
    
    def start(self):
        self.initial_time = time.time()
        self.current_time = self.initial_time
    
    def stop(self):
        # Might as well just do nothing here
        self.initial_time = 0
        self.current_time = 0

class TallyTimer(Timer):
    def __init__(self):
        super().__init__()
        self.count = 0              # Count in this instance
        self.last_time = 0          # Time elasped in last count
        self.avg_time_per_count = 0 # Average time per count (speed)
    def count(self):
        self.count += 1
        self.current_time = time.time()
        self.last_time = time.time()
            
