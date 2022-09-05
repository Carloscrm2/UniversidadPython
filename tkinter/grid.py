import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Grid')
ventana.iconbitmap('icono.ico')

# Configuramos el grid
ventana.rowconfigure(0, weight=1) # renglon 0 tamanio 1
ventana.rowconfigure(1, weight=5) # renglon 1 tamanio 5
ventana.columnconfigure(0, weight=1) # columna 0 tamanio 1
ventana.columnconfigure(1, weight=5) # columa 1 tamanio 5

# Metodos de los eventos
def evento1():
    boton1.config(text='Boton 1 presionado')

def evento2():
    boton2.config(text='Boton 2 presionado')
    
def evento4():
    # con fg cambiamos el color de la fuente del boton
    # relief cambiamos el contorno del boton
    boton4.config(text='Boton 4 presionado', fg='blue', relief=tk.GROOVE, bg='yellow')
# Definimos los botones
boton1 = ttk.Button(ventana, text='Boton 1', command=evento1)
boton2 = ttk.Button(ventana, text='Boton 2', command=evento2)
boton3 = ttk.Button(ventana, text='Boton 3')
# podemos usar directamente el paquete tk aunque habra diferencias
# con el paquete de ttk 
boton4 = tk.Button(ventana, text='Boton 4', command=evento4)

# utilizamos el metodo grid para colocar los elementos
# Con la propiedad sticky podemos hacer que un elemento se cargue
# hacia un espacio predeterminado

# N(arriba), E(derecha), S(abajo), W(izquierda)
# NSWE(Se expande hacia arriba abajo derecha e izquierda)

# padx=40 agregamos un margen externo de 40 a la izquierda y derecha de 40px
# pady margen externo en la parte superior e inferior
# ipadx margen interno a la izquiera y derecha 
# ipady margen interna arriba y abajo
# columnspan=2 hace que el primer boton se extienda 2 columnas
# rowspan el mismo concepto que columnspan pero con las filas
boton1.grid(row=0, column=0, sticky='NSWE', padx=40, pady=30, ipadx=20, ipady=50, columnspan=2, rowspan=2)
# boton2.grid(row=1, column=0, sticky='NSWE')
# boton3.grid(row=0, column=1, sticky='NSWE')
# boton4.grid(row=1, column=1, sticky='NSWE')
ventana.mainloop()

boton2 = ttk.Button(ventana, text='Boton 2', command=evento2)