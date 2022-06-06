try:
    archivo = open('prueba.txt', 'r')
    # print(archivo.read())  # leemos la información del archivo

# Leer algunos caracteres
#     print(archivo.read(5))  # leemos los primeros 5 caracteres
#     print(archivo.read(3))  # leemos los siguientes 3 caracteres

# Leer líneas completas
#     print(archivo.readline())  # leemos la primera línea
#     print(archivo.readline())  # leemos la segunda línea

# iterar el archivo
#     for linea in archivo:
#         print(linea)

# Leer todas las líneas
#     print(archivo.readlines())  # regresa una lista

# Acceder a una línea de la lista
#     print(archivo.readlines()[0])  # regresa la primera línea

# abrimos un nuevo archivo
# a - anexar información
    archivo2 = open('copia.txt', 'a')
    archivo2.write(archivo.read())  # copiamos el archivo a archivo2
except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()