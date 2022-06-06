# ciclo while
# condicion = True
#
# while condicion:
#     print('Ejecutando ciclo while')
# else:
#     print('Fin del ciclo while')


contador = 0
while contador < 3:
    print(contador)
    contador += 1  # contador = contador + 1
else:
    print('Fin ciclo while')

# ciclo for
cadena = 'Hola'
for letra in cadena:
    print(letra)
else:
    print('Fin ciclo for')

# palabra break
for letra in 'Holanda':
    if letra == 'a':
        print(f'Letra encontrada: {letra}')
        break;
else:
    print('Fin ciclo for')

# palabra continue
# imprimimos los valores de i hasta el 6
for i in range(6):
    print(f'valor: {i}')

# imprimimos unicamente los numeros pares
# for i in range(6):
#     if i % 2 == 0:
#         print(f'valor: {i}')

# el ejercicio anterior pero con la palabra continue
for i in range(6):
    if i % 2 != 0:
        continue
    print(f'valor: {i}')