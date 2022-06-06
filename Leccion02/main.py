operandoA = 3
operandoB = 2
suma = operandoA + operandoB
print('resultado de la suma:', suma)
print(f'Resultado suma: {suma}')
resta = operandoA - operandoB
print(f'Resultado resta: {resta}')
multiplicacion = operandoA * operandoB
print(f'resultado multiplicacion: {multiplicacion}')
division = operandoA / operandoB
print(f'resultado division: {division}')
# utilizamos // para que la division regrese un valor entero
division = operandoA // operandoB
print(f'resultado de la division (int): {division}')
modulo = operandoA % operandoB
print(f'Resultado residuo division (modulo): {modulo}')
exponente = operandoA ** operandoB  # 3^2
print(f'resultado exponente: {exponente}')

# Operadores de asignacion =
miVariable = 10
print(miVariable)

# Operadores de reasignacion
miVariable = miVariable + 1
print(miVariable)
# sintaxsis reducida
miVariable += 1  # Es lo mismo que miVariable = miVariable + 1
print(miVariable)

miVariable -= 2
print(miVariable)  # Le restamos 2

miVariable *= 3
print(miVariable)  # multiplicamos por 3

miVariable /= 2
print(miVariable)  # dividimos entre 2

# Operadores de comparacion
a = 4
b = 2

resultado = a == b  # ¿a es igual a b?
print(f'Resultado == : {resultado}')

resultado = a != b  # ¿a es diferente de b?
print(f'Resultado != : {resultado}')

resultado = a > b  # ¿a es mayor que b?
print(f'Resultado > : {resultado}')

resultado = a >= b  # ¿a es mayor igual que b?
print(f'Resultado >= : {resultado}')

# operadores logicos
a = True
b = False
resultado = a and b
print(resultado)

resultado = a or b
print(resultado)

resultado = not a
print(resultado)  # invierte el valor de a
