# Con el _ indica que no debemos acceder a los atriibutos de
# nuestra clase de manera directa y mucho menos modificar sus valores
# unicamente se puede hacer dentro de la misma clase, aunque python no
# hace ningún tipo de restricción si deseamos hacerlo

# pero con __ ya quedara estrictamente prohibido acceder o modifcar los atributos de
# la clase si no se hace dentro de la misma clase, aunque esta notacion no
# se usa
class Persona:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

# Con los métodos get y set podremos acceder y modificar los atributos
    @property
    def nombre(self):
        print('Llamndo al método get')
        return self._nombre

# Con el metodo set modificamos el atributo
    @nombre.setter
    def nombre(self, nombre):
        print('Llamando método set nombre')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    # Creamos un metodo para la clase
    def mostrar_detalle(self):  # La palabra self se agrega a todos los metodos de instancia
        print(f'Persona: {self._nombre} {self._apellido} {self._edad}')

   # Metodo destructor de objetos
    def __del__(self):
        print(f'Persona: {self._nombre} {self._apellido}')

persona1 = Persona('Juan', 'Perez', 20)

# Con el decordador @property podremos llamar de manera indirecta
# al metodo get de nombre ya no es necesario poner el parentesis (nombre())
print(persona1.nombre)
persona1.nombre = 'Juan Carlos' # se manda a llamar al metodo setter indirectamente
