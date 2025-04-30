from calculate_mode import Mode
from tkinter import *
import time as t
from timer import TallyTimer
from display_render import Display
import threading as thr
# Consider adding a Display class that handles the button press methods and global variables


# ==== Root window config ====
root = Tk()
root.geometry("300x300")
root.title("Tally Timer")
# Label, Button, Entry, Text
status_frame = Frame()
status_label = Label(status_frame, text="Status: ")
status_label.grid(column=0,row=0)
status_value = StringVar(value="Standby")
status_value_label = Label(status_frame,textvariable=status_value)
status_value_label.grid(column=1,row=0)
status_frame.pack()

# ==== Global Variables ====
timer_obj = TallyTimer()
counting = False
display = Display(timer_obj, status_value,counting)

# ==== UI Functions ====
# ~ Start Button ~
"""
Pressing Start button (re)initializes a TallyTimer instance.
If the timer is already running, pressing again does nothing
"""
def start_button_press(timer_obj):
    global counting
    if not counting:
        timer_obj.start()
        print(timer_obj.initial_time)
        counting = True
        status_value.set("Counting")
    # Might want to add a warning about the timer is already running and tell user to press Stop
    
# ~ Count Button ~
"""
Pressing Count will increment count by 1, record time spent on last count then update current time and calculate speed
"""
def count_button_press(timer_obj):
    global counting
    if counting:
        timer_obj.count()
        ui_update()
        
# ~ Stop button ~ (TODO)
"""
Pressing Stop will change the status of timer to not running and save log (not implemented yet). Change status label to stop.
DO NOT RESET THE STATS BEFORE RESTARTING.
"""
def stop_button_press(timer_obj):
    global counting
    if counting:
        # Stop counting
        counting = False
        status_value.set("Stopped")
        
        ui_update()
        # Save log here

# ~ Logging methods ~ (Not impletemented yet)
def log():
    pass

# ~ Refresh all labels ~
def ui_update():
    # global timer_obj, count_value, last_time_value, current_duration_value
    # Make a class called Display for this too maybe
    count_value.set(timer_obj.total)
    last_time_value.set(timer_obj.convert_to_string(Mode.LAST_TIME))
    current_duration_value.set(timer_obj.convert_to_string(Mode.CURRENT_DURATION))
    speed_value.set(timer_obj.convert_to_string(Mode.SPEED))
    
    

# ================= Interface renderer ==================  
# Start button
button_menu = Frame()
start_button = Button(button_menu,text="Start",command=lambda: start_button_press(timer_obj))
start_button.grid(column=0,row=0)

# Count button
count_button = Button(button_menu, text="Count",command=lambda: count_button_press(timer_obj))
count_button.grid(column=1,row=0)

# Stop button
stop_button = Button(button_menu,text="Stop", command=lambda: stop_button_press(timer_obj))
stop_button.grid(column=2,row=0)

button_menu.pack()

# === Time display frame ===
"""
Display:
- total count
- time since last
- time elasped
- average time per count
"""
display_section = Frame()

"""
Each of these are labels and values.
"""
# Count
count_label = Label(display_section, text="Count")
count_label.grid(column=0,row=0,sticky="w")
count_value = StringVar(value=0)
count_value_label = Label(display_section, textvariable=count_value)
count_value_label.grid(column=1,row=0)

# Last time
last_time_label = Label(display_section,text="Time since last count")
last_time_label.grid(column=0,row=1,sticky="w")
last_time_value = StringVar(value=0)
last_time_value_label = Label(display_section, textvariable=last_time_value)
last_time_value_label.grid(column=1,row=1)

# Time elasped
current_duration_label = Label(display_section,text="Current duration")
current_duration_label.grid(column=0,row=2,sticky="w")
current_duration_value = StringVar(value=0)
current_duration_value_label = Label(display_section, textvariable=current_duration_value)
current_duration_value_label.grid(column=1,row=2)

# Speed
speed_label = Label(display_section,text="Speed\n(Count/Time)",justify="left")
speed_label.grid(column=0,row=3,sticky="nw")
# Speed grid that displays values
speed_value = StringVar(value="0/sec\n0/min\n0/hour\n0/day")
speed_value_label = Label(display_section,textvariable=speed_value)
speed_value_label.grid(column=1,row=3)


display_section.pack()

# === Textbox section for logging ===
"""
Example:
Start timer at <current time>
Count: <count> - Time since last - Time elasped - Average
End timer at <current time> - Total time

Enable textbox in the program when logging then disable it

(TODO)
"""
logging_section = Frame()

text = Text(logging_section, width=40, height=10)
# use this to insert text into the textbox
text.insert('1.0','Press Start to start counting\n')
# disable the textbox
text['state'] = 'disabled'
text.pack()

logging_section.pack()

# Log frame

root.mainloop()