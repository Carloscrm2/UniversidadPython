import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de entry')
ventana.iconbitmap('icono.ico')


# Etiqueta (label)
etiqueta1 = tk.Label(ventana, text='Aqui se mostrara el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2) # con column span abarca dos columas
# Definimos una variable que podremos modificar posteriormente (set), leer (get)
entrada_var1 = tk.StringVar(value='valor por default')
# asociamos una variable a nuestro componente Entry (textvariable=entrada1_var1)
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada_var1)
entrada1.grid(row=0, column=0)



def enviar():
    # Recuperamos la informacion a partir de la variable asociada con la caja de texto
    boton1.config(text=entrada1.get())
    # Messagebox (cajas mensajes)
    mensaje1 = entrada1.get()
    # messagebox.showinfo('Mensaje Informativo', mensaje1 + ' Informativo')
    # messagebox.showerror('Mensaje Error', mensaje1 + ' Error')
    messagebox.showwarning('Mensaje Alerta', mensaje1 + ' Alerta')

# Creamos un boton para que cada vez que lo presionemos
# nos imprima en la consola el texto ingresado, en la caja de texto
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()