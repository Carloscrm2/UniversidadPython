class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
  # tambien se puede hacer una sobrecarga de operadores
  # a nivel de clases
    def __add__(self, other):
        return self.nombre + other.nombre

    # sobrecarga del metodo resta
    def __sub__(self, other):
        return self.edad - other.edad

# obj + obj2 seria equivalente a
# obj1.__add__(obj2)

persona1 = Persona('Juan', 28)
persona2 = Persona('Carlos', 50)
print(persona1 + persona2)  # se concatena el valor de los dos objetos
print(persona1 - persona2)  # se resta el valor de las edades de los objetos




