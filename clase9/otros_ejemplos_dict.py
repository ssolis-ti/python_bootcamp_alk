#contar palabras
frase = "Python es genial y Python es poderoso"


#metodo split en python
print(frase.split()) #crea una lista de las palabras contenidas en un texto


frecuencia = {}

print(frecuencia.get("es", 0))
#el metodo get con solo 1 argumento, busca esa palabra en el diccionario y si no la encuentra
#devuelve None (no encontrado). PERO si contiene un segundo argumento, ese argumento
#me entrega el valor por defecto que devolvera si no encuentra la llave

for palabra in frase.split():

    frecuencia[palabra] = frecuencia.get(palabra,0) + 1

print(frecuencia)


##diccionarios anidados

producto = {
    "nombre": "Laptop",
    "precio": 1200,
    "especificaciones":{"RAM":"16GB","Disco":"512 GB SSD"}
}

print(producto["nombre"])

#acceder a un elemento del diccionario anidado
# dict_especificaciones = producto["especificaciones"]
# dict_especificaciones["Disco"]

print(producto["especificaciones"]["Disco"])
