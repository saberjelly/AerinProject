import tkinter as tk

window = tk.Tk()
frame = tk.Frame(master=window, height=150, width=150)
frame.pack()
label1 = tk.Label(master=frame, text="I am at 0,0", bg="red")
label1.place(x=0, y=0)
label2 = tk.Label(master=frame, text="I am at 75,75", bg="blue")
label2.place(x=75, y=75)
window.mainloop()
