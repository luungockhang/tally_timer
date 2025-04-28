from tkinter import *
import time as t

root = Tk()
root.geometry("300x300")
# Label, Button, Entry, Text
label = Label(root, text="Average Timer")
label.pack()

# Global Variables
running = False
initial_time = t.time() # to calculate time per count
current_time = t.time()
last_time = t.time()
total_count = 0
time_elasped = 0
avg_time_per_count = 0

# ==== Functions ====
def start_button_press():
    global initial_time, current_time, running
    initial_time = t.time()
    running = True
    
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
        refresh_labels()
# ~ Stop button ~
def stop_button_press():
    global initial_time, current_time, last_time, running, total_count
    # Reset everything
    running = False
    total_count = 0
    # log here

# ~ Logging functions ~
def log():
    pass

# ~ Refresh all labels ~
def refresh_labels():
    global count_label_content
    count_label_content.set(f"Count: {total_count}")
    
    
# Button frame
button_menu = Frame()
start_button = Button(button_menu,text="Start",command=start_button_press)
start_button.grid(column=0,row=0)

count_button = Button(button_menu, text="Count",command=count_button_press)
count_button.grid(column=1,row=0)

stop_button = Button(button_menu,text="stop")
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
count_label_content = StringVar(value=f"Count: {total_count}")
count_label = Label(display_section, textvariable=count_label_content)
count_label.pack()

last_time_content = StringVar(value=f"Last time: {last_time}")
last_time_label = Label(display_section,textvariable=last_time_content)
last_time_label.pack()

time_elasped_content = StringVar(value=f"Time elasped: {time_elasped}")
time_elasped_label = Label(display_section,textvariable=time_elasped_content)
time_elasped_label.pack()

avg_time_per_count_content = StringVar(value=f"Average time per count: {avg_time_per_count}")
avg_time_per_count_label = Label(display_section,text="Last time: ", textvariable=avg_time_per_count_content)
avg_time_per_count_label.pack()

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
text.pack()

logging_section.pack()



# Log frame

root.mainloop()