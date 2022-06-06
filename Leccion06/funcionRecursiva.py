# funcion recursiva: es una funcion que se llama a si misma
# para terminar de completar una tarea

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)

resultado = factorial(5)
print(f'El factorial de 5 es {resultado}')


# ejercicio: imprimir numeros de 5 al 1 usando una funcion
# recursiva
def imprimirNumeros(numero):
    if numero >= 1:
        print(numero)
        imprimirNumeros(numero-1)

imprimirNumeros(-1)

# Ejercicio: Crear una función para calcular el total
# de un pago incluyendo un impuesto aplicado.

def calcular_total(pago_sin_impuesto, impuesto):
    total = pago_sin_impuesto + (pago_sin_imuesto*impuesto)/100
    print(f'total = {total}')

pago_sin_imuesto = float(input("ingrese el pago sin impuesto: "))
impuesto = float(input("ingrese el impuesto: "))
calcular_total(pago_sin_imuesto, impuesto)
