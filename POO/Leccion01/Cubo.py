class Cubo:
    def __init__(self, ancho, profundo, alto):
        self.ancho = ancho
        self.profundo = profundo
        self.alto = alto

    def calcular_volumen(self):
        return self.ancho * self.profundo * self.alto


ancho = float(input('Ingrese el ancho: '))
profundo = float(input('Ingrese el profundo: '))
alto = float(input('Ingrese el alto: '))

cubo = Cubo(ancho, profundo, alto)
print(f'volumen del cubo: {cubo.calcular_volumen()}')