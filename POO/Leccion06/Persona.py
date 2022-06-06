class Persona:
    contador_personas = 0 # identificador unico para cada objeto que vayamos a crear

    def __init__(self, nombre, edad):
        Persona.contador_personas += 1  # incrementamos en uno cada que creamos un objeto
        self.id_persona = Persona.contador_personas
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'


persona1 = Persona('Juan', 28)
print(persona1)
persona2 = Persona('Karla', 30)
print(persona2)
print(f'valor contador personas: {Persona.contador_personas}')

