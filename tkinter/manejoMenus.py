import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de Menus')
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
    etiqueta1.config(text=entrada1.get())
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje Informativo', mensaje1 + ' Informativo')


# programamos la opcion de salir 
def salir():
    ventana.quit()
    ventana.destroy()
    sys.exit()


def crear_menu():
    # configurar el menu principal
    menu_prinicipal = Menu(ventana)
    #tearoff = false para que no se separe el menu de la interface grafica
    # creamos el submenu archivo
    submenu_archivo = Menu(menu_prinicipal, tearoff=False)
    # agregamos una nueva opcion al submenu archivo
    submenu_archivo.add_command(label='Nuevo')
    # Agregamos un separador
    submenu_archivo.add_separator()
    # Agregamos la opcion de salir
    submenu_archivo.add_command(label='Salir', command=salir)
    # agregamos el submenu al menu principal
    menu_prinicipal.add_cascade(menu=submenu_archivo, label='Archivo')
    # submenu de ayuda
    submenu_ayuda = Menu(menu_prinicipal, tearoff=False)
    # Agregamos una nueva opcion al submenu ayuda
    submenu_ayuda.add_command(label='Acerca De')
    # Agregamos al menu principal el submenu ayuda
    menu_prinicipal.add_cascade(menu=submenu_ayuda, label='Ayuda')
    # mostramos el menu en la ventana principal
    ventana.config(menu=menu_prinicipal)

boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

crear_menu()
ventana.mainloop()