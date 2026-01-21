"""
1. Solicitar al usuario que ingrese una frase
2. Dividir la frase en palabras usando .split()
3. Crear un diccionario vacío llamado frecuencia
4. Recorrer las palabras con un for
5. Usar get() para contar cuántas veces aparece cada palabra
6. Guardar cada conteo como clave: valor (palabra: cantidad)
7. Imprimir el diccionario final con las frecuencias
8. Bonus: Ordenar el diccionario por frecuencia descendente
"""

#1
frase = input("Ingrese una frase para contar sus palabras: ")

#2 Dividir la frase en una lista de palabras
palabras = frase.split()

#3 Creamos el diccionario llamado frecuencia
frecuencia = {}


#4 recorrer palabras con un for
for palabra in palabras:
    #5 y 6 seria en este paso
    frecuencia[palabra] = frecuencia.get(palabra,0) + 1

#7
print(frecuencia)

#8 bonus
ordenado_desc = dict(
    sorted(frecuencia.items(), key=lambda item: item[1], reverse=True) #valores
)
print(ordenado_desc)