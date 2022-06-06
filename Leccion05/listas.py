# listas
nombres = ['Juan', 'Karla', 'Ricardo', 'Maria']
# imprimir la lista nombre
print(nombres)
# acceder a los elementos de una lista
print(nombres[0])
print(nombres[1])
# acceder a los elementos de manera inversa
print(nombres[-1])  #  Maria
print(nombres[-2])  # Ricardo
# imprimir un rango
print(nombres[0:2])  # no incluye el indice 2
# ir al incio de la lista al indice (sin incluirlo)
print(nombres[:3])
# Desde el indice indicado hasta el final
print(nombres[1:])
# cambiar un valor especificando un indice
nombres[3] = 'Ivone'
print(nombres)
# iterar una lista
for nombre in nombres:
    print(nombre)
else:
    print('No existen mas nombres en la lista')

# preguntar el largo de una lista
print(len(nombres))
# agregar un elemento a la lista
nombres.append('Lorenzo')
print(nombres)

# insertar un elemento en un indice en especifico
nombres.insert(1, 'Octavio')
print(nombres) # los demas elementos se mueven hacia la derecha

# remover un elemento
nombres.remove('Octavio')
print(nombres)

# remover el ultimo valor de la lista
nombres.pop()
print(nombres)

# eliminar un elemento en un indice indicado
del nombres[0]
print(nombres)

# limpiar todos los elementos de la lista
nombres.clear()
print(nombres)

# borrar la lista por completo
del nombres
print(nombres)
