class MiClase:
    # cuando se define una variable fuera del metodo
    # init entonces esta variable sera una variable de clase
    variable_clase = 'Valor variable clase'

    # esta variable se va a poder compartir con todos los objetos
    # creados de esta clase
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    # metodo estatico: se asocia con la clase y no con los objetos
    # no pueden acceder directamente a las variables de instancia
    # debemos de usar el nombre de la clase para poder hacerlo
    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    # metodo de clase:
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_instancia)
        print(self.variable_clase)

# no es necesario crear un objeto para mandar llamar a una variable
# de clase
print(MiClase.variable_clase)

miClase = MiClase('Valor variable instancia')
print(miClase.variable_instancia)
print(miClase.variable_clase)

miClase2 = MiClase('Otro valor variable de instancia')
print(miClase2.variable_instancia)

# tambien se pueden crear variables de clase al vuelo(en cualquier momento)
MiClase.variable_clase2 = 'Valor variable clase 2'

print(miClase2.variable_instancia)
print(miClase2.variable_clase)
print(miClase.variable_clase2)
print(miClase2.variable_clase2)

# para acceder al metodo estatico debemos usar el nombre de la clase
MiClase.metodo_estatico()

# mandamos a llamar el metodo de clase
MiClase.metodo_clase()

