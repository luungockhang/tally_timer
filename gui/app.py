from tkinter import *
import time as t

root = Tk()
root.geometry("300x300")
# Label, Button, Entry, Text
label = Label(root, text="Average Timer")
label.pack()

# Variables
running = False
initial_time = t.time()
current_time = t.time()
last_time = t.time()

# Functions
def start():
    global initial_time, current_time, running
    initial_time = t.time()
    running = True
    
def count():
    global initial_time    
    if running:
        last_time = t.time()
        print(int(current_time-last_time))

def stop():
    global initial_time, current_time, last_time, running
    running = False
    # log here
    
def log():
    pass
    
# Button frame
button_menu = Frame()
start_button = Button(button_menu,text="Start",command=start)
start_button.grid(column=0,row=0)

count_button = Button(button_menu, text="Count",command=count)
count_button.grid(column=1,row=0)

stop_button = Button(button_menu,text="stop")
stop_button.grid(column=2,row=0)

button_menu.pack()

# Time display frame


# Log frame

root.mainloop()