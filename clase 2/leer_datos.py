###Leer -> input
#input permite interactuar con el usuario y alamacenar su respuesta en una variable
input("pulse enter para continuar")
nombre = input("Ingrese su nombre por favor: ")
apellido = input("Ingrese su apellido por favor: ")
edad = input("Ingrese su edad por favor: ")

#que tipo de dato creen que es la edad al ingresar al sistema?

print("el tipo de dato de edad es",type(edad)) #la funcion type me entrega el tipo de dato que es una varibale o estructura
print("")
print("Hola soy " + nombre + " " +apellido +" y mi edad es " + edad)

edad = float(edad) #convierte el texto a numero decimal
if edad >= 18: #si edad es mayor o igual a 18
    print("Es mayor de edad, puede manejar") #en caso que la condicion sea True
else:
    print("no tiene permitido manejar") #en caso que la condicion no se cumpla




#print(nombre, apellido, edad)
# print(f"Hola soy {nombre} {apellido} y mi edad es {edad}")