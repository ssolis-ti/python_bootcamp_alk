"""
este es un comentario de mas de una linea
que me interesa que conozcan los alumnos del curso
de python fullstack

este se considera un comentario (docstring) a menos que se almacene
en una varibale, donde pasa a ser un texto (str)
"""

#tipos de datos
## cadenas de texto
texto = "Hola mundo" #string -> str
texto2 = 'Hola mundo' #string -> str

texto_especial = """
hola
mundo 
como estas

yo bien y usted?

yo tambien

"""
print(texto_especial)


##numericas
numero1 = 12 #numero entero -> int
numero3 = 12.0 # el separador decimal es el que entrega el tipo de dato
numero2 = 12.5 #numero decimal -> float
#toda fraccion aunque sea exacta , python la considera como un numero decimal
ejemplo = 4/2
print(ejemplo)
print("tipo de dato de ejemplo",type(ejemplo))

## booleanos
booleano1 = True #booleano -> bool
booleano2 = False #booleano -> bool