"""
Crea una clase Coche con los atributos marca, modelo, año y color.
Solicita al usuario los datos del coche y crea una instancia de la clase.
Usa condicionales (if-else) para verificar si el coche es nuevo (año >= 2022) o usado (año < 2022).
Implementa un bucle while para permitir modificar atributos del coche hasta que el usuario decida salir.
Utiliza break para salir del menú cuando el usuario lo indique.
Usa continue para repetir el menú sin realizar cambios si el usuario ingresa una opción inválida.
Imprime la información final del coche antes de terminar el programa.

paso a paso
1. Definir la clase Coche con los atributos mencionados.
2. Pedir los datos del coche y crear un objeto de la clase.
3. Evaluar con if-else si el coche es nuevo o usado.
4. Crear un menú interactivo (while) que permita modificar atributos.
5. Implementar break para salir del menú.
6. Usar continue para manejar entradas incorrectas.
7. Mostrar la información final del coche antes de terminar el programa.

"""

#paso1

class Coche:
    #funcion de inicializacion
    def __init__(self, marca, modelo, anno, color):
        self.marca = marca
        self.modelo = modelo
        self.anno = anno
        self.color = color


marca_coche = input("Ingrese la marca del coche: ")
modelo_coche = input("Ingrese el modelo del coche: ")
anno_coche = input("Ingrese el año del coche: ") #por ahora vamos a confiar en el usario, pero esto deberia validarse antes de continuar
color_coche = input("Ingrese el color del coche: ")

    
# if not anno_coche.isdigit(): # devuelve True si el valor del dato es entero positivo
#     print("ingrese un año valido")


coche = Coche(marca_coche, modelo_coche, anno_coche, color_coche)

if int(coche.anno)>=2022:
    print("el coche es nuevo")
    coche.condicion = "nuevo"
else:
    print("el coche es usado")
    coche.condicion = "usado"

condicion = True
while condicion:
    print("""
    Bienvenido al sistema de coches, ingrese la opcion a modificar:
    1. Modificar la marca
    2. Modiciar modelo
    3. Modificar el año
    4. Modificar color
    5. Imprimir datos actuales del coche
    6. Salir del Programa      
    """)
    opcion_elegida = input("Seleccione la opcion a realizar: ")
    
    if opcion_elegida == '1':
        print(f"La marca actual es {coche.marca}")
        actualizacion_marca = input("Ingrese la nueva marca: ")
        coche.marca = actualizacion_marca

    elif opcion_elegida == '2':
        print(f"El modelo actual del coche es {coche.modelo}")
        actualizacion_modelo = input("Ingrese el nuevo modelo: ")
        coche.modelo = actualizacion_modelo

    elif opcion_elegida == '3':
        print(f"El año actual del coche es {coche.anno}")
        actualizacion_anno = input("Ingrese el nuevo año del coche: ")
        if not actualizacion_anno.isdigit():
            print("año no valido, Intentelo nuevamente")
            continue
        coche.anno = actualizacion_anno
        if int(coche.anno)>=2022:
            print("el coche es nuevo")
            coche.condicion = "nuevo"
        else:
            print("el coche es usado")
            coche.condicion = "usado"

    elif opcion_elegida =='4':
        print(f"El color actual del coche es {coche.color}")
        actualizacion_color = input("Ingrese el nuevo color: ")
        coche.color = actualizacion_color
    
    elif opcion_elegida == '5':
        print(f"""
        Los datos Actuales del coche son:
        marca: {coche.marca}
        modelo: {coche.modelo}
        año: {coche.anno}
        color: {coche.color}
        condicion: {coche.condicion}
        """)

    elif opcion_elegida == '6':
        print(f"""
        Los datos finales del coche son:
        marca: {coche.marca}
        modelo: {coche.modelo}
        año: {coche.anno}
        color: {coche.color}
        condicion: {coche.condicion}
        """)
        
        print("Saliendo del programa....")
        
        break

    else:
        print("opcion no valida intentelo nuevamente")