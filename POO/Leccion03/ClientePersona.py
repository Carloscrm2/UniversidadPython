from Persona import *

persona1 = Persona('Juan', 28)
# al sobreescribir el metodo str en la clase persona
# se imprimen los valores asiganados al objeto persona1
print(persona1) # se manda a llamar al metodo str

empleado1 = Empleado('Karla', 30, 5000)
print(empleado1) # tambien se hereda el metodo str