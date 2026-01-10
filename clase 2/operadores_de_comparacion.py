#comparacion , SIEMPRE DEVUELVEN True o False (booleanos)
numero1 = 5
numero2 = 3

print("5 es mayor que 3?", numero1 > numero2)

print("5 es menor que 3?", numero1 < numero2)
print("5 es distinto que 3?", numero1 != numero2)

numero2 = 5
print("5 es igual que 5?", numero1 == numero2)
print("5 es mayor o igual que 5?", numero1 >= numero2)
print("5 es menor o igual que 5?", numero1 <= numero2)

#########################operadores logicos
edad = 18
tiene_licencia = True
#   && -> and y
if edad >= 18 and tiene_licencia: # y
    print("como tiene licencia y es mayor de edad, puede conducir")

# || or 
es_amarillo = False
es_verde = True
#caso del semaforo
if es_amarillo or es_verde:  #en el or basta con que una de las dos condiciones sea verdadero para que toda la operacion sea verdadera
    print("puedo seguir conduciendo")
else:
    print("detenerse inmediatamente")

print(not True) #-> False
print(not False) #-> True


### voy a un concierto (para mayores de 18)
### tengo entrada y(soy mayor de edad  o voy acompadaño de un adulto)
#con un input capturo la edad, saber si tiene entrada   'Si' -> True
#viene con adulto acompañante
es_mayor_de_edad = True #edad>=19
tiene_entrada = False 
viene_con_adulto = False

if tiene_entrada and(es_mayor_de_edad or viene_con_adulto):
    print("puede ingresar al concierto")
else:
    print("no puede ingresar al concierto")