
dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miercoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sabado",
    7: "Domingo",
}
# #el diccionario se compone de pares de elementos que se comportan como llave : valor, key:value

# print(dias[1])#lunes
# print(dias[2])
# print(dias[3])
# print(dias[4])
# # print(dias[8])

# print(dias.get(5)) #esta opcion nos permite devolver algo en caso de que se cometa un error
# print(dias.get(6))
# print(dias.get(7))
# print(dias.get(8, "esta llave no existe")) #si no coloco el segundo argumento devuelve None

# ####en python no existe la estructura switch, pero si la match case

dia_semana = int(input("""
        Ingrese el numero del dia de  la semana: """))

match dia_semana:
    case 1:
        print("El dia de hoy es lunes")
    case 2:
        print("El dia de hoy es Martes")
    case 3:
        print("El dia de hoy es Miercoles")
    case 4:
        print("El dia de hoy es Jueves")
    case 5:  
        print("El dia de hoy es Viernes")
    case 6:
        print("El dia de hoy es Sabado")
    case 7:
        print("El dia de hoy es Domingo")
    case _:
        print("EL numero ingresado no corresponde a un dia de la semana")