
#ejemplo de compresion de lista seria

cuadrados = [ x**2 for x in range(10)]

"""
cuadrados = []

for elemento in range(10):
    cuadrados.append(elemento**2)"""

# print(cuadrados)

pares = { x : x**2 for x in range(10)}
# print(pares)



#uso de generadores

def numeros(n):
    for i in range(n):
        yield i
#alamacena en memoria una lista
print(numeros(9)) #onjeto consu hash de memoria en el sistema

for numero in numeros(9):
    print(numero)