class Monitor:
    contadorMonitores = 0

    def __init__(self, marca, tamaño):
        self.idMonitor = Monitor.contadorMonitores = + 1
        self.marca = marca
        self.tamaño = tamaño

