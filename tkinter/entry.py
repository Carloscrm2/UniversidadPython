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
entrada1.config(state='readonly')

ventana.mainloop()