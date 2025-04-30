# Timer class and its methods

import time
import datetime
from calculate_mode import Mode

class Timer:
    def __init__(self):
        self.initial_time = 0       # Initial time when started
        self._current_time = 0       # Current time (for calculation)
        self._raw_current_duration = 0  # Total time elasped (for calculation)
        self.current_duration = 0   # Total time elasped
    
    def start(self):
        self.initial_time = time.time()
        self._current_time = self.initial_time
    
    # def stop(self):
    #     # Might as well just do nothing here
    #     self.initial_time = 0
    #     self.current_time = 0

class TallyTimer(Timer):
    def __init__(self):
        super().__init__()
        self.total = 0              # Count in this instance
        self.last_time = 0          # Time elasped in last count
        self.speed = 0 # Average time per count (speed)

    # Calculate last_time, increment count
    def count(self):
        self.total += 1
        self.last_time = self.convert_to_time(time.time() - self._current_time)
        self._current_time = time.time()
        self._raw_current_duration = self._current_time - self.initial_time
        self.current_duration = self.convert_to_time(self._raw_current_duration)
        self.speed = 0
    
    # Calculate speed
    def calculate_speed(self):
        # Speed is a tuple of day, minute, hour, sec
        
        pass
    
    # Convert into a tuple of day hour minute sec?
    def convert_to_time(self,secs):
        print(secs)
        secs = int(secs)
        days = secs // (24*60*60)
        secs %= 24*60*60
        hours = secs // (60*60)
        secs %= 60*60
        mins = secs // 60
        secs %= 60
        return (secs,mins,hours,days)
    
    def convert_to_string(self,mode):
        # If current_duration is 0, it means the object was freshly initialized
        time = 0
        match mode:
            case Mode.CURRENT_DURATION:
                time = self.current_duration
            case Mode.LAST_TIME:
                time = self.last_time
            case Mode.SPEED:
                return
            case _:     # Default case
                return
        
        # per days,hours,mins,secs
        if time == 0:
            return "0 sec"
        # If day isn't 0
        if time[3] != 0:
            return f"{time[3]} days {time[2]} hours {time[1]} mins {time[0]} secs"
        # If hour isn't 0
        if time[2] != 0:
            return f"{time[2]} hours {time[1]} mins {time[0]} secs"
        # If min isn't 0
        if time[1] != 0:
            return f"{time[1]} mins {time[0]} secs"
        
        return f"{time[0]} secs"
        
