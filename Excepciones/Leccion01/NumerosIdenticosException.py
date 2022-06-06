# Clases de Excepciones personalizadas

# Cualquier clase personalizada que deseemos crear
# debe de heredar de la clase Exception
class NumerosIdenticosException(Exception):

    def __init__(self, mensaje):
        self.message = mensaje