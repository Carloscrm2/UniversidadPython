import psycopg2 as bd

conexion = bd.connect(
    user='postgres', password='admin', host='localhost', port='5432', database='test_db')

try:
    conexion.autocommit = False  # si no hacemos un commit al final, no se guardaran los cambiamos
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
    valores = ('Maria', 'Esparzadededddedededededede', 'mesparza@mail.com')
    cursor.execute(sentencia, valores)

    sentencia = 'UPDATE persona SET nombre = %s, apellido=%s, email=%s WHERE id_persona=%s'
    valores = ('Juan Carlos', 'Juarez', 'jcjuarez@mail.com', 1)
    cursor.execute(sentencia, valores)

    conexion.commit()  # Se guardan los cambios si no existe ningún problema
    print('Termina la transacción')
except Exception as e:
    conexion.rollback()  # si hubo un error llamamos al método rollback
    print(f'ocurrió un error, se hizo rollback: {e}')
finally:
    cursor.close()
