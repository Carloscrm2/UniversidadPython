from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, 'rojo')
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(cuadrado1.calcular_area())

# MRO - Method Resolution Order
# nos permite saber la jerarquia de clase, de la clase
# a la cual mandamos a llamar este metodo

print(Cuadrado.mro())