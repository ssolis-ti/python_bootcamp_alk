"""Tenemos un sistema de recomendación de vestimenta según la temperatura del día. Dependiendo de la temperatura ingresada por el usuario, el programa sugiere qué tipo de ropa usar:
🥶Menos de 10°C → Abrigo grueso y bufanda
😶‍🌫️Entre 10°C y 20°C → Chaqueta ligera
😎Entre 20°C y 30°C → Ropa cómoda y fresca
🥵Más de 30°C → Ropa ligera y protector solar
Si el usuario ingresa un valor fuera de rango o no numérico, el sistema deberá indicar un mensaje de error.

Sistema de recomendación de vestimenta 
¿Cuántas condiciones debemos evaluar en este problema? R: 4
¿Qué estructura condicional nos ayudaría a organizarlo mejor? R: condicional multiple
¿Cómo asegurarnos de que se cubran todos los rangos de temperatura sin solapamientos? R:
debemos tener en cuenta las condiciones que colocamos, suponiendo que temperatura es la varibable ingresada por el usuario
condiciones:

temperatura < 10
10 <= temperatura <=20 
20 < temperatura <= 30
teperatura > 30
 #correccion de las temperaturas en caso de ingresar un dato de tipo decimal o float

¿Qué pasa si el usuario ingresa un valor inválido, como letras o números negativos?

R:
los numeros negativos si podrian considerarse en el caso de temperatura <10.
en el caso de letas u otros valores deberiamos enviar un mensaje de que el dato ingresado no es valido



1. Pídele al usuario que ingrese la temperatura del día.
2. Convierte ese valor a tipo numérico (usá int() o float()).
3. Implementa una estructura condicional (if, elif, else) que cubra los siguientes rangos:
4. Menos de 10°C → Mostrar: "🧥 Usá abrigo grueso y bufanda"
5. Entre 10°C y 20°C inclusive → Mostrar: "🧣 Usá chaqueta ligera"
6. Entre 20°C y 30°C inclusive → Mostrar: "🩳 Usá ropa cómoda y fresca"
7. Más de 30°C → Mostrar: "🧢 Usá ropa ligera y protector solar"
8. Si el usuario ingresa un valor inválido (texto, negativo, etc.), muestra un mensaje de error.

"""
#extra manejo de errores en python

try:

    temperatura = float(input("Ingrese la temperatura actual en °C: "))
    
    if temperatura < 10:
        print("🧥 Usar abrigo grueso y bufanda")
    elif 10<= temperatura <= 20:
        print("🧣 Usar chaqueta ligera")
    elif 20 < temperatura <= 30:
        print("🩳 Usar ropa cómoda y fresca")

    elif temperatura > 30 :
        print("🧢 Usar ropa ligera y protector solar")

    else:
        print("Temperatura no valida")

except:

    print("se ha ingresado una temperatura no valida")
