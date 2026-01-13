##objetos

class Persona:
    #funcion de inicializacion de la clase
    
    def __init__(self, nombre, edad):
        #atributos
        self.nombre = nombre
        self.edad = edad
        #estos que se definen dentro de esta funcion se conocen como atributos
         
    

persona1 = Persona("Diego", 34) #instanciar un objeto de una clase
persona2 = Persona("Patito", 18)
persona3 = Persona("Juan", 23)
persona4 = Persona("Marcela", 30)
persona5 = Persona("William", 19)

persona2.apellido = "de Goma" #atributo dinamico (por que se crea en esta linea)
print(persona2.nombre,persona2.edad)
print(persona2.apellido)
persona2.nombre = "Pedrito"
print(persona2.nombre)
persona2.direccion = "Calle P Sherman Wallaby 42 Sydney"
print(persona2.direccion)