import tkinter as tk

# root window
root = tk.Tk()

# prevent from resizing a window
root.resizable(width=False, height=False)

canvas = tk.Canvas(root, height=420, width=800)
canvas.pack()

label = tk.Label(root, text='Odblokuj bazę danych', font=24)
label.place(relx=0.1, rely=0.2)

label2 = tk.Label(root, text='© powered by Filip Walkowicz')
label2.pack()

frame = tk.Frame(root, bg='#cbc8c8')
frame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

if __name__ == "__main__":
    # run an APP
    root.mainloop()
