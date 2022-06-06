import psycopg2  # para poder conectarnos a Posgresql

# método que nos permite conectarnos a posgres
conexion = psycopg2.connect(
    user='postgres', password='admin', host='localhost', port='5432', database='test_db')

# Cursor: objeto que nos permite ejecutar sentencias sql
# cursor = conexion.cursor()
# sentencia = 'SELECT * FROM persona'
# cursor.execute(sentencia)
# # recuperamos todos los registros de la sentencia ejecutada
# registros = cursor.fetchall()
# print(registros)
# # cerramos el cursos
# cursor.close()
# # cerramos la conexión
# conexion.close()

# with no puede cerrar automáticamente la conexión
# por eso la sentencia close() la encerramos en un bloque
# try-except
try:
    # con el uso de with se cierra automáticamente el cursor
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM persona'
            cursor.execute(sentencia)
            registros = cursor.fetchall()  # con fetchall() recuperamos todos los registros
            print(registros)
except Exception as e:
    print(f'ocurrio un error: {e}')
finally:
    cursor.close()

try:
    # con el uso de with se cierra automáticamente el cursor
    with conexion:
        with conexion.cursor() as cursor:
            # El '%s' es un parametro posicional o Placeholder
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = 2
            # A la sentencia execute() le pasamos una tupla con el parámetro id_persona
            # se agregar una coma para que sea una tupla
            cursor.execute(sentencia, (id_persona,))
            registros = cursor.fetchone()  # con fetchone() recuperamos solo un registros
            print(registros)
except Exception as e:
    print(f'ocurrio un error: {e}')
finally:
    cursor.close()

try:
    with conexion:
        with conexion.cursor() as cursor:
            # Con la sentencia IN podemos procesar varios registros
            sentencia = 'SELECT * FROM persona WHERE id_persona IN (1,2)'
            cursor.execute(sentencia)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
    print(f'ocurrio un error: {e}')
finally:
    cursor.close()

# Insertar Registros con Pyscopg
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = ('Carlos', 'Lara', 'clara@mail.com')
            cursor.execute(sentencia, valores)
        # como estamos insertando datos en la BD debemos guardar estos cambios
        # esto lo hacemos con la función commit()
        #     conexion.commit()
        # sin embargo al usar with, el commit se ejecuta en automático,
        # así que no hay que colocarlo manualmente
        registros_insertados = cursor.rowcount
        print(f'registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'ocurrio un error: {e}')
finally:
    cursor.close()


# insertar varios registros
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (('Angel', 'Quintana', 'aquintana@mail.com'),
                       ('Maria', 'Gonzales', 'mgonzales@mail.com'),
                       ('Marcos', 'Cantu', 'mcantu@mail.com'))
            # con executemany insertamos varios registros
            cursor.executemany(sentencia, valores)
        registros_insertados = cursor.rowcount
        print(f'registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'ocurrió un error: {e}')
finally:
    cursor.close()

# actualizar registro
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com', 1)
            cursor.execute(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'ocurrió un error: {e}')
finally:
    cursor.close()

# actualizar varios registros
# como vemos es muy similar a cuando insertamos varios registros
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = (('Juan', 'Perez', 'jperez@mail.com', 1),
                       ('Ivonne', 'Gutierrez', 'igutierrez@mail', 2) )
            cursor.executemany(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'ocurrió un error: {e}')
finally:
    cursor.close()

# eliminar registro
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            valores = (7,)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')
except Exception as e:
    print(f'ocurrió un error: {e}')
finally:
    cursor.close()

# eliminar varios registros
try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'DELETE FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id_persona a eliminar (separados po coma): ')
            # el metodo split() regresa una lista, por ello se tiene que convertir a una tupla
            valores = (tuple(entrada.split(',')),)
            cursor.execute(sentencia, valores)
            registros_eliminados = cursor.rowcount
            print(f'Registros Eliminados: {registros_eliminados}')
except Exception as e:
    print(f'ocurrió un error: {e}')
finally:
    cursor.close()
