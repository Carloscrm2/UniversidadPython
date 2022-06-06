import os # contiene el método para eliminar un archivo
class CatalogoPeliculas:
    ruta_archivo = 'peliculas.txt'

    # los métodos de clase pueden acceder directamente
    # a los atributos de clase
    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r') as archivo:
            print('Catálogo de películas'.center(50, '-'))
            print(archivo.read())

    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo eliminado: {cls.ruta_archivo}')
