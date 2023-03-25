from tkinter import Tk, Frame, Label, Button

top = Tk()
Lhello = Label(top, text="hello world")
Lhello.pack(side="left")
B = Button(top, text="Quit", command=top.quit)
B.pack(padx=10)
top.mainloop()
print("end")
