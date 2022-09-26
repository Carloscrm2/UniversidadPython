import sys
import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('300x130')
ventana.title('Login')

# configuracion del grid
ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)


# Definimos las etiquetas
label1 = ttk.Label(ventana, text='Usuario:')
label1.grid(row=0, column=0)
label2 = ttk.Label(ventana, text='Contraseña:')
label2.grid(row=1, column=0, sticky='N')

# Varibales asociadas a las cajas de texto
user = tk.StringVar(value='')
pas = tk.StringVar(value='')

# Definimos las cajas de texto
entrada1 = ttk.Entry(ventana, width=20, justify=tk.CENTER, textvariable=user)
entrada1.grid(row=0, column=1, sticky='W')
entrada2 = ttk.Entry(ventana, width=20, justify=tk.CENTER, show='*', textvariable=pas)
entrada2.grid(row=1, column=1, sticky='WN')
entrada2.config()

def login():
    messagebox.showinfo('Datos Login', 'Usuario: ' + user.get() + ', Password: ' + pas.get())
    pass

# Definimos el boton
boton1 = ttk.Button(ventana, text='Login', command=login)
boton1.grid(row=2, column=1, sticky='WN')
ventana.mainloop()