"""
1. Crear un diccionario con los datos: nombre, edad, email
2. Acceder a valores usando claves (persona["nombre"])
3. Modificar un dato (por ejemplo, actualizar la edad)
4. Agregar un nuevo dato ("país": "Argentina")
5. Eliminar un campo con pop() o del
6. Mostrar todas las claves, valores y pares con keys(), values(), items()
7. Iterar sobre el diccionario e imprimir: "clave: valor"
8. Usar get() para obtener un dato sin error si no existe
"""
#1 crear un diccionario
usuario = {
    "nombre": "Tony Stark",
    "edad": 40,
    "email":"tutonystark@correo.cl",
    "ocupacion": "Avenger",
    "vivo":False,
    "ultima_pelicula": "End game",
}

#2 acceder a valores
#para eso usamos las claves/key/llaves

print(usuario["edad"])
print(usuario["nombre"])
print(usuario["email"])

#3 actualizar la edad, en este caso con las llaves

usuario["edad"] = 45
print("Edad actualizada:",usuario["edad"])
#4 agregar dato
usuario["pais"] = "Estados Unidos"

print("Se agrega el pais",usuario) 

#5 elimianr dato con pop
usuario.pop("email")
# usuario.pop() #esto no sirve ya que necesita la llave del dato a eliminar

print("se elimina email",usuario)
#metodo del para eliminar edad
del usuario["edad"]

print("se elimina edad",usuario)

#6 Metodos especiales de los diccionarios keys(), values(), items()


#metodo keys
print(usuario.keys()) 
#dict_keys(['nombre', 'ocupacion', 'vivo', 'ultima_pelicula', 'pais'])
#este metodo me devuelve una lista de las llaves, del diccionario.

#metodo values()
#este metodo me devuelve los valores del diccionario
print(usuario.values())
#dict_values(['Tony Stark', 'Avenger', False, 'End game', 'Estados Unidos'])

#metodo items()

print(usuario.items()) #se parece al enumerate
#dict_items([('nombre', 'Tony Stark'), ('ocupacion', 'Avenger'), ('vivo', False), ('ultima_pelicula', 'End game'), ('pais', 'Estados Unidos')])
                # llave    valor            llave        valor       llave    valor    llave     valor        

#items me devuelve una lista de tuplas compuestas por clave y valor del diccionario

#7 iterar clave y valor
for key, value in usuario.items():
    print(f"llave: {key}, valor: {value}")

#8 metodo get

print(usuario.get("nombre")) #get me permite acceder a los datos del diccionario, usando como argumento la llave
#pero en caso de no encontrar el valor devuelve None
print(usuario.get("mascota")) 
#la diferencia de esto con
# usuario["mascota"] #KeyError por que mascota no e encuentra en el diccionario

