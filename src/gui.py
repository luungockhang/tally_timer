from tkinter import *
import time as t
from timer import TallyTimer

# Root window config
root = Tk()
root.geometry("300x300")
root.title("Tally Timer")
# Label, Button, Entry, Text
status_label = Label(root, text="Standby")
status_value = StringVar(value="running")
status_value_label = Label(root,textvariable=status_value)
status_label.pack()


# Global Variables
running = False
initial_time = t.time() # to calculate time per count
current_time = t.time()
last_time = t.time()
total_count = 0
time_elasped = 0
avg_time_per_count = 0

# ==== UI Functions ====
# ~ Start Button ~
"""
Pressing Start button (re)initializes a TallyTimer instance.
If the timer is already running, pressing again does nothing
"""
def start_button_press():
    global initial_time, current_time, running
    if not running:
        initial_time = t.time()
        running = True
    # Might want to add a warning about the timer is already running and tell user to press Stop
    
# ~ Count Button ~
"""
"""
def count_button_press():
    global current_time, initial_time, last_time, total_count, total_count_label
    if running:
        # Get current time, then get time since last with current time - last time (time delta)
        current_time = t.time()
        print(current_time, last_time, int(current_time-last_time))
        last_time = t.time()
        # Increment count by one
        total_count += 1
        
        # Refresh UI
        ui_update()
        
# ~ Stop button ~ (TODO)
def stop_button_press():
    global initial_time, current_time, last_time, running, total_count
    if running:
        # Reset everything
        running = False
        total_count = 0
        # log here

# ~ Logging functions ~ (Not impletemented yet)
def log():
    pass

# ~ Refresh all labels ~
def ui_update():
    # Make a class called Display for this too maybe
    global count_value
    count_value.set(total_count)
    
    
# Button frame
button_menu = Frame()
start_button = Button(button_menu,text="Start",command=start_button_press)
start_button.grid(column=0,row=0)

count_button = Button(button_menu, text="Count",command=count_button_press)
count_button.grid(column=1,row=0)

stop_button = Button(button_menu,text="Stop", command=stop_button_press)
stop_button.grid(column=2,row=0)

button_menu.pack()

# Time display frame
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
last_time_label = Label(display_section,text="Last time")
last_time_label.grid(column=0,row=1,sticky="w")
last_time_value = StringVar(value=0)
last_time_value_label = Label(display_section, textvariable=last_time_value)
last_time_value_label.grid(column=1,row=1)

# Time elasped
time_elasped_label = Label(display_section,text="Time elasped")
time_elasped_label.grid(column=0,row=2,sticky="w")
time_elasped_value = StringVar(value=0)
time_elasped_value_label = Label(display_section, textvariable=time_elasped_value)
time_elasped_value_label.grid(column=1,row=2)

# Average time per count
avg_time_per_count_label = Label(display_section,text="Average time per count")
avg_time_per_count_label.grid(column=0,row=3,sticky="w")
avg_time_per_count_value = StringVar(value=0)
avg_time_per_count_value_label = Label(display_section, textvariable=avg_time_per_count_value)
avg_time_per_count_value_label.grid(column=1,row=3)

display_section.pack()

# Textbox section for logging
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