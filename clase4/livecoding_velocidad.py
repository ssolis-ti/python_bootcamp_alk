"""
Aplicar un condicional simple (if) para detectar si un vehículo supera el límite de velocidad permitido.
.Vamos a imaginar que estamos diseñando un sistema que detecta si un conductor excede la velocidad máxima permitida en una zona. Si supera los 60 km/h, el sistema debe advertirlo
1.Lo primero que haremos es pedirle al usuario que ingrese su velocidad actual. Como es un número con decimales, lo convertiremos a float.
2.Luego usaremos una estructura if para verificar si la velocidad ingresada es mayor a 60. Si lo es, mostraremos un mensaje de advertencia.

"""

velocidad_usuario = float(input("Por favor ingrese su velocidad actual (Km/h): "))
#confiaremos en que el usuario ingresara un numero

if velocidad_usuario > 60:
    print(f"su velocidad {velocidad_usuario} Km/h supera el limite permitido,Favor reducirla a menos de 60 km/h")