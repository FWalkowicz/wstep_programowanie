import tkinter as tk

import settings
from settings import *


class App:

    def __init__(self, master):
        self.master = master
        self.master.resizable(width=False, height=False)  # prevent from resizing a window
        self.canvas = tk.Canvas(self.master, height=HEIGHT, width=WIDTH)
        self.frame = tk.Frame(self.master, bg=FRAME_BG_COLOUR)
        self.label = tk.Label(self.master, text='Odblokuj bazę danych', font=24)
        self.label3 = tk.Label(self.frame, text='Wprowadź hasło: ', bg=FRAME_BG_COLOUR)
        self.entry = tk.Entry(self.frame)
        self.label2 = tk.Label(self.master, text='© powered by Filip Walkowicz')
        self.login_menu()

    def login_menu(self):
        self.frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)
        self.label.place(relx=0.1, rely=0.2)
        self.label3.place(relx=0.05, rely=0.1)
        self.entry.place(relx=0.2, rely=0.1)
        self.label2.pack()
        self.canvas.pack()

def initialization():
    root = tk.Tk()
    App(root)
    root.mainloop()


if __name__ == "__main__":
    initialization()
