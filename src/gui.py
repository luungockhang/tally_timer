from constants import Mode
from tkinter import *
from tkinter import ttk
import time as t
from timer import TallyTimer
from logger import TimerLogger
from display_render import Display
import threading as thr
# Consider adding a Display class that handles the button press methods and global variables


# ==== Root window config ====
root = Tk()
root.geometry("500x300")
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
log_textbox = ""    # Workaround for undefined variable

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
        counting = True
        status_value.set("Counting")
        clear_log()
        ui_update()
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
        ui_write_log()
    
    # Writes log
        
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
        run_name = "default"
        logger_obj = TimerLogger(run_name,log_textbox.get("1.0","end"))
        logger_obj.saveToFile()
        

# ~ Logging method ~
def ui_write_log():
    count = count_value.get()
    dur = current_duration_value.get()
    last = last_time_value.get()
    s = speed_value.get().split('\n')
    spd_str = f"{s[0]} / {s[1]} / {s[2]} / {s[3]}"
    append_log('end',f"Count: {count} | Duration: {dur} | Span: {last} | Speed: {spd_str}\n")
    log_textbox.see("end wordend")  # Scroll textbox to the end
    
def textbox_decorator(func):
    def wrapper(index, content):
        log_textbox['state'] = 'normal'
        func(index, content)
        log_textbox['state'] = 'disabled'
    return wrapper

@textbox_decorator
def delete_log(index,content):
    log_textbox.delete(index,content)

@textbox_decorator
def append_log(index, content):
    log_textbox.insert(index, content)

def clear_log():
    delete_log('1.0','end')

# ~ UI Update method ~
def ui_update():
    # (Make a class called Display for this too maybe)
    # Update stats
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
'''
Example:
Start timer at <current time>
Count: <count> - Time since last - Time elasped - Average
End timer at <current time> - Total time

Enable textbox in the program when logging then disable it
'''

# ~ Textbox UI (Log frame) ~
logging_section = Frame()
log_textbox = Text(logging_section, width=100, height=10)
append_log('1.0',
'''Press Start to start counting.
Press Count to increment counts and update logs.
Press Stop to stop counting and save log.
''')
log_textbox.pack()

# ~ Scrollbar(s) ~
log_textbox_ys = ttk.Scrollbar(logging_section, orient ='vertical',command=log_textbox.yview)
log_textbox['yscrollcommand'] = log_textbox_ys.set

logging_section.pack()


root.mainloop()