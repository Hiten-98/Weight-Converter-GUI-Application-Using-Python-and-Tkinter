import tkinter as tk

def pounds():
    pound = float(entry.get())
    new_pound = pound * 2.20
    result.config(text= new_pound)

def grams():
    gram = float(entry.get())
    new_gram = gram * 1000
    result.config(text= new_gram)

def ounces():
    ounce = float(entry.get())
    new_ounce = ounce * 35.27
    result.config(text = new_ounce)

window = tk.Tk()
window.title("Weight Converter")
window.config(padx = 30, pady = 30)

entry_label = tk.Label(text="Enter Weight in KG = ")
entry_label.grid(row=0, column=0)

entry = tk.Entry(width=5)
entry.grid(row=0, column=1)

kg_label = tk.Label(text=" KG ")
kg_label.grid(row=0, column=2)

result = tk.Label(text="0")
result.grid(row=1, column=1)

p_button = tk.Button(text="Pounds", command = pounds)
p_button.grid(row=2, column=0)

g_button = tk.Button(text="Grams", command = grams)
g_button.grid(row=2, column=1)

o_button = tk.Button(text="Ounces", command = ounces)
o_button.grid(row=2, column=3)

window.mainloop()