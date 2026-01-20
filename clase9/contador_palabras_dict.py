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


frase = "Python es genial y Python es poderoso"

print(frase.split()) 


frecuencia = {}

print(frecuencia.get("es", 0))

for palabra in frase.split():

    frecuencia[palabra] = frecuencia.get(palabra,0) + 1

print(frecuencia)


