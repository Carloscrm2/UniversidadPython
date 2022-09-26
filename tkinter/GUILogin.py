import sys
import tkinter as tk
from tkinter import ttk, messagebox

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('300x130')
        self.title('Login')

    # configuracion del grid
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self._crear_componentes()

    # Definir metodo crear componentes:
    def _crear_componentes(self):
        # Definimos las etiquetas
        label1 = ttk.Label(self, text='Usuario:')
        label1.grid(row=0, column=0)
        label2 = ttk.Label(self, text='Contraseña:')
        label2.grid(row=1, column=0, sticky='N')

        # Varibales asociadas a las cajas de texto
        self.user = tk.StringVar(value='')
        self.pas = tk.StringVar(value='')

        # Definimos las cajas de texto
        self.entrada1 = ttk.Entry(self, width=20, justify=tk.CENTER, textvariable=self.user)
        self.entrada1.grid(row=0, column=1, sticky='W')
        self.entrada2 = ttk.Entry(self, width=20, justify=tk.CENTER, show='*', textvariable=self.pas)
        self.entrada2.grid(row=1, column=1, sticky='WN')

        # Definimos el boton
        self.boton1 = ttk.Button(self, text='Login', command=self._login)
        self.boton1.grid(row=2, column=1, sticky='WN')
        
    def _login(self):
        messagebox.showinfo('Datos Login', 'Usuario: ' + self.user.get() + ', Password: ' + self.pas.get())



    
if __name__== '__main__':
    login_ventana = Login()
    login_ventana.mainloop()    