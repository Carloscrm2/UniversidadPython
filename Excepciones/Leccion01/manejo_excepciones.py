# Manejo de excepciones

# 10/0 # De manera automática arroja una excepción por division entre 0

# para manejar esta excepción y nuestro programa no termine de manera
# abrupta, encerramos nuestro código en un try-exception

# importamos nuestra clase de Exception personalizada
from NumerosIdenticosException import NumerosIdenticosException

resultado = None
a = 10
b = 0
try:
    resultado = a / b
except Exception as e:
    print(f'Ocurrió un error: {e}')

# si tenemos un bloque try-exception y ocurre una excepción
# el código continuará ejecutándose
print(f'Resultado: {resultado}')  # como ocurrió una division por 0 la variable resultado sigue con el valor de none
print(f'Continuamos...')

# excepción de tipo TypeError: cuando los tipos de datos no
# son compatibles entre ellos
resultado = None
a = '10'
b = 0
try:
    resultado = a / b
except Exception as e:
    print(f'Ocurrió un error: {e}')

print(f'Resultado: {resultado}')
print(f'Continuamos...')

# la clase Exception es la clase padre de todas las clases
# de tipo Exception, solo las clases padre pueden procesar
# cualquier tipo de excepciones.

# Como vemos la clase ZeroDivisionError no puede procesar la excepción
# de tipo TypeError por lo que el programa termina de manera abrupta
# resultado = None
# a = '10'
# b = 0
# try:
#     resultado = a/b
# except ZeroDivisionError as e:
#     print(f'Ocurrió un error: {e}')
#
# print(f'Resultado: {resultado}')
# print(f'Continuamos...')


# Manejo de excepciones específicas

resultado = None
a = '10'
b = 0

# Como vimos en el ejemplo anterior la clase ZeroDivisionError
# no puede manejar las excepciones de tipo TypeError puesto, que
# la variable "a" tiene asignado el valor '10'
# por eso agregamos otro except especificando la clase TypeError

try:
    resultado = a/b
except ZeroDivisionError as e:
    print(f'Ocurrió un error: {e}, {type(e)}')  # con type(e) visualizamos el tipo de excepción que se está procesando
except TypeError as e:
    print(f'Ocurrió un error: {e}, {type(e)}')
except Exception as e:
    print(f'Ocurrio un error:{e}, {type(e)}')

# Al agregar el bloque except con la clase Exception (Clase padre de todas las excepciones)
# podemos hacer más genérico el bloque try-except, sin embargo hay que tener que contar
# que no debemos de poner la clase Exception hasta el principio si queremos que se haga la
# revisión de las clases hijas (ZeroDivisionError y TypeError)

print(f'Resultado: {resultado}')
print('Continuamos...')


# Al final de los bloques except podemos agregar dos bloques mas:
# el bloque else y el bloque finally

# El bloque else únicamente se va a ejecutar en caso de que no se haya lanzado
# ninguna excepción. El bloque finally independientemente que se arroje un error
# una excepción o no, siempre se va a ejecutar el bloque finally
a = 10
b = 10
try:
    # Ejemplo de uso de nuestra clase personalizada de Exception
    if a == b:
        # la palabra raise nos permite lanzar una excepción
        raise NumerosIdenticosException('números idénticos')
    resultado = a / b

except ZeroDivisionError as e:
    print(f'Ocurrió un error: {e}, {type(e)}')
except TypeError as e:
    print(f'Ocurrió un error: {e}, {type(e)}')
except Exception as e:
    print(f'Ocurrio un error:{e}, {type(e)}')
else:
    print('No se arrojo ninguna excepción')
finally:
    print('Ejecución del bloque finally')

