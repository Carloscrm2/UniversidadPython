from Producto import Producto


class Orden:
    contador_ordenes = 0

    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._productos = list(productos)  # lista de productos

   # metodo para agregar productos de forma independiente
    def agregar_productos(self, producto):
        self._productos.append(producto)

    # metodo para calcular el total
    def calcular_total(self):
        total = 0
        for producto in self._productos:
            total += producto.precio # se accede al precio por el metodo getprecio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + '|'

        return f'Orden: {self._id_orden}, \nProductos: {productos_str}'

if __name__ == '__main__':
    producto1 = Producto('Camisa', 100.00)
    print(producto1)
    producto2 = Producto('Pantalodn', 150)
    productos1 = [producto1, producto2]
    orden1 = Orden(productos1)
    print(orden1)
    orden2 = Orden(productos1)
    print(orden2)
