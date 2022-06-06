class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Color: {self.color} Ruedas: {self.ruedas}'

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super(Coche, self).__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'{super.__str__()} Velocidad: {self.velocidad}'

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super(Bicicleta, self).__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'{super.__str__()} tipo:{self.tipo}'
