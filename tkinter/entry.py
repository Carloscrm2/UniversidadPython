import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de entry')
ventana.iconbitmap('icono.ico')

# width cantidad de caracteres a ocupar en la caja
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER)
entrada1.grid(row=0, column=0)
# insert agrefa un texto a la caja
entrada1.insert(0,'Introduce una cadena')

ventana.mainloop()