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

# run the windows
root.mainloop()

