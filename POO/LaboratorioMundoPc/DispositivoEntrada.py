class DispositivoEntrada:
    def __init__(self, tipoEntrada, marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @property
    def marca(self):
        return self._marca

    def __str__(self):
        return f'Dispositivo entrada :[tipo entrada: {self._tipoEntrada}, marca: {self._marca}]'

    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada

    @marca.setter
    def marca(self, marca):
        self._marca = marca