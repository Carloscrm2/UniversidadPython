# variables y tipos de datos

x = 10
y = 2
z = x + y
print(x)
print(y)
print(z)

# para obtener la direccion de memoria de una varibale
# se utiliza la funcion id()
print(id(x))

x = 10  # entero
print(x)

# para obtener que tipo de dato que es un variable

print(x)
print(type(x))

# podemos dar una "pista" del tipo de dato que podria
# estar apuntando nuestra variable con ":"

x: str = "Hola Mundo"  # string
print(x)
print(type(x))

x = 10.5  # float
print(x)
print(type(x))

x = True  # boole
print(x)
print(type(x))

# Manejo de cadenas
miGrupoFavorito = "The Beatles"

# En este caso el sigo + funciona como concatenacion
print("mi grupo favorito es: " + miGrupoFavorito)
# se puede concatenar cadenas utilizando ","
print("mi grupo favorito es:", miGrupoFavorito)

numero1 = "1"
numero2 = "2"
print("Concatenacion:", numero1 + numero2)
# para que se realice la suma de estos dos valores primero
# debemos convertirlos a tipos de dato entero
print("suma:", int(numero1) + int(numero2))

# Tipos bool
miVariable = True
print(miVariable)

# 3 es mayor que 2?
miVariable = 3 > 2
print(miVariable)  # true

if miVariable:
    print("El resultado fue verdadero")
else:
    print("El resultado fue falso")

# Funcion input para procesar la entrada del usuario
resultado = input("Escribe un mensaje: ")  # la funcion input regresa un tipo String (str)
print(resultado)
print("Fin del programa")

# Conversion de la entrada de datos
numero1 = int(input("Escribe el primer numero: "))
numero2 = int(input("Escribe el segundo numero: "))
resultado = numero1 + numero2  # sin el metodo int() no se realiza la suma se hace una concatenacion
print("El resultado de la suma es:", resultado)