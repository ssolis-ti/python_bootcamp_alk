
"""
1. Crear un diccionario llamado libros donde la clave sea un ID ("B001", "B002", etc.)
2. Cada valor será un diccionario con:

"titulo": cadena
"autor": tupla con (nombre, año de nacimiento)
"genero": cadena
"stock": entero

3. Mostrar todos los libros disponibles
4. Permitir buscar libros por género ingresado por el usuario
5. Calcular cuántos libros hay por género usando Counter
6. Mostrar solo los libros con stock menor a 3 unidades
7. Agregar un nuevo libro y actualizar el stock de uno existente
8. Bonus: Eliminar un libro del diccionario por su código"""

libros = {
    "B001": {
        "titulo": "1984",
        "autor": ("George Orwell", 1903),
        "genero": "Distopía",
        "stock": 5
    },
    "B002": {
        "titulo": "El Hobbit",
        "autor": ("J. R. R. Tolkien", 1892),
        "genero": "Fantasía",
        "stock": 2
    },
    "B003": {
        "titulo": "Dune",
        "autor": ("Frank Herbert", 1920),
        "genero": "Ciencia ficción",
        "stock": 1
    },
    "B004": {
        "titulo": "Fahrenheit 451",
        "autor": ("Ray Bradbury", 1920),
        "genero": "Distopía",
        "stock": 4
    },
    "B005": {
        "titulo": "El nombre de la rosa",
        "autor": ("Umberto Eco", 1932),
        "genero": "Misterio",
        "stock": 3
    },
    "B006": {
        "titulo": "Crónica de una muerte anunciada",
        "autor": ("Gabriel García Márquez", 1927),
        "genero": "Novela",
        "stock": 6
    },
    "B007": {
        "titulo": "Neuromante",
        "autor": ("William Gibson", 1948),
        "genero": "Ciencia ficción",
        "stock": 2
    },
    "B008": {
        "titulo": "La sombra del viento",
        "autor": ("Carlos Ruiz Zafón", 1964),
        "genero": "Novela",
        "stock": 1
    }
}