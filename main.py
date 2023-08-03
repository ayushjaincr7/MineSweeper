from tkinter import *
from tkinter import ttk
import settings
import utils
from cell import Cell


root = Tk()
# override the settings of the window
root.config(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('MineSweeper')
root.resizable(False,False)

top_frame = Frame(
    root,
    bg="black", #change later to black
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0,y=0)


left_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(25),
    height=utils.height_prct(75),
)
left_frame.place(x=0,y=180)

center_frame = Frame(
    root,
    bg="black",
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)

center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,row=y
        )
    
Cell.randomize_mines()

# run the windows
root.mainloop()

