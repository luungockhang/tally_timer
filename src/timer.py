# Timer class and its methods

import time
import datetime
from constants import Mode

"""
Fields:
    initial_time: Initial time when the timer is started.
    _current_time: Current time when the count button is pressed, for calculation in class methods. 
    _raw_current_duratino: Unprocessed current duration for speed calculation (subjected to removal)
    current_duration: Current duration tuple for display.

Methods:
    start: Record the initial time as well as update private current time field

Notes/Consideration:
    If reset is necessary, simply reinitialize the instance.
"""
class Timer:
    def __init__(self):
        self.initial_time = 0
        self._current_time = 0
        self._raw_current_duration = 1
        self.current_duration = 0
    
    def start(self):
        self.initial_time = time.time()
        self._current_time = self.initial_time
        self.current_duration = 0
        

class TallyTimer(Timer):
    def __init__(self):
        super().__init__()
        self.total = 0              # Count in this instance
        self.last_time = 0          # Time elasped in last count
        self.speed = self.calculate_speed() # Average time per count (speed)

    def start(self):
        super().start()
        self.total = 0
        self.last_time = 0
        
        
    # Calculate last_time, increment count
    def count(self):
        self.total += 1
        self.last_time = self.convert_to_time(time.time() - self._current_time)
        print(self._current_time)
        self._current_time = time.time()
        self._raw_current_duration = self._current_time - self.initial_time
        print(self._raw_current_duration)
        self.current_duration = self.convert_to_time(self._raw_current_duration)
        self.speed = self.calculate_speed()
    
    # Calculate speed
    def calculate_speed(self):
        # Speed is a tuple of day, minute, hour, sec
        secs = self._raw_current_duration
        per_s = round(self.total / secs, 2)
        secs /= 60  # Convert to mins
        per_m = round(self.total / secs, 2)
        secs /= 60  # Convert to hours
        per_h = round(self.total / secs, 2)
        secs /= 24  # Convert to days
        per_d = round(self.total / secs, 2)
        return (per_s,per_m,per_h,per_d)
    
    # Convert into a tuple of day hour minute sec?
    def convert_to_time(self,secs):
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
                s = self.speed
                return f"{s[0]}/sec\n{s[1]}/min\n{s[2]}/hour\n{s[3]}/day"
            case _:
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
        
