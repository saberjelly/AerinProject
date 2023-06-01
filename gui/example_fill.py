from tkinter import Tk, Frame, Label, Button, X, Y, LEFT, BOTH

window = Tk()
frame1 = Frame(master=window, width=100, bg="red")
frame1.pack(fill=BOTH, side=LEFT, expand=True)
frame2 = Frame(master=window, width=50, bg="yellow")
frame2.pack(fill=BOTH, side=LEFT, expand=True)
frame3 = Frame(master=window, width=25, bg="blue")
frame3.pack(fill=BOTH, side= LEFT, expand=True)
window.mainloop()
