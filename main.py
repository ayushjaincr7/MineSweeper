from tkinter import *
from tkinter import ttk


root = Tk()
# override the settings of the window
root.config(bg="black")
root.geometry('1440x720')
root.title('MineSweeper')
root.resizable(False,False)

top_frame = Frame(
    root,
    bg="red", #change later to black
    width=1440,
    height=180
)
top_frame.place(x=0,y=0)


left_frame = Frame(
    root,
    bg="blue",
    width=360,
    height=540,
)
left_frame.place(x=0,y=180)

# run the windows
root.mainloop()

