# Funciones
def mi_funcion():
    print('saludos desde mi funcion')

mi_funcion()
# no se puede mandar a llamar una función sin definirla previamente

def mi_funcion_con_argumentos(nombre, apellido):
    print('saludos desde mi funcion')
    print(f'Nombre: {nombre}, Apellido: {apellido}')

mi_funcion_con_argumentos('Juan', 'Perez')


# palabra return
def sumar(a, b):
    return a + b

resultado = sumar(5,10)
print(f'resultado sumar= {resultado}')

# valores por default de los parámetros

def sumar(a = 0, b = 0):
    return a + b

# si mandamos a llamar a la funcion sumar sin pasarle
# argumentos por default regresará un valor de 0

print(f'resultado de sumar = {sumar()}')

# Argumentos variables
# cuando no sabemos la cantidad de elementos que vamos a recibir
# anteponemos un *, de manera interna python lo va a convertir en una tupla
def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)

listarNombres('Juan', 'Karla', 'Maria', 'Ernesto')

# TAREA: Función con argumentos variables
# para sumar todos los valores recibidos

def sumar(*numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    else:
        return suma

print(f'resultado de la suma: {sumar(5,4,3,2,1)}')

# TAREA: Función con argumentos variables
# para multiplicar todos los valores recibidos
def multiplicar(*numeros):
    multiplicacion = 1
    for numero in numeros:
        multiplicacion *= numero
    return multiplicacion

print(f'resultado de la multiplicacion:{multiplicar(5,4,3,2,1)}')

# Argumentos variables llave-valor
# con el ** podremos recibir diccionarios

def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}:{valor}')

listarTerminos(IDE='Integrated Development Environment', PK='Primary Key')
listarTerminos(DBMS='Database Managment System')

# Distintos tipos de datos como argumentos

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan', 'Karla', 'Guillermo']
desplegarNombres(nombres)
desplegarNombres('Carlos') # itera cada elemento de la cadena
# desplegarNombres(10) # no se puede iterar un tipo entero
desplegarNombres((10, 11)) # tupla de 2 elementos
desplegarNombres([10, 11]) # lista de 2 elementos