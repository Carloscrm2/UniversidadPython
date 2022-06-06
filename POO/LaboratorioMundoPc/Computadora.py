class Computadora:
    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        self._idComputadora = Computadora.contadorComputadoras = + 1
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'Computadora: id: {self._idComputadora}, nombre: {self._nombre}, monitor: {self._monitor}' \
               f'teclado: {self._teclado}, raton: {self._raton}'

    @property
    def idComputadora(self):
        return self._idComputadora

    @property
    def nombre(self):
        return self._nombre

    @property
    def monitor(self):
        return self._monitor

    @property
    def teclado(self):
        return self._teclado

    @property
    def raton(self):
        return self._raton

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @raton.setter
    def raton(self, raton):
        self._raton = raton

