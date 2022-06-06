# importamos la clase Persona
# from archivo import clase

from Encapsulamiento import Persona

print('Creación de objetos'.center(50,'-'))
persona1 = Persona('Karla', 'Gomez', 30)
persona1.mostrar_detalle()

# Se destruyen los objetos para liberar ciertos recursos
print('Eliminacion objetos'.center(30,'-'))
del persona1