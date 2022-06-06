# Definir una tupla
# La tupla al igual que la lista respeta el orden
# en que se agregan los elementos, con la diferencia
# de que no se pueden modificar
frutas = ('Naranja', 'Plátano', 'Guayaba')
print(frutas)
# saber el largo de una tupla
print(len(frutas))

# acceder a un elemento
print(frutas[0])

# navegacion inversa
print(frutas[-1]) # Guayaba

# acceder a un rango
print(frutas[0:1])  # no incluye el último indice indicado

# recorrer los elementos de una tupla
for fruta in frutas:
    print(fruta, end=' ') # parametro end para quitar los saltos de linea

# # cambiar valor de una tupla
# frutas[0] = 'Pera'
# print(frutas) # marca un error porque los valores en la tupla no se pueden modificar

# convertimos la tupla hacia una lista
frutasLista = list(frutas)
frutasLista[0] = 'Pera'
# convertimos la lista a una tupla
frutas = tuple(frutasLista)

print('\n',frutas)

# eliminar la tupla
del frutas
# print(frutas)

tupla = (13, 1, 8, 3, 2, 5, 8)

lista = []

for numeros in tupla:
    if numeros < 5:
        lista.append(numeros)

print(lista)

