class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura


base = float(input('Proporciona la base: '))
altura = float(input('Proporciona la altura: '))

rectangulo = Rectangulo(base, altura)
print(f'Area = {rectangulo.calcular_area()}')