from computadora import Computadora
from monitor import Monitor
from orden import Orden
from raton import Raton
from teclado import Teclado

teclado1 = Teclado('Hp', 'USB')
raton1 = Raton('Hp', 'USB')
monitor1 = Monitor('HP', 15)
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('Acer', 'Bluetooth')
raton2 = Raton('Acer', 'Bluetooth')
monitor2 = Monitor('Acer', 27)
computadora2 = Computadora('Acer', monitor2, teclado2, raton2)

computadoras1 = [computadora1, computadora2]

orden1 = Orden(computadoras1)
print(orden1)