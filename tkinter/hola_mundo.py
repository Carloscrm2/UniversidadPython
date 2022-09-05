# GUI - Graphical User Interface
# Tkinter - Tk Interface
# Importamos el modulo de tkinter
from bdb import effective
import tkinter as tk
# Importamos el modulo del tema (componentes) de tkinter
from tkinter import ttk 

# Creamos un objeto usando la clase tk
ventana = tk.Tk()

# Modificamos el tamaño de la ventana (pixeles)
ventana.geometry('600x400')

# Cambiamos el nombre de la ventana
ventana.title('Hola Mundo')

# Configuramos el icono de la aplicacion
ventana.iconbitmap('icono.ico')

#Creamos un metodo evento_click
def evento_click():
    boton1.config(text='Boton presionado')
    print('Ejecucion del evento_click')
    # Creamos un nuevo boton y lo mostramos
    boton2 = ttk.Button(ventana, text='Nuevo boton')
    boton2.pack()
    
# Creamos un boton (widget), el objeto padre es la ventana
boton1 = ttk.Button(ventana, text='Dar click', command=evento_click)

# Utilizamos el pack layout manager para mostrar el boton de la ventana
boton1.pack()

# Iniciamos la venta (esta linea la ejecutamos al final)
# Si la ejecutamos antes no se van a ejecutar los cambios
ventana.mainloop()