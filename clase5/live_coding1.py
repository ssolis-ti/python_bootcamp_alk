
menu = {
    1: "Lentejas con arroz y ensalada de tomate",
    2: "Tallarinata con salsa de carne",
    3: "Porotos granados",
    4: "Pollo al horno con papas cocidas y ensalada chilena",
    5: "Pescado frito al horno con puré y ensalada",
    6: "Carbonada de vacuno",
    7: "Cazuela de vacuno o pollo",
}

try:
    dia_semana = int(input("""
    1. Lunes
    2. Martes
    3. Miercoles
    4. Jueves
    5. Viernes
    6. Sabado
    7. Domingo
    
Ingrese la opcion correspondiente al dia de la semana: """))

    match dia_semana:
        case 1:
            print("El dia de hoy es lunes")
            print(f"El menu del dia es {menu[dia_semana]}")
        case 2:
            print("El dia de hoy es Martes")            
            print(f"El menu del dia es {menu[dia_semana]}")
            
        case 3:
            print("El dia de hoy es Miercoles")
            print(f"El menu del dia es {menu[dia_semana]}")
        case 4:
            print("El dia de hoy es Jueves")
            print(f"El menu del dia es {menu[dia_semana]}")            
        case 5:  
            print("El dia de hoy es Viernes")
            print(f"El menu del dia es {menu[dia_semana]}")
        case 6:
            print("El dia de hoy es Sabado")
            print(f"El menu del dia es {menu[dia_semana]}")
        case 7:
            print("El dia de hoy es Domingo")
            print(f"El menu del dia es {menu[dia_semana]}")
        case _:
            print("EL numero ingresado no corresponde a un dia de la semana")

except:
    print("El valor ingresado no corresponde a un dia de la semana")