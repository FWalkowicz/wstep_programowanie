import tkinter as tk
from settings import *

# root window
root = tk.Tk()

# prevent from resizing a window
root.resizable(width=False, height=False)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#cbc8c8')
frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

label = tk.Label(root, text='Odblokuj bazę danych', font=24)
label.place(relx=0.1, rely=0.2)

label3 = tk.Label(frame, text='Wprowadź hasło: ', bg=FRAME_BG_COLOUR)
label3.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

label2 = tk.Label(root, text='© powered by Filip Walkowicz')
label2.pack()

if __name__ == "__main__":
    # run an APP
    root.mainloop()
