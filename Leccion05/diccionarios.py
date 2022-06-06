# diccionarios estan compuestos por:
# dict (key, value)
# se parece a un set() en el sentido de que no hay indices

diccionario = {
    'IDE': 'Integrated Development Enviornment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Managment System'
}
print(diccionario)

# para saber el largo
print(len(diccionario))

# acceder a un elemento debemos indicar la (key)
print(diccionario['IDE'])
# otra forma de recuperar un elemento, también se indica la llave
print(diccionario.get('OOP'))

# modificando elementos
diccionario['IDE'] = 'integrated development environment'
print(diccionario)

# recorrer los elementos
for termino, valor in diccionario.items(): # items() nos permite regresar los elementos separados por termino y valor
    print(termino, valor)

# si queremos recuperar unicamente los terminos
for termino in diccionario.keys(): # keys() recuperamos unicamente los terminos
    print(termino)

# si queremos recuperar unicamente los valores asociados
# a cada uno de los terminos
for valor in diccionario.values():
    print(valor)

# comprobar existencia de algún elemento
print('IDE' in diccionario)

# agregar un elemento
diccionario['PK'] = 'Primary Key'
print(diccionario)

# no es posible agregar llaves duplicadas
# si agregamos una llave existente sobreescribe la llave con
# el nuevo valor

# remover un elemento
diccionario.pop('DBMS') # se debe indicar con la llave
print(diccionario)

# limpiar el diccionario
diccionario.clear()
print(diccionario)

# eliminar por completo el diccionario
del diccionario
print(diccionario)