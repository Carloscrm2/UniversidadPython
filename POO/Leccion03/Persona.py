class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    # sobreescribimos el metodo str
    def __str__(self):
        return f'Persona: {self.nombre} {self.edad}'

# se pone entre parentesis el nombre de la clase que se va heredar
class Empleado(Persona):
    # se deben colocar los atributos de la clase padre
    def __init__(self, nombre,edad,sueldo):
 # se manda a llamar al constructor de la clase padre
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    def __str__(self):
        return  f'{super().__str__()} Sueldo: {self.sueldo}'


empleado1 = Empleado('Juan',28,5000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

