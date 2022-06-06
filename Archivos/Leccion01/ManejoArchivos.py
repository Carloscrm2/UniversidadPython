class ManejoArchivos:
    def __init__(self, nombre):
        self.nombre = nombre

  # En este método indicamos como obtener este recurso
    def __enter__(self):
        print('Obtenemos el recurso'.center(50, '-')) # centramos este texto
        self.nombre = open(self.nombre, 'r') # abrimos el archivo
        return self.nombre

   # Se manda a llamar automáticamente cuando terminamos de usar el archivo
    def __exit__(self, tipo_excepcion, valor_excepcion, traza_error):
        print('Cerramos el recurso'.center(50, '_'))
        if self.nombre:
            self.nombre.close()