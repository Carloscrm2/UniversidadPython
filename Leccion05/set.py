# definimos una coleccion de tipo set
# no respeta el orden, es totalmente aleatorio y no acepta
# elementos duplicados
planetas = {'Marte', 'Jupiter', 'Venus'}
print(planetas)

# conocer el largo
print(len(planetas))

# revisar si un elemento esta presente
print('Marte' in planetas) # regresa un booleano

# agregar un elemento
planetas.add('Tierra')
print(planetas)

# no se pueden duplicar elementos
planetas.add('Tierra')
print(planetas)

# eliminar elemento posiblemente arrojando un error (en caso de que no lo encuentre)
planetas.remove('Tierra')
print(planetas)

# eliminar elemento pero sin arrojar error en caso de no exisitir el elemento
planetas.discard('Jupiter')
print(planetas)

# limpiar por completo el set
planetas.clear()
print(planetas)

# eliminar por completo el set
del planetas
print(planetas)