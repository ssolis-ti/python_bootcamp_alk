"""¿En qué consistirá la Demo?
Crear un asistente bancario que reciba una opción numérica del usuario y devuelva información útil según el área seleccionada. El sistema debe permitir:
Elegir entre opciones del 1 al 5
Mostrar la respuesta según el área elegida
Mostrar un mensaje de advertencia si el número no es válido
🔢 Opciones disponibles:
Consultar saldo
Transferencias
Pago de servicios
Préstamos y créditos
Atención al cliente
"""
respuestas = {
    1: "Su saldo disponible es de $850.000.",
    2: "Puede realizar transferencias a cuentas propias o de terceros.",
    3: "Puede pagar servicios como luz, agua, gas e internet.",
    4: "Contamos con préstamos de consumo y créditos hipotecarios.",
    5: "Un ejecutivo se comunicará con usted para atención al cliente."
}

try:

    opcion_cliente = int(input("""
    BIENVENIDOS A BANCO MASTERPLOP

    Seleccione su consulta:
        1. Consultar saldo
        2. Transferencias
        3. Pago de servicios
        4. Préstamos y créditos
        5. Atención al cliente
        
    Ingrese aqui su opcion: """
    ))
    print("")
    match opcion_cliente:
        case 1:
            print(f"{respuestas[opcion_cliente]}")
        case 2:
            print(f"{respuestas[opcion_cliente]}")
        case 3:
            print(f"{respuestas[opcion_cliente]}")
        case 4:
            print(f"{respuestas[opcion_cliente]}")
        case 5:
            print(f"{respuestas[opcion_cliente]}")
        case _:
            print("Opcion no valida.")

except:
    print("Opcion no valida.")


####tarea para la casa realizar la consulta al diccionario usando get en vez de  la notacion de parentesis

