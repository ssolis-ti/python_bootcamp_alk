"""Tenemos un sistema de reservas de un cine. Dependiendo del tipo de usuario (cliente regular, estudiante, jubilado,  etc.), el sistema debe aplicar un descuento diferente en la compra del boleto. Si el tipo de usuario no está en la lista, el precio se mantiene normal.
1. ¿Cuántas condiciones debemos evaluar en este problema?
2. ¿Qué estructura condicional nos ayudaría a organizarlo mejor?
3. ¿Cómo evitar repetir código innecesario?
4. ¿Qué pasaría si el usuario ingresa un tipo no reconocido?
"""
opcion_cliente = input("Ingrese el tipo de cliente (cliente regular, estudiante, jubilado): ").strip().lower()
#strip() o metodo strip quita los espacios del comienzo y el final
#lower() metodo que permite pasar todo el texto a minuscula

if opcion_cliente == "cliente regular":
    print("el precio de la entrada es $8000")

elif opcion_cliente == 'estudiante':
    print("el precio de las entrada es de $4000")

elif opcion_cliente == "jubilado":
    print("la entrada cuesta $3200")

else:
    print("Tipo de cliente no valido")
