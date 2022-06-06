# pass: se utiliza para indicar que no se va a procesar nada mas
# y que unicamente se cree este tipo de dato

# el metodo __init__() se utiliza para agregar  e inicializar
#  atributos y metodos es similar a un constructor,
#  solo que en python el constructor
# queda oculto y se manda a llamar directamente por el lenguaje

class Persona:
    # def __init__(self):
    #     # estos son atributos de instancia (de objeto), no de la clase
    #     self.nombre = 'Juan'
    #     self.apellido = 'Perez'
    #     self.edad = 28

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    # Creamos un metodo para la clase
    def mostrar_detalle(self):  # La palabra self se agrega a todos los metodos de instancia
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

# Creamos un Objeto de tipo Persona
# persona1 = Persona()  # De manera indirecta se esta llamando al metodo __init__
# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

# Creación de objetos con parametros
persona1 = Persona('Carlos', 'Gómez', 23)
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

persona2 = Persona('Beatriz', 'Garcia', 40)
print(f'Objeto Persona 2: {persona2.nombre} {persona2.apellido} {persona2.edad}')

# modificar atributos de un objetos
persona1.nombre = 'Juan Carlos'
persona1.apellido = 'Juarez'
persona1.edad = 25
print(f'Objeto Persona 1: {persona1.nombre} {persona1.apellido} {persona1.edad}')

# Llamada del metodo de instancia
persona1.mostrar_detalle()
persona2.mostrar_detalle()

# Llamada del metodo de instancia utilizando el nombre de la clase
Persona.mostrar_detalle(persona1) # solo que ahora tenemos que pasar la referencia del objeto al que queremos acceder

# Se pueden agregar atributos a un objeto en cualquier momento
# solo que estos no se compartiran con los demas objetos
persona1.telefono = '5566023587'
print(persona1.telefono)
