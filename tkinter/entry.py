import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de entry')
ventana.iconbitmap('icono.ico')

# width cantidad de caracteres a ocupar en la caja

# show: para indiciar que componente se va mostrar independientemente
# de lo que escriba el usuario. Pero lo que escriba el usuario si se podra
# recuperar correctamente, es util por ejemplo cuando se escribe una contraseña 
# entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')

# state=tk.DISABLED: desabilita el componente. Si state tiene NORMAL
# se podra volver a caputar el texto con normalidad
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL)
entrada1.grid(row=0, column=0)
# insert agrefa un texto a la caja
entrada1.insert(0,'Introduce una cadena')
entrada1.insert(tk.END, '.')

# state='readonly' se configurar como solo lectura y no se podra modificar
# entrada1.config(state='readonly')

def enviar():
    # el metodo get obtiene el texto ingresado en la caja de texto
    print(entrada1.get())
    # recuperamos el texto ingresado en la caja de texto
    # y se lo enviamos al texto del boton
    boton1.config(text=entrada1.get())
    # para eliminar el contenido escrito en la caja de texto
    # se elimina desde el indice 0 hasta el final (END) de
    # la cadena de caracteres 
    # entrada1.delete(0,tk.END)

    # Selecionar el texto de la caja de texto
    entrada1.select_range(0, tk.END)
    # para hacer efectiva la selecion del texto
    entrada1.focus()

# Creamos un boton para que cada vez que lo presionemos
# nos imprima en la consola el texto ingresado, en la caja de texto
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()