# Classes for logging
# Tkinter lets you insert into its text field, so we use the tkinter library to edit the text. Then get the text and save to a file. 
import constants as const
import os
from pathlib import Path
import datetime

class Logger:
    def __init__(self):
        self.content = ""
        self.path = const.DEFAULT_LOG_PATH
        self.log_time_string = datetime.datetime.now().astimezone().strftime("%Y%m%d%H%M%S")
    
    def saveToFile(self):
        pass
        # Implement naming logic in child

# Currently does not save the name of a run
class TimerLogger(Logger):
    def __init__(self):
        self.run_name = ""
    
    def saveToFile(self):
        p = Path(self.path)
        if not p.exists():
            p.mkdir()
        file_name = self.run_name + " " + self.log_time_string
        p /= file_name
        p.write_text(self.content)