# Primero abrimos un archivo

try:
    # open() abre un archivo ya existente o crea uno nuevo de manera automática
    # open('nombre archivo', 'w(escritura),r(lectura)')
    archivo = open('prueba.txt', 'w', encoding='utf8')
    archivo.write('Agregamos información al archivo\n') # para agregar información
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
    archivo.close() # close() cerramos el archivo, una vez cerrado el archivo
                    # no podemos agregar información