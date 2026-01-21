#es pqarte de la libreria standar de python
from collections import defaultdict, Counter

#default

contadores = defaultdict(int) # int el valor por defecto de los elementos creados es  0
                        #str ''
contadores["python"] += 1
contadores["Python"] 
print(contadores)

# #####
# frecuencia = {}

# frecuencia["Perro"]# no encuentra la llave lanza un error


#counter

colores = ["Rojo", "azul", "rojo", "rojo", "azul"]

conteo = Counter(colores)

print(conteo)
