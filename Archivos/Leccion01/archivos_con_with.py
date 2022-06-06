# El uso de with nos permite usar de manera simplificada
# el uso de archivos, ya no es necesario usar un bloque try-except
# además de que with abre y cierra el archivo de manera automática
# no es necesario usar la sentencia close()

# with open('prueba.txt', 'r') as archivo:
#     print(archivo.read()) # recuperamos la info del archivo


# Mandamos a llamar nuestra clase de ManejoArchivos
from ManejoArchivos import ManejoArchivos

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())


