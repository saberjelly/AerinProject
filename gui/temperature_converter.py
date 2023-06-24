import tkinter as tk

def convert_to_C():
    value = float(initial_entry1.get())
    result_c["text"] = f"{(5/9) * (value - 32)} \N{DEGREE CELSIUS}"
def convert_to_F():
    value = float(initial_entry2.get())
    result_f["text"] = f"{(value * 9/5) + 32} \N{DEGREE FAHRENHEIT}"


window = tk.Tk()
window.title(string="Temperature Converter")
window.resizable(width=False, height=False)
frame1 = tk.Frame(master=window, pady=10)

# F to C
initial_entry1 = tk.Entry(master=frame1, width=10)
label_f = tk.Label(master=frame1, text="\N{DEGREE FAHRENHEIT}")
button_celsius = tk.Button(master=frame1, text="->", command=convert_to_C)
result_c = tk.Label(master=frame1, text="\N{DEGREE CELSIUS}")

initial_entry1.grid(row=0, column=0, sticky="e")
label_f.grid(row=0, column=1, sticky="w")
frame1.grid(row=0, column=0, padx=10)
button_celsius.grid(row=0, column=2)
result_c.grid(row=0, column=3, padx=10)

# C to F
initial_entry2 = tk.Entry(master=frame1, width=10)
label_c = tk.Label(master=frame1, text="\N{DEGREE CELSIUS}")
button_fahrenheit = tk.Button(master=frame1, text="->", command=convert_to_F)
result_f = tk.Label(master=frame1, text="\N{DEGREE FAHRENHEIT}")

initial_entry2.grid(row=1, column=0, sticky="e")
label_c.grid(row=1, column=1, sticky="w")
button_fahrenheit.grid(row=1, column=2)
result_f.grid(row=1, column=3, padx=10)

window.mainloop()