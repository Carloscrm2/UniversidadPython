from DispositivoEntrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contadorRatones = 0

    def __init__(self):
        self.idRaton = Raton.contadorRatones = + 1

    def __str__(self):
        return f'Raton: id:{self.idRaton}'


