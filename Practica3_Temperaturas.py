from tkinter import END, messagebox
import tkinter as tk
import math

root = tk.Tk()
root.title("Temperaturas")
root.config(width=400, height=400)

tk.Label(root, text="Temperatura: ").place(x=50, y=60)
txtTemp = tk.Entry(root)
txtTemp.place(x=50, y=80)
select = tk.IntVar()

tk.Label(root, text="Resultado: ").place(x=50, y=100)
txtResultado = tk.Entry()
txtResultado.place(x=50, y=120)


def Mensaje():
    if select.get() == 1:  # Celsius - Kelvin
        txtResultado.delete(0, END)
        temperatura = float(txtTemp.get())
        res = float(temperatura + 273.16)
        txtResultado.insert(0, res)

    if select.get() == 2:  # Kelvin - Celsius
        txtResultado.delete(0, END)
        temperatura = float(txtTemp.get())
        res = float(temperatura - 273.16)
        txtResultado.insert(0, res)

    if select.get() == 3:  # Celsius - Fahrenheit
        txtResultado.delete(0, END)
        temperatura = float(txtTemp.get())
        res = float(temperatura * 1.8 + 32)
        txtResultado.insert(0, res)

    if select.get() == 4:  # Farenheit - Kelvin
        txtResultado.delete(0, END)
        temperatura = float(txtTemp.get())
        res = float((5 / 9) * (temperatura - 32) + 273.16)
        txtResultado.insert(0, res)

    if select.get() == 5:  # Farenheit - Celsius
        txtResultado.delete(0, END)
        temperatura = float(txtTemp.get())
        res = float((temperatura - 32) / 1.8)
        txtResultado.insert(0, res)

    if select.get() == 6:  # Kelvin - Farenheit
        txtResultado.delete(0, END)
        temperatura = float(txtTemp.get())
        res = float(1.8 * (temperatura - 273.16) + 32)
        txtResultado.insert(0, res)


btnMostrar = tk.Button(root, text="Calcular", command=Mensaje)
btnMostrar.place(x=50, y=150)

rbt = tk.Radiobutton(root, text="Celsius - Kelvin", value=1, variable=select).place(x=50, y=200)
rbt = tk.Radiobutton(root, text="Kelvin - Celsius", value=2, variable=select).place(x=50, y=220)
rbt = tk.Radiobutton(root, text="Celsius - Fahrenheit", value=3, variable=select).place(x=50, y=240)
rbt = tk.Radiobutton(root, text="Farenheit - Kelvin", value=4, variable=select).place(x=50, y=260)
rbt = tk.Radiobutton(root, text="Farenheit - Celsius", value=5, variable=select).place(x=50, y=280)
rbt = tk.Radiobutton(root, text="Kelvin - Farenheit", value=6, variable=select).place(x=50, y=300)

root.mainloop()
