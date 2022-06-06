from FiguraGeometrica import FiguraGeometrica
from Color import Color

# el orden en que se escriben la clases a heredar importa
# se mandará a llamar primero la clase FiguraGeomtrica,
# después la de color
class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #se debe mandar a llamar el metodo self de manera
        # obligada cuando se hace herencia multiple
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    # Metodo para calcular el area
    def calcular_area(self):
        return self.alto * self.ancho

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}'