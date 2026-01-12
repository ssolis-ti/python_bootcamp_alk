numero1 = 10
numero2 = 3

#suma

resultado_suma = numero1 + numero2
print("Suma", resultado_suma)

#resta
resultado_resta = numero1 - numero2
print("Resta", resultado_resta)

#multiplicacion
resultado_multiplicacion = numero1 * numero2
print("multiplicacion", resultado_multiplicacion)

#division (normal)
#SIEMPRE DEVUELVE UN NUMERO DECIMAL, AUNQUE LA DIVISION SEA EXACTA

resultado_division = numero1 / numero2
print("Division", resultado_division)

resultado_modulo = numero1 % numero2    #calcula el resto de la division
print("modulo", resultado_modulo)    
#10 /3 -> me cabe 3 y el resto es 1

resultado_division_entera = numero1 // numero2 #entrega la parte entera de la division
print("Division entera", resultado_division_entera)

resultado_potencia = numero1**numero2  # 10^5
print("Potencia", resultado_potencia)
###################################################################
#Operadores de asignacion
print("***********************************************")

# numero1 = numero1 + 5
numero1 += 5

print("valor actual numero1", numero1)

#numero1 = numero1 -3
numero1 -= 3
print("valor actual numero1", numero1)

# numero1 = numero1 * 10 
numero1 *= 10
print("valor actual numero1", numero1)

# numero1 = numero1 / 5 
numero1 /= 5
print("valor actual numero1", numero1)


# numero1 = numero1 ** 5 
numero1 **= 5
print("valor actual numero1", numero1)
